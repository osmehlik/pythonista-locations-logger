# Asks for name of the current location
# and appends it to file in geojson format.


import console
import json
import location
import os


class Locations:
    def __init__(self):
        self.feature_collection = {"type": "FeatureCollection", "features": []}

    def add_any(self, name, longitude, latitude):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            },
            "properties": {
                "name": name
            }
        }
        self.feature_collection["features"].append(feature)

    def add_cur(self, name):
        location.start_updates()
        loc = location.get_location()
        location.stop_updates()
        self.add_any(name, loc["longitude"], loc["latitude"])

    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.feature_collection, f, indent=4)

    def load(self, path):
        with open(path, "r") as f:
            self.feature_collection = json.load(f)


def main():
    db = "locations.geojson"
    locations = Locations()
    if os.path.exists(db):
        locations.load(db)
    try:
        name = console.input_alert(
            "Name this location:", "", "", "Save"
        )
        locations.add_cur(name)
        locations.save(db)
        console.hud_alert("Saved", "success")
    except KeyboardInterrupt:
        console.hud_alert("Cancelled", "error")


if __name__ == "__main__":
    main()
