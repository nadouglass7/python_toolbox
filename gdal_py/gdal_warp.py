### Warp raster

from osgeo import gdal

filename = r"/Volumes/GoogleDrive/My\ Drive/Projects/Vintage_Alaska/working/raster/gdtm_alaska.tif "
input_raster = gdal.Open(filename)
output_raster = r"/Volumes/GoogleDrive/My\ Drive/Projects/Vintage_Alaska/working/raster/projected/gdtm_alaska.tif"
gdal.Warp(output_raster,input_raster,dstSRS='EPSG:102006')