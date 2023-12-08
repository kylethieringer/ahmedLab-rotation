#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

def save_nii(fpath, volume):
    pass

def load_pickle(fpath):
    pass

def save_pickle(fpath):
    pass
