### Warp raster

from osgeo import gdal

filename = "/Users/nathanieldouglass/Desktop/merged_dem/dem_GDTM.0.tif"
input_raster = gdal.Open(filename)
output_raster = "/Users/nathanieldouglass/Desktop/alaska_dem.tif"
gdal.Warp(output_raster,input_raster,dstSRS='EPSG:102006')