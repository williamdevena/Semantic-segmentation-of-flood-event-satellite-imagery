import rasterio
from rasterio.plot import show
from matplotlib import pyplot
import glob

files=glob.glob("../WORLDFLOODS/val/S2/*")

for file in files:
	src = rasterio.open(file)
	array = src.read(1)
	pyplot.imshow(array)
	pyplot.show()
#fp = '../WORLDFLOODS/val/S2/EMSR271_02FARKADONA_DEL_v1_observed_event_a.tif'
# img = rasterio.open(fp)
# show(img)