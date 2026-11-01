# pythonista-locations-collector

A script for Pythonista iOS app
to collect named GPS locations
in GeoJSON file.

## Installation

Create locations.py file in Pythonista
and use iOS copy & paste functionality
to save content of locations.py file
in this repository into it.

## Usage

Every time you are in place whose
GPS location you want to save,
run locations.py script in Pythonista.
It asks you for name of the current
location and then saves it into
locations.geojson file. The next time
you run the script to save another
location, new location is added
to locations already present in that
file.

After you are happy with saved
locations, you manually copy
locations.geojson file to where
you want to use it. Maybe
you can manually convert it
to gpx file format and then
try to load it into your favorite
application.