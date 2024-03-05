import datetime
import getpass
import logging
from pathlib import Path

import pandas as pd
from arcgis.features import FeatureLayer
from arcgis.gis import GIS

agol_url = "https://www.arcgis.com/"
username = input("AGOL username: ")
password = getpass.getpass()
gis = GIS(agol_url, username, password)


def main() -> None:
    logging.basicConfig(
        format="{levelname}:{asctime}:{message}", level=logging.INFO, style="{"
    )
    layer = create_feature_layer()
    update_dates(layer)


def create_feature_layer() -> FeatureLayer:
    """Create a new AGOL hosted feature layer from `layer_source.csv`."""
    csv = str(Path("layer_source.csv").resolve())
    csv_item = gis.content.add(item_properties={"title": "Date Example CSV"}, data=csv)
    logging.info(f"Created CSV item {csv_item.id!r}")
    example_date_item = csv_item.publish()
    logging.info(f"Created Date Example Feature Layer {example_date_item.id!r}")
    example_date_item.update(item_properties={"title": "Date Example"})
    return example_date_item.layers[0]


def update_dates(layer: FeatureLayer) -> None:
    logging.info(f"Initial state: {layer.query(object_ids='1').features[0].attributes}")
    updates = pd.DataFrame(
        [
            {
                "OBJECTID": 1,
                "date_field": datetime.datetime(1999, 6, 15, 1),
                "date_field_2": datetime.datetime(2005, 12, 1, 8),
                "SHAPE": {
                    "x": -7000000,
                    "y": 5000000,
                    "spatialReference": {"wkid": 102100, "latestWkid": 3857},
                },
            }
        ]
    )
    edit_results = layer.edit_features(updates=updates)
    logging.info(f"Edit results: {edit_results}")
    logging.info(f"Final state: {layer.query(object_ids='1').features[0].attributes}")


main()
