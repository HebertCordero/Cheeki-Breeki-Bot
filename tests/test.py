import csv
from tabulate import tabulate

b_dataRaw = './assets/bullet_data.csv'

with open(b_dataRaw, encoding="utf8") as f:
    csv_reader = csv.reader(f)
    temp_arr = []
    for line in csv_reader:
      if line[0] == '12 g sh':
        temp_arr.append(line)
    print(tabulate(temp_arr, headers=['Bullet Type','Ammo Type','Damage','Pen Value','Armor Damage','Frag. Chance', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6' ]))