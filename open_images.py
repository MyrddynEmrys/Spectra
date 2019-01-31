from astropy.io import fits
import glob
import numpy as np
np.version.version
from matplotlib import pyplot as plt
%matplotlib inline
from scipy import ndimage


darks = []
flats = []
dead_pixel = []
spectra = []
