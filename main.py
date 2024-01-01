import pandas as pd
import os

from Constant import API_Key_Google_Map
from bokeh.io import output_file, show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions

bokeh_width, bokeh_height = 500, 400

df = pd.read_csv('dvf_gex.csv')

print(df.head())

lat, lng = 46.2437, 6.0251

def plotRoadMap(lat, lng, zoom=10, map_type='roadmap'):
    output_file(map_type + ".html")
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    show(p)
    output_file("Roadmap.html")
    return p

def plotCircleMarker(lat, lng, zoom=10, map_type='roadmap'):
    output_file("CircleMarker-"+map_type + ".html")
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    # beware, longitude is on the x axis ;-)
    center = p.circle([lng], [lat], size=10, alpha=0.5, color='red')
    show(p)
    return p

# p = plotRoadMap(lat, lng)

p = plotCircleMarker(lat, lng, map_type='terrain')

show(p)

