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
    # Download the map data.
    ...

    # Download the chart data.
    ...

    # Download the population density list data.
    ...

    # Render the data into the template.
    env = Environment(loader=FileSystemLoader(template_root))
    template = env.get_template('index.html')
    output = template.render(
        # TEMPLATE DATA GOES HERE...
    )

    # Save the rendered output to a file in the "output" folder.
    with open(output_root / 'index.html', mode='w') as outfile:
        outfile.write(output)

if __name__ == '__main__':
    main()
