import numpy as np
import h5py
import os
import glob
from nre import io, moco, roi
import ants

from util import _zscore, _zdff

import matplotlib.pyplot as plt


def main():


if __name__ == "__main__":
    main()
    dropboxDir = "/Users/kyle/Library/CloudStorage/Dropbox-ahmedlab/ahmedlab-big/kyle/data"
    fly = '231213_106-013'
    dataDir = os.path.join(dropboxDir, fly)
    nifty_paths_ch1 = glob.glob(os.path.join(dataDir, fly+'_channel_1*.nii'))
    nifty_paths_ch2 = glob.glob(os.path.join(dataDir, fly+'_channel_2*.nii'))


    print("num ch1 .nii files: ", len(nifty_paths_ch1))
    print("num ch2 .nii files: ", len(nifty_paths_ch2))

    labels_path = os.path.join(dataDir, fly+'_labels.h5')

    if len(nifty_paths_ch1)> 1:
        split_nifty = True