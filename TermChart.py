#

import math
import sys

ROWS = 10
data = [3, 18, 9, 24, 32, 19, 7, 10, 16]
minimum = min(data)
maximum = max(data)

chart = []

for row in range(ROWS):
    chart.append([])
    chart[row].append(math.ceil((maximum / ROWS) * row))
    for d in data:
        chart[row].append('   ')

#print(chart)

for r_idx, row in enumerate(chart):
    for c_idx, col in enumerate(data, start=1):
        if col >= row[0]:
            chart[r_idx][c_idx] = ' _ '

chart.reverse()

for row in chart:
    for col in row:
        sys.stdout.write(f'{str(col).rjust(3)} ')
    sys.stdout.write('\n')

for d in data:
    sys.stdout.write(str(d) + ' ')

# print(chart)