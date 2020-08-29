import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/Toronto_2019.csv'
with open(filename) as f:
	reader = csv.reader(f)
	# return the next line in the file (the first line of the file)
	header_row = next(reader)
	
#for index, column_header in enumerate(header_row):
	#print(index, column_header)

# Get dates and high temperature from this file
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:

			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			high = int(row[4])
			low = int(row[5])
			dates.append(current_date)
			highs.append(high)
			lows.append(low)


# Plot the high temperature
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates,lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'yellow', alpha = 0.1)

# Format plot
plt.title('Daily high and low temperature \n Toronto - 2019', fontsize = 20)
plt.xlabel ('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize =16)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.show()	
