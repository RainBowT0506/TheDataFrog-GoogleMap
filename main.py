import pandas as pd
import os

from Constant import API_Key_Google_Map
from bokeh.io import output_file, show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions,ColumnDataSource
from bokeh.models import HoverTool


bokeh_width, bokeh_height = 500, 400

df = pd.read_csv('dvf_gex.csv')

print(df.head())

lat, lng = 46.2437, 6.0251

def plotType1(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    show(p)
    output_file("Roadmap.html")
    return p

def plotType2(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    # beware, longitude is on the x axis ;-)
    center = p.circle([lng], [lat], size=10, alpha=0.5, color='red')
    show(p)
    output_file("Terrain.html")
    return p



def plotType3(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    # definition of the column data source:
    source = ColumnDataSource(df)
    # see how we specify the x and y columns as strings,
    # and how to declare as a source the ColumnDataSource:
    center = p.circle('lon', 'lat', size=4, alpha=0.2,
                      color='yellow', source=source)
    show(p)
    output_file("Satellite.html")
    return p

def plotType4(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    # the tools are defined below:
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height,
             tools=['hover', 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    center = p.circle('lon', 'lat', size=4, alpha=0.5,
                      color='yellow', source=source)
    show(p)
    return p

def plotType5(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    # the tools are defined below:
    hover = HoverTool(
        tooltips = [
            # @price refers to the price column
            # in the ColumnDataSource.
            ('price', '@price euros'),
            ('building', '@area_build m2'),
            ('terrain', '@area_tot m2'),
        ]
    )
    # below we replaced 'hover' (the default hover tool),
    # by our custom hover tool
    p = gmap(API_Key_Google_Map, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height,
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    center = p.circle('lon', 'lat', size=4, alpha=0.5,
                      color='yellow', source=source)
    show(p)
    return p

# p = plotType1(lat, lng)
#
# p = plotType2(lat, lng, map_type='terrain')
#
# p = plotType3(lat, lng, map_type='satellite')

# p = plotType4(lat, lng, map_type='satellite', zoom=12)

p = plotType5(lat, lng, map_type='satellite', zoom=12)


