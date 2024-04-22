#!/usr/bin/env python3

# python3 delete_gisquick_users.py ~/Downloads/Prezencni_seznam_B232_1551GIS.csv | sh

import argparse
import csv
import json
import bcrypt
from unidecode import unidecode
from datetime import datetime

def main(csv_input):
    users = []
    with open(csv_input) as csvfile:
        userreader = csv.reader(csvfile, delimiter=',')
        for i in range(5):
            next(userreader) # skip initial rows
        for row in userreader:
            users.append(unidecode(row[0].lower()))

    for u in users:
        print(f"docker compose exec app gisquick deleteuser {u}")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create Gisquick users from KOS-generated CSV file')
    parser.add_argument('csv_input')

    args = parser.parse_args()
    main(args.csv_input)
    
