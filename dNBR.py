
#final project for python
##this project is also designed for python 3.6
##first we must install git, bash, and anaconda to local computer
##after those are installed we need to install earth-analytics-python environment

#** means that we are missing a step here and need to figure it out

##this program does the following in this order

##1. opens pre fire landsat data and calculates the NBR of prefire

##2. opens post fire data and calculates NBR of postfire

##3. calculates dNBR using simple rater functions

##4. classifies fire damage using certain value ranges in dNBR

##5. calculates areas of no burn, low, moderate, and high fire damage.

##6. generates color map of dNBR

##7. plots these classes in a graph

## first we have to install python libraries


##numpy and glob modules with descriptions
"""numpy is for scientific computing"""
import numpy as np

"""reads filepaths using unix path extensions"""
from glob import glob

"""adds operating system dependant functionality"""
import os


##matplotlib and seaborn modules with descriptions
"""2-D plotting library that make matplotlib work like MATLAB"""
import matplotlib.pyplot as plt

"""A patch is a 2D artist with a face color and an edge color."""
from matplotlib import patches as mpatches

"""imports color map used for plotting"""
from matplotlib.colors import ListedColormap

"""imports color options in plotting"""
from matplotlib import colors

"""renames matplotlib to mpl to make shorthand easier"""
import matplotlib as mpl

"""this is a data visualization library that
works in tandem with matplotlib"""
import seaborn as sns



##rasterio module and descriptions
"""rasterio stores grid info of tiff files"""
import rasterio as rio

"""plotting_extent sets the extent of the image"""
from rasterio.plot import plotting_extent

"""mask makes filled array based on shapefile boundaries"""
from rasterio.mask import mask




##geopandas and earthpy modules with descriptions
"""geopandas is used for reading geospatial data"""
import geopandas as gpd

"""shapely works specifically with spatial files like shape, point, lines ect..
this specific tool allows for mapping and bounding boxes i think"""
from shapely.geometry import mapping, box

"""earthpy is a module that uses geopandas and rasterios and matplotlib
to better work with geospatial data and vector data
specifically for scientific purposes"""
import earthpy as et
import earthpy.spatial as es

"""this sets the background to white for plots"""
sns.set_style('white')

"""filepath for project"""
os.path.join("P:/python final project/data")

#NBR post fire calculations

"""this line pulls all of the landsat bands file for the postfire NBR"""
all_landsat_bands = glob(
    "data/cold-springs-fire/landsat_collect/LC080340322016072301T1-SC20180214145802/crop/*band*.tif")

"this compiles and sorts the landsat bands" 
all_landsat_bands.sort()


"""setting our output file path"""
landsat_post_fire_path = "data/cold-springs-fire/outputs/landsat_post_fire.tif"

"""es.stack will stack all bands on top of one another.
making raster values more easily comparable."""
es.stack_raster_tifs(all_landsat_bands,
                     landsat_post_fire_path)


# we can clip the files but in this case we use .read()
"""the next 5 lines will open the file, set up profile, set up bounding box,
our plotting extent, and validates that our data has values assigned to array"""

with rio.open(landsat_post_fire_path) as src:
    landsat_post_fire = src.read(masked=True)
    landsat_post_meta = src.profile
    landsat_post_bounds = src.bounds
    landsat_extent = plotting_extent(src)


# Open fire boundary layer and reproject it to match the Landsat data
fire_boundary_path = "data/cold-springs-fire/vector_layers/fire-boundary-geomac/co_cold_springs_20160711_2200_dd83.shp"
fire_boundary = gpd.read_file(fire_boundary_path)


# If the CRS' are not the same be sure to reproject
"""this reprojects the coordinate reference system for the fire boundary"""
fire_bound_utmz13 = fire_boundary.to_crs(landsat_post_meta['crs'])


#calculating NBR postfire and plotting results
"""this calculates postfire NBR"""
landsat_postfire_nbr = (
    landsat_post_fire[4]-landsat_post_fire[6]) / (landsat_post_fire[4]+landsat_post_fire[6])

"""sets plot parameters"""
fig, ax = plt.subplots(figsize=(12, 6))
"""sets a divergent colormap, legend, and value extents"""
nbr_post = ax.imshow(landsat_postfire_nbr,
                 cmap='PiYG',
                 vmin=-1,
                 vmax=1,
                 extent=landsat_extent)

"""this projects fire boundary on map.
also sets no color fill but a 2pt width black border"""
fire_bound_utmz13.plot(ax=ax, color='None',
                       edgecolor='black', linewidth=2)
"""makes colorbar in the plot so we have a legend with our colormap"""
fig.colorbar(nbr_post)
ax.set(title="Landsat derived Normalized Burn Ratio\n 23 July 2016 \n Post Cold Springs Fire")
ax.set_axis_off()
plt.show()

# stack bands NBR prefire.
"""loads all landsat bands from file"""
all_landsat_bands_pre = glob(
    "data/cold-springs-fire/landsat_collect/LC080340322016070701T1-SC20180214145604/crop/*band*.tif")
"""sorts bands from 1-7"""
all_landsat_bands_pre.sort()
"""this sets output location for our prefire NBR tif"""
landsat_pre_fire_path = "data/cold-springs-fire/outputs/landsat_pre_fire.tif"

es.stack_raster_tifs(all_landsat_bands_pre,
                     landsat_pre_fire_path)

# again we not cropping the data in this lesson so you can just use .read()
with rio.open(landsat_pre_fire_path) as src2:
    landsat_pre_fire = src2.read(masked=True)
    landsat_pre_meta = src2.profile
    landsat_pre_bounds = src2.bounds
    landsat_extent = plotting_extent(src2)

# Open fire boundary layer and reproject it to match the Landsat data
fire_boundary_path_pre = "data/cold-springs-fire/vector_layers/fire-boundary-geomac/co_cold_springs_20160711_2200_dd83.shp"
fire_boundary_pre = gpd.read_file(fire_boundary_path)

# setting the CRS to utm13 again
"""this reprojects the coordinate reference system for the fire boundary"""
fire_bound_utmz13_pre = fire_boundary_pre.to_crs(landsat_pre_meta['crs'])


#calculating NBR prefire and plotting results
"""this calculates prefire NBR"""
landsat_prefire_nbr = (
    landsat_pre_fire[4]-landsat_pre_fire[6]) / (landsat_pre_fire[4]+landsat_pre_fire[6])

"""sets plot parameters"""
fig, ax = plt.subplots(figsize=(12, 6))
"""sets a divergent colormap, legend, and value extents"""
nbr_pre = ax.imshow(landsat_prefire_nbr,
                 cmap='PiYG',
                 vmin=-1,
                 vmax=1,
                 extent=landsat_extent)

"""this projects fire boundary on map.
also sets no color fill but a 2pt width black border"""
fire_bound_utmz13_pre.plot(ax=ax, color='None',
                       edgecolor='black', linewidth=2)
"""makes colorbar in the plot so we have a legend with our colormap"""
fig.colorbar(nbr_pre)
ax.set(title="Landsat derived Normalized Burn Ratio\n 7 July 2016 \n Pre Cold Springs Fire")
ax.set_axis_off()
plt.show()


#cropping NBR prefire
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(landsat_prefire_nbr, cmap='PiYG',
          extent=plotting_extent(nbr_pre_chm))
crop_extent.plot(ax=ax, alpha=.8)
ax.set_title("NBR prefire")
ax.set_axis_off()

# create geojson object from the shapefile imported above
"""geojson is a text structured format that allows us to set vertex extents of
our clipping extent. this is like when you use clip tool in
arcpro and it has the vertices listed."""
extent_geojson = mapping(crop_extent_nbr['geometry'][0])
extent_geojson
{'type': 'Polygon',
 'coordinates': (((472510.46511627914, 4436000.0),
   (476009.76417479065, 4436000.0),
   (476010.46511627914, 4434000.0),
   (472510.46511627914, 4434000.0),
   (472510.46511627914, 4436000.0)),)}

"""with the vertexes set we can now clip image"""
with rio.open(data/cold-springs-fire/outputs/landsat_pre_fire.tif) as nbr_pre_chm:
    nbr_pre_chm_crop, nbr_pre_chm_crop_affine = mask(nbr_pre_chm,
                                                 [extent_geojson],
                                                 crop=True)
# export NBR prefire
path_out = "data/colorado-flood/spatial/outputs/nbr_pre_chm_cropped.tif"
with rio.open(path_out, 'w', **nbr_pre_chm_meta) as ff_pre:
    ff_pre.write(nbr_pre_chm_crop[0], 1)
    
#cropping and plotting NBR postfire
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(landsat_prefire_nbr, cmap='PiYG',
          extent=plotting_extent(nbr_post_chm))
crop_extent.plot(ax=ax, alpha=.8)
ax.set_title("NBR postfire")
ax.set_axis_off()

# create geojson object from the shapefile imported above
"""geojson is a text structured format that allows us to set vertex extents of
our clipping extent. this is like when you use clip tool in
arcpro and it has the vertices listed."""
extent_geojson = mapping(crop_extent_nbr['geometry'][0])
extent_geojson
{'type': 'Polygon',
 'coordinates': (((472510.46511627914, 4436000.0),
   (476009.76417479065, 4436000.0),
   (476010.46511627914, 4434000.0),
   (472510.46511627914, 4434000.0),
   (472510.46511627914, 4436000.0)),)}

"""with the vertexes set we can now clip image"""
with rio.open(data/cold-springs-fire/outputs/landsat_post_fire.tif) as nbr_post_chm:
    nbr_post_chm_crop, nbr_post_chm_crop_affine = mask(nbr_post_chm,
                                                 [extent_geojson],
                                                 crop=True)
# export NBR prefire
path_out = "data/colorado-flood/spatial/outputs/nbr_post_chm_cropped.tif"
with rio.open(path_out, 'w', **nbr_post_chm_meta) as ff_post:
    ff_post.write(nbr_post_chm_crop[0], 1)

dnbr_landsat = nbr_pre_chm_cropped - nbr_post_chm_cropped

####this is where the lesson leaves me behind. 
##to do rest of project i need to research how to set an array 
##reclass the array into low, moderate, and high intensity burns
##once that is taken care of i can do the statistics and histogram
##part of this project. overall just a little bit above my head.

