import json


# Explore the structure of the data 
filename = 'weather/data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

readable_file = 'weather/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent = 4)	

all_eq_dict = all_eq_data['features']

mags = []
for eq_dict in all_eq_dict:
	mag = eq_dict['properties']['mag']
	mags.append(mag)

print(mags[:10])	