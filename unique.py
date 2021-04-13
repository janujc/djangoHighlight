import os
import sys
import csv

path = os.path.join(sys.path[0], 'clubs.csv')
file = open(path, encoding='utf-8-sig')

reader = csv.DictReader(file)

club_list = list(reader)
club_set = set(club_list)

writer = csv.DictWriter