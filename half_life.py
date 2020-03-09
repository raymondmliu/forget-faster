import io
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

open(f'half_life.csv', "w").close()

# Map of year -> half-life of year
data = {}
num = np.log(1/2)/10

for x in range(1875, 1976):
	# Getting data for year x from file (year vs. frequency)
	raw_data = {}
	y = []
	with open(f'processed_data/{x}.csv') as file:
		for line in file:
			year, count, freq = line.split(',')
			if int(year) >= x:
				y.append(float(freq))
	max_index = 0
	_max = 0.0
	for i in range(len(y)):
		if y[i] > _max:
			max_index = i
			_max = y[i]
	y = y[max_index:]
	if len(y)>40:
		y = y[:40]

	popt, pcov = curve_fit(lambda t,a,b: a*np.exp(b*t),
						   list(range(len(y))), y, p0=(_max, num))
	"""
	mid_year = peak_year
	for year in range(x+1, 2009):
		if raw_data[year] * 2 < peak_frequency:
			mid_year = year
			break
	data[x] = (mid_year - peak_year)
	"""
	data[x] = np.log(1/2)/popt[1]
	write_file = open(f'half_life.csv', 'a')
	write_file.write(f'{x},{data[x]}\n')

print(data)

