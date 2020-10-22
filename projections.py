import pyproj
from functools import partial
from pyproj import Transformer

projections = {
    "wgs84": "EPSG:4326",
    "israel": "EPSG:2039"
}




def convertGeometry(x,y, fromCRS, toCRS) :
    transformer = Transformer.from_crs(projections[fromCRS], projections[toCRS])
    x,y = transformer.transform(x, y)
    return x,y