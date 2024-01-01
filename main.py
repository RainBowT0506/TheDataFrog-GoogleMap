import pandas as pd
from bokeh.io import output_notebook
output_notebook()
bokeh_width, bokeh_height = 500,400

df = pd.read_csv('dvf_gex.csv')

print(df.head())