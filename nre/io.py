"""
IO: input/output utils for loading, saving image arrays
07 dec 2023
@author: sama ahmed

todo:
[ ] ??
"""

import os
import glob
import ants
import logging

LOG = logging.getLogger(__name__)


def load(fpath: str):
    """loads volume from filepath and returns N-Dim numpy array"""
    LOG.info(f"loading: {fpath}")
    imgarray = ants.image_read(fpath)
    volume = imgarray.numpy()
    LOG.debug(f"volume shape: {volume.shape}")
    return volume

def save(fpath: str, volume):
    "save volume to fpath"
    ants.image_write(ants.from_numpy(volume), fpath)
    LOG.info(f'saved volume to: {fpath}')

def load_pickle(fpath):
    pass

def save_pickle(fpath):
    pass
