#####
# Setting environment variable. NOTE: This is not a production-safe practice.
# This is only acceptable because this is a lab.
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mjumbewu/.google-cloud/musa-509-2021-82382711a91a.json'
#####

import geopandas as gpd
import pandas as pd
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

template_root = Path(__file__).parent / 'templates'
output_root = Path(__file__).parent.parent / 'output'

def main():
    # Download the map data, and convert geometry to column to actual geometry
    # objects.
    mapdata_df = pd.read_gbq('SELECT * FROM lab09.blockgroups_mapdata')
    mapdata_df.blockgroup_geom = gpd.GeoSeries.from_wkt(mapdata_df.blockgroup_geom)
    mapdata_gdf = gpd.GeoDataFrame(mapdata_df, geometry='blockgroup_geom')

    # Download the chart data.
    chartdata_df = pd.read_gbq('SELECT * from lab09.blockgroups_chartdata')

    # Download the population density list data.
    listdata_df = pd.read_gbq('SELECT * from lab09.blockgroups_listdata')

    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))
    template = env.get_template('index.html')
    output = template.render(
        mapdata=mapdata_gdf.to_json(),
        chartdata=chartdata_df.to_dict('list'),
        listdata=listdata_df.to_dict('records'),
    )

    # Save the rendered output to a file in the "output" folder.
    with open(output_root / 'index.html', mode='w') as outfile:
        outfile.write(output)

if __name__ == '__main__':
    main()
