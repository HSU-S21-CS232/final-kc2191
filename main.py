#With the help of Dr. Tyler Mitchell of the Astronomy department at HSU, I decided to analyze if there is a correlation between exoplanets
#and false positives
#i'm going to first do an analyzition of data acquired from Hubble Telescope, and then do imaging stuff myself

import pandas as pd
import numpy as numpy

from astropy.io import fits

M43 = fits.open('m56.fits')

print(M43[0])

print(M43[0].header)

M43.info()

data = M43[0].data

print(type(data))