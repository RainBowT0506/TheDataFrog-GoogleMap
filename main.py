import pandas as pd
import os

from Constant import API_Key_Google_Map
from bokeh.io import output_file, show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions, ColumnDataSource
from bokeh.models import HoverTool
import numpy as np
from bokeh.transform import linear_cmap
from bokeh.palettes import Plasma256 as palette
from bokeh.models import ColorBar

bokeh_width, bokeh_height = 1024, 768
lat, lng = 46.2437, 6.0251

df = pd.read_csv('dvf_gex.csv')
pd.set_option('display.max_columns', None)

def plotBasicMap(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Basic Map',
             width=bokeh_width, height=bokeh_height)
    show(p)
    output_file("Basic Map.html")
    return p


def plotMapWithCenterMarker(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Map with Center Marker',
             width=bokeh_width, height=bokeh_height)
    center = p.circle([lng], [lat], size=10, alpha=0.5, color='red')
    show(p)
    output_file("Map with Center Marker.html")
    return p


def plotMapWithMultiplePoints(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    p = gmap(API_Key_Google_Map, gmap_options, title='Map with Multiple Points',
             width=bokeh_width, height=bokeh_height)
    # definition of the column data source:
    source = ColumnDataSource(df)
    # see how we specify the x and y columns as strings,
    # and how to declare as a source the ColumnDataSource:
    center = p.circle('lon', 'lat', size=4, alpha=0.2,
                      color='yellow', source=source)
    show(p)
    output_file("Map with Multiple Points.html")
    return p


def plotMapWithTools(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    # the tools are defined below:
    p = gmap(API_Key_Google_Map, gmap_options, title='Map with Tools',
             width=bokeh_width, height=bokeh_height,
             tools=['hover', 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    center = p.circle('lon', 'lat', size=4, alpha=0.5,
                      color='yellow', source=source)
    show(p)
    output_file("Map with Tools.html")
    return p


def plotMapWithCustomHoverTool(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    # the tools are defined below:
    hover = HoverTool(
        tooltips=[
            # @price refers to the price column
            # in the ColumnDataSource.
            ('price', '@price euros'),
            ('building', '@area_build m2'),
            ('terrain', '@area_tot m2'),
        ]
    )
    # below we replaced 'hover' (the default hover tool),
    # by our custom hover tool
    p = gmap(API_Key_Google_Map, gmap_options, title='Map with Custom Hover Tool',
             width=bokeh_width, height=bokeh_height,
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    center = p.circle('lon', 'lat', size=4, alpha=0.5,
                      color='yellow', source=source)
    show(p)
    output_file("Map with Custom Hover Tool.html")
    return p

def plotScaledCircleSizesMap(lat, lng, zoom=10, map_type='roadmap'):
    df['radius'] = np.sqrt(df['price']) / 200.

    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    hover = HoverTool(
        tooltips = [
            ('price', '@price euros'),
            ('building', '@area_build m2'),
            ('terrain', '@area_tot m2'),
        ]
    )
    p = gmap(API_Key_Google_Map, gmap_options, title='Scaled Circle Sizes Map',
             width=bokeh_width, height=bokeh_height,
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    # we use the radius column for the circle size:
    center = p.circle('lon', 'lat', size='radius',
                      alpha=0.5, color='yellow', source=source)
    show(p)
    output_file("Scaled Circle Sizes Map.html")
    return p

def plotAdjustedRadiusMap(lat, lng, zoom=10, map_type='roadmap'):
    # need to change the radius coefficient
    # so that the points are visible
    df['radius'] = np.sqrt(df['price']) / 5.

    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    hover = HoverTool(
        tooltips = [
            ('price', '@price euros'),
            ('building', '@area_build m2'),
            ('terrain', '@area_tot m2'),
        ]
    )
    p = gmap(API_Key_Google_Map, gmap_options, title='Adjusted Radius Map',
             width=bokeh_width, height=bokeh_height,
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    # see how we set radius instead of size:
    center = p.circle('lon', 'lat', radius='radius', alpha=0.5,
                      color='yellow', source=source)
    show(p)
    output_file("Adjusted Radius Map.html")
    return p

def plotColorMappedCirclesMap(df, lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    hover = HoverTool(
        tooltips = [
            ('price', '@price euros'),
            # the {0.} means that we don't want decimals
            # for 1 decimal, write {0.0}
            ('price/m2', '@pricem2{0.}'),
            ('building', '@area_build m2'),
            ('terrain', '@area_tot m2'),
        ]
    )
    p = gmap(API_Key_Google_Map, gmap_options, title='Color-Mapped Circles Map',
             width=bokeh_width, height=bokeh_height,
             tools=[hover, 'reset', 'wheel_zoom', 'pan'])
    source = ColumnDataSource(df)
    # defining a color mapper, that will map values of pricem2
    # between 2000 and 8000 on the color palette
    mapper = linear_cmap('pricem2', palette, 2000., 8000.)
    # we use the mapper for the color of the circles
    center = p.circle('lon', 'lat', radius='radius', alpha=0.6,
                      color=mapper, source=source)
    # and we add a color scale to see which values the colors
    # correspond to
    color_bar = ColorBar(color_mapper=mapper['transform'],
                         location=(0,0))
    p.add_layout(color_bar, 'right')
    show(p)
    output_file("Color-Mapped Circles Map.html")
    return p


p = plotBasicMap(lat, lng)

p = plotMapWithCenterMarker(lat, lng, map_type='terrain')

p = plotMapWithMultiplePoints(lat, lng, map_type='satellite')

p = plotMapWithTools(lat, lng, map_type='satellite', zoom=12)

p = plotMapWithCustomHoverTool(lat, lng, map_type='satellite', zoom=12)

p = plotScaledCircleSizesMap(lat, lng, map_type='satellite', zoom=11)

p = plotAdjustedRadiusMap(lat, lng, map_type='satellite', zoom=11)

df['radius'] = np.sqrt(df['price']) / 5.
dfb = df[df['area_build'] > 0.].copy()
dfb['pricem2'] = dfb['price'] / dfb['area_build']
print(dfb.head())
p = plotColorMappedCirclesMap(dfb, lat, lng, map_type='roadmap', zoom=11)


