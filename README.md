# nifty roi extractor

Loads .nii file (xyzt), runs motion correction via ants, and extracts ROIs over time.

## Pre-requisites

- [Anaconda](https://www.anaconda.com/download)
- [homebrew](https://brew.sh/)
- [ANTsPy](https://github.com/ANTsX/ANTsPy)

### installing ANTsPy
ANTsPy is powerful but challenging to install. It may help to first install `cmake` and/or `libpng`

-- `pip install cmake`  
-- `brew install libpng`  

then run:  
-- `pip install antspyx`  

#### debugging ants install

If that doesn't work, make sure you have the correct python version.   

`python --version`  

For example, I installed `python 3.11` and then ran this to pull a [specific release](https://github.com/ANTsX/ANTsPy/releases):  

`pip install https://github.com/ANTsX/ANTsPy/releases/download/v0.4.2/antspyx-0.4.2-cp311-cp311-macosx_10_9_x86_64.whl`  

note: "cp311" refers to `python 3.11`  

