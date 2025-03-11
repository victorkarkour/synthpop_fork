import pandas as pd
from astropy.io import fits
from astropy.table import Table

hdul = fits.open("/home/victor/SURP/Synthpop_Tests/1_obj_norm.ms.fits")
data = Table(hdul[0].data)

RV1 = data.to_pandas()

print(RV1)