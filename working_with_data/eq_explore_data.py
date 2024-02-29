from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_day_1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Using for loop
# mags, lons, lats, eq_titles = [], [], [], []
# for eq_dict in all_eq_dicts:
# mag = eq_dict['properties']['mag']
# lon = eq_dict['geometry']['coordinates'][0]
# lat = eq_dict['geometry']['coordinates'][1]
# eq_title = eq_dict['properties']['title']
# mags.append(mag)
# lons.append(lon)
# lats.append(lat)
# eq_titles.append(eq_title)

#  Using list comprehension
mags = [mag['properties']['mag'] for mag in all_eq_dicts]
lons = [lon['geometry']['coordinates'][0] for lon in all_eq_dicts]
lats = [lat['geometry']['coordinates'][1] for lat in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

title = all_eq_data['metadata']['title']
print(title)

print(mags[:10])
print(lons[:5])
print(lats[:5])
