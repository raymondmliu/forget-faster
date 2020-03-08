import io
import csv
import matplotlib.pyplot as plt
import numpy

open(f'half_life.csv', "w").close()

data = {}

for x in range(1875, 1976):
	# Getting data for year x from file (year vs. frequency)
	raw_data = {}
	with open(f'processed_data/{x}.csv', newline='') as csvfile:
		lines = csv.reader(csvfile, delimiter=',')
		for line in lines:
			raw_data[int(line[0])] = float(line[2])
	
	peak_year = 0
	peak_frequency = 0.0
	for (year, frequency) in raw_data.items():
		if frequency > peak_frequency:
			peak_year = year
			peak_frequency = frequency

	mid_year = peak_year
	for (year, frequency) in raw_data.items():
		if year > mid_year and frequency * 2 < peak_frequency:
			mid_year = year
			break

	data[x] = (mid_year - peak_year)

plt.plot(list(data.keys()), list(data.values()))
plt.show()

print(data)
	
	