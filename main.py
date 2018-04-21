import csv
from collections import Counter



pupils = Counter()
k = int(input())
print('Top-', k,  ' stats ', sep = '')
with open('A.csv',  encoding='utf-8') as csvfile:
     spamreader = csv.reader(csvfile)
     spamwriter = csv.writer(csvfile)
     i = 0
     for row in spamreader:
          if len(row[2]) > 0 and '0' <= row[2][0] <= '9':
               pupils[row[3]] += 1
               i += 1
          if i == k:
               break

A = []
for elem in pupils:
     A.append((pupils[elem], elem))
print(sorted(A)[::-1])
