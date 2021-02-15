# PMG Programming Challenge

Given a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. The script outputs a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). The script uses 'filename' as the header for the additional column.


## Example Output

Given two input files named `clothing.csv` and `accessories.csv`.

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

The script would output

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|


## Language Used

- Python, used Pandas library to read and write CSV files by creating a virtual environment using Anaconda

## To run the main csv_combiner.py file run the following command on terminal 

Through command line:
```
$ python ./csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

## to perform unit tests on the csv_combiner.py file run the testcsv_combiner.py using the following command

Through command line: 
```
$ python -m unittest testcsv_combiner.py
```

