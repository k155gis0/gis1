#!/usr/bin/env python3

# python3 create_gisquick_users_from_kos.py ~/Downloads/Prezencni_seznam_B232_1551GIS.csv users.json
# docker compose exec app gisquick loadusers users.json

import argparse
import csv
import json
import bcrypt
from unidecode import unidecode
from datetime import datetime

teachers = [
    ('Landa', 'Martin', 'landamar'),
    ('Mužík', 'František', 'muzikfra')
]

salt = bcrypt.gensalt()

def gen_user(firstname, lastname, username):
    return {
        "username": unidecode(lastname.lower()),
        "email": f"{username.lower()}@cvut.cz",
        "password": bcrypt.hashpw(unidecode(firstname.lower()).encode(), salt).decode(),
        "first_name": firstname,
        "last_name": lastname,
        "is_active": True,
        "is_superuser": False,
        "created_at": f"{datetime.now().isoformat()}Z",
        "confirmed_at": None,
        "last_login_at": None,
    }

def main(csv_input, json_output):
    users = []
    with open(csv_input) as csvfile:
        userreader = csv.reader(csvfile, delimiter=',')
        for i in range(5):
            next(userreader) # skip initial rows
        for row in userreader:
            users.append(gen_user(row[1], row[0], row[3]))

    for ln, fn, un in teachers:
        users.append(gen_user(fn, ln, un))
                         
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=4)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create Gisquick users from KOS-generated CSV file')
    parser.add_argument('csv_input')
    parser.add_argument('json_output')

    args = parser.parse_args()
    main(args.csv_input, args.json_output)
    
