import matplotlib.pyplot as plt
import numpy as np

MIN_YEAR = 1875
MAX_YEAR = 1975

years = list(range(MIN_YEAR, MAX_YEAR+1))
half_lives = []

frequencies = []
# range(MIN_YEAR, MAX_YEAR+1)

for year in [1881, 1925, 1975]:
    with open(f"processed_data/{year}.csv") as f:
        cur_freq = []
        for line in f:
            cur_year, count, freq = line.split(',')
            if MIN_YEAR <= int(cur_year) <= MAX_YEAR:
                cur_freq.append(float(freq))
        frequencies.append(cur_freq)

with open("half_life.csv") as f:
    for line in f:
        year, half_life = line.split(',')
        half_lives.append(float(half_life))

plt.figure(1)
plt.plot(years, frequencies[0], years, frequencies[1], years, frequencies[2])
plt.xlabel("year")
plt.ylabel("raw count")
plt.title("Raw Count Over Year")
plt.figure(2)
plt.plot(years,half_lives)
plt.xlabel("year")
plt.ylabel("half life")
plt.title("Half Life Over Year")
plt.show()
