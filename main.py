# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import gzip
import io

MIN_YEAR = 1875
MAX_YEAR = 1975

# Map from year -> total number of words
total_counts = {}
# Process total_counts file
with io.open('total_counts.txt', 'rt') as f:
	lines = f.read().split()
	for line in lines:
		parts = line.split(',')
		year = int(parts[0])
		total_count = int(parts[1])
		total_counts[year] = total_count
print(total_counts)

# Clear files
for i in range(1875, 1976):
	open(f'processed_data/{i}.csv', "w").close()

# Process raw_data file
with gzip.open('raw_data.gz','rb') as f:
	counter = 0
	for line_binary in f:
		counter += 1
		line = line_binary.decode('utf-8')
		parts = line.split()
		
		if (parts[0].isdigit()):
			year = int(parts[0]) 
			if MIN_YEAR <= year <= MAX_YEAR:
				x = int(parts[1])
				raw_mention_count = int(parts[2])
				frequency = float(raw_mention_count) / total_counts[x]

				write_file = open(f'processed_data/{parts[0]}.csv', 'a')
				write_file.write(f'{x},{raw_mention_count},{frequency}\n')
		
		if counter % 1000000 == 0:
			print(parts[0])
			