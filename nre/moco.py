"""
MOCO: motion correct volumes
- align moving volumes to a fixed brain using ANTsPy SyN

07 dec 2023
@author: sama ahmed

todo:
[ ] ??
"""

import numpy as np
import ants


def apply(fixed, moving):
    moco_moving = ants.registration(fixed, moving, type_of_transform='SyN')
    return moco_moving["warpedmovout"]


