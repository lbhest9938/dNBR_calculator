
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
