#!/usr/bin/env python3

"""
description: a modified version of original given generatefixtures.py for testing purposes
"""
import os.path as path
import random
import os
import csv
import hashlib


DIR = path.abspath(path.dirname(__file__))
FILES = {
    'clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
    'accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
    'household_cleaners.csv': ('Kitchen Cleaner', 'Bathroom Cleaner',),
}


def write_file(writer, length, categories):
    writer.writerow(['email_hash', 'category'])
    for i in range(0, length):
        writer.writerow([
            hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
            random.choice(categories),
        ])


# small change in the main function
def main():
    'if path does not exist to the test csv files create one'
    if not os.path.exists('./testcsv_fixtures'):
        os.makedirs('testcsv_fixtures')

    for fn, categories in FILES.items():
        with open(path.join(DIR, 'testcsv_fixtures', fn), 'w+', encoding='utf-8') as fh:
            write_file(
                csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
                random.randint(9, 9),
                categories
            )
        'adding an emtpy csv file to the path of testcsv__fixtures i,e. test csv files'
        
    with open(path.join(DIR, 'testcsv_fixtures', 'empty_file.csv'), 'w', encoding='utf-8') as fh:
        pass

if __name__ == '__main__':
    main()
