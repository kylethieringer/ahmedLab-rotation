import numpy as np
import h5py
import os
import glob
from nre import io, moco, roi
import ants
from multiprocessing import Pool
from util import _zscore, _zdff

import matplotlib.pyplot as plt


def stabilize_brain(brain, fixed, savepath=None, save=False, overwrite=False):
    
    if not overwrite and os.path.exists(savepath+'_moco.nii'):
        
        print("loading previous moco_brain")
        moco_brain = io.load(savepath+'_moco.nii')
        
        return moco_brain
    
    n_vols = brain.shape[-1]

    moco_brain = np.zeros_like(brain)

    for vol in range(n_vols):
        moving = ants.from_numpy(brain[:, :, :, vol])
        moco_brain[:, :, :, vol] = moco.apply(fixed, moving).numpy()

    if save:
        io.save(savepath+'_moco.nii', moco_brain)
    
    return moco_brain


def fix_brain(brain, savepath=None, save=False, overwrite=False):
    """
    savepath : the identifier for the specific fly and split file
                shouldnt be a whole filepath, we will append the ending
    """

    if not overwrite and os.path.exists(savepath+"_mean_brain.nii"):
        print("loading previous mean brain")
        mean_brain = io.load(savepath+"_mean_brain.nii")
        fixed = ants.from_numpy(mean_brain)
        return fixed
    
    mean_brain = np.mean(brain, axis=-1)

    fixed = ants.from_numpy(mean_brain)
    
    if save:
        io.save(savepath+'_mean_brain.nii', mean_brain)

    return fixed


def get_labels(moco_brain, n_clusters, savepath=None, save=False, overwrite=False):
    
    if not overwrite and os.path.exists(savepath+'_labels.h5'):
        print("loading previous labels")
        with h5py.File(savepath+'_labels.h5', 'r') as f:
            labels = f['labels'][:]
        return labels
    
    labels = []
    # for each slice in Z, generate n_clusters of pixels and return the pixel label
    for iSlice in range(moco_brain.shape[2]):
        cluster_model = roi.create_2d_clusters(moco_brain[:, :, iSlice, :], n_clusters, 'tmp/cluster_mem')
        labels.append(cluster_model.labels_)
    
    if save:
        with h5py.File(savepath+'_labels.h5', 'w') as f:
            f.create_dataset('labels', data=labels)
        
    return labels



def get_ROIs(moco_brain, n_clusters=100, savepath=None, save=False, overwrite=False):
    
    if not overwrite and os.path.exists(savepath+'_ROIs.nii'):
        ROIs = io.load(savepath+'_ROIs.nio')
        return ROIs
    
    labels = get_labels(moco_brain, n_clusters, savepath=savepath, save=True)
    
    n_vols = moco_brain.shape[-1]
    n_slices = moco_brain.shape[2]

    F_WINDOW = n_vols

    ROIs = np.empty((n_slices, n_clusters, n_vols))

    for iSlice in range(n_slices):
        mean_signal = np.empty(shape=(n_vols, n_clusters))

        for vol in range(n_vols):
            mean_supervox, _ = roi.get_supervoxel_mean_2D(moco_brain[:, :, iSlice, vol], labels[iSlice], n_clusters)
            mean_signal[vol] = mean_supervox

        # find zscored(df/f) and smooth over time
        ROIs[iSlice, :, :] = _zdff(mean_signal.T, win=F_WINDOW, smooth=True)
    
    if save:
        io.save(savepath+'_ROIs.nii', ROIs)

    return ROIs


def process_brain(dataDir, niiFile, channel, split=False, save=False, overwrite=False):
    print("processing : ", niiFile)
    
    if split:
        splitID = os.path.basename(niiFile).split('_')[-1].split('.')[0]
    else:
        splitID = ""
    savepath = os.path.join(dataDir, f"{channel}_{splitID}")

    brain = io.load(niiFile)
    print("brain loaded")

    fixed = fix_brain(brain, savepath=savepath, save=save, overwrite=overwrite)
    print("brain fixed")

    moco_brain = stabilize_brain(brain, fixed, savepath=savepath, save=save, overwrite=overwrite)
    print("motion corrected")

    return moco_brain, savepath



def main(dataDir, fly, ch1_paths, ch2_paths):
    labels_path = os.path.join(dataDir, fly+'_labels.h5')

    print("num ch1 .nii files: ", len(ch1_paths))
    print("num ch2 .nii files: ", len(ch2_paths))

    split_nifty=False
    if len(nifty_paths_ch1)> 1:
        split_nifty = True
    
    for niiFile in nifty_paths_ch2:
        channel = "2" # make this modular so we can analyze both channels in future

        moco_brain, savepath = process_brain(dataDir, niiFile, channel, split=split_nifty, save=True, overwrite=False) 

        rois = get_ROIs(moco_brain, n_clusters=100, savepath=savepath, save=True)


if __name__ == "__main__":
    
    dropboxDir = "/Users/kyle/ahmedlab Dropbox/ahmedlab-big/princess/data/"
    fly = ['TSeries-12132023-1329-000']
    
    for f in fly:
        dataDir = os.path.join(dropboxDir, f)
        nifty_paths_ch1 = glob.glob(os.path.join(dataDir, f+'_channel_1*.nii'))
        nifty_paths_ch2 = glob.glob(os.path.join(dataDir, f+'_channel_2*.nii'))

        main(dataDir, f, nifty_paths_ch1, nifty_paths_ch2)