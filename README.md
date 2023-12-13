# ahmed lab rotation project
this initial repository was cloned from here: [nifty-roi-extractor](https://github.com/oahmedlab/nifty-roi-extractor)  
the rest of this repository contains code related to my rotation project

## Pre-requisites

- [Anaconda](https://www.anaconda.com/download)
- [homebrew](https://brew.sh/)
- [ANTsPy](https://github.com/ANTsX/ANTsPy)
- [h5py](https://docs.h5py.org/en/stable/build.html)

### installing ANTsPy
ANTsPy is powerful but challenging to install. It may help to first install `cmake` and/or `libpng`

-- `pip install cmake`  
-- `brew install libpng`  

then run:  
-- `pip install antspyx`  

#### debugging ANTsPy install

If that doesn't work, make sure you have the correct python version.   

`python --version`  

For example, you can install `python 3.11` in your environment and then run the following `pip install` to pull a [specific release](https://github.com/ANTsX/ANTsPy/releases):  

`pip install https://github.com/ANTsX/ANTsPy/releases/download/v0.4.2/antspyx-0.4.2-cp311-cp311-macosx_10_9_x86_64.whl`  

note: "cp311" refers to `python 3.11`  

