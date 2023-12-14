import numpy as np
from scipy.ndimage import gaussian_filter1d


def _zscore(x):
    """x: 2D array (n, t)"""

    x_mean = np.mean(x, axis=-1)
    x_std = np.std(x, axis=-1)
    return (x - x_mean[:, None]) / x_std[:, None]


def _zdff(F, win=200, smooth=False):
    """calculate zscored(df/f) based on F baseline activity"""

    # find average signal in first `win` volumes
    Fbase = np.mean(F[:, :win], axis=-1)
    dff = (F - Fbase[:, None]) / Fbase[:, None]

    if smooth:
        dff = gaussian_filter1d(dff, sigma=1)

    return _zscore(dff)