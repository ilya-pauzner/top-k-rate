#!/usr/bin/python
import csv
import argparse
import logging
from collections import Counter

def parse_args():
     parser = argparse.ArgumentParser(description='Groups in rating top-k')
     parser.add_argument('k', metavar='k', type=int, nargs='+',
                         help='how many students we want to parse')     
     parser.add_argument('filename', metavar='filename', type=str, nargs='+',
                         help='csv filename')     
     return parser.parse_args()

if __name__ == '__main__':
     pupils = Counter()
     args = parse_args()
     k = args.k[0]
     filename = args.filename[0]
     try:
          with open(filename,  encoding='utf-8') as csvfile:
               print('Top-', k,  ' stats ', sep = '')
               spamreader = csv.reader(csvfile)
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
     except FileNotFoundError:
          logging.error('Csv file with rating not found')
