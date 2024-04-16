import csv
import matplotlib.pyplot as plt

file = open("E:/DataScience_py/2_final_class/day9_data/weather.csv")
data = csv.reader(file)

header = next(data)

monthly_wind = [0 for x in range(12)]
days_countes = [0 for x in range(12)]

for row in data:
    month = int(row[0][5:7])
    if row[3] != '':
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_countes[month-1] += 1

for i in range(12):
    monthly_wind[i] /= days_countes[i]

plt.plot(monthly_wind, "blue")
plt.show()

file.close()

