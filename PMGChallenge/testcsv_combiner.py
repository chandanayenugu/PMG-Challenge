"""
file: testcsv_combiner.py
Functionality: a set of unit tests used to test the csv combiner as mentioned using a modified test_generatefixtures.py file
"""
import pandas as pd
import sys
import test_generatefixtures
import unittest
import os
from csv_combiner import CSVCombiner
from io import StringIO


class TestCombineMethod(unittest.TestCase):

    # initialize all paths
    test_output_path = "./test_output.csv"
    csv_combiner_path = "./csv_combiner.py"
    accesories_path = "./testcsv_fixtures/accessories.csv"
    clothing_path = "./testcsv_fixtures/clothing.csv"
    household_cleanerspath = "./testcsv_fixtures/household_cleaners.csv"
    empty_filepath= "./testcsv_fixtures/empty_file.csv"

    # initialize the test output
    backup = sys.stdout
    test_output = open(test_output_path, 'w+')
    combiner = CSVCombiner()

    @classmethod
    def setUpClass(cls):
        # generate the test fixture files located in ./testcsv_fixtures/
        test_generatefixtures.main()

        # redirect the output to ./test_output.csv
        sys.stdout = cls.test_output

    @classmethod
    def tearDownClass(cls):

        cls.test_output.close()

        if os.path.exists(cls.accesories_path):
            os.remove(cls.accesories_path)
        if os.path.exists(cls.clothing_path):
            os.remove(cls.clothing_path)
        if os.path.exists(cls.household_cleanerspath):
            os.remove(cls.household_cleanerspath)
        if os.path.exists(cls.empty_filepath):
            os.remove(cls.empty_filepath)
        if os.path.exists(cls.test_output_path):
            os.remove(cls.test_output_path)
        if os.path.exists("./testcsv_fixtures"):
            os.rmdir("./testcsv_fixtures")

    def setUp(self):
        # setup
        self.output = StringIO()
        sys.stdout = self.output
        self.test_output = open(self.test_output_path, 'w+')

    def tearDown(self):
        self.test_output.close()
        self.test_output = open(self.test_output_path, 'w+')
        sys.stdout = self.backup
        self.test_output.truncate(0)
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

    def test_empty(self):
    
        # run csv_combiner by passing an empty file as argument
        argv = [self.csv_combiner_path, self.empty_filepath]
        self.combiner.csvcombine_files(argv)

        self.assertIn("Warning: The following file is empty or null: ", self.output.getvalue())
    
    def test_no_filearguments(self):

        # run csv_combiner without passing any arguments
        argv = [self.csv_combiner_path]
        self.combiner.csvcombine_files(argv)

        self.assertIn("Error: No file-paths input.", self.output.getvalue())


    def test_non_existent(self):

        # run csv_combiner with a non exisiting file
        argv = [self.csv_combiner_path, "non_existent.csv"]
        self.combiner.csvcombine_files(argv)

        self.assertTrue("Error: No such File or directory is found:" in self.output.getvalue())


    def test_filename_validrows(self):
        # run csv_combiner with valid row args
        argv = [self.csv_combiner_path, self.accesories_path, self.clothing_path]
        self.combiner.csvcombine_files(argv)

        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

        # check if a filename value exists in the produced data-frame
        with open(self.test_output_path) as f:
            df = pd.read_csv(filepath_or_buffer=f, lineterminator='\n')
        self.assertIn('accessories.csv', df['file_name'].tolist())
    
    def test_filename_validcolumns(self):
    
        # run csv_combiner with valid column args
        argv = [self.csv_combiner_path, self.accesories_path, self.clothing_path]
        self.combiner.csvcombine_files(argv)

        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

        # check if the column exists in the data-frame
        with open(self.test_output_path) as f:
            df = pd.read_csv(f)
        self.assertIn('file_name', df.columns.values)

    def test_all_valuescombined(self):

        # run csv_combiner with valid combined args
        argv = [self.csv_combiner_path, self.accesories_path, self.clothing_path,
                self.household_cleanerspath]
        self.combiner.csvcombine_files(argv)

        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

        # open all test csv data frames using pandas read_csv function

        accesories_df = pd.read_csv(filepath_or_buffer=self.accesories_path, lineterminator='\n')
        clothing_df = pd.read_csv(filepath_or_buffer=self.clothing_path, lineterminator='\n')
        household_cleaners_df = pd.read_csv(filepath_or_buffer=self.household_cleanerspath, lineterminator='\n')

        # check that data from the given fictures is present in the resulting combined csv file

        with open(self.test_output_path) as f:
            combined_df = pd.read_csv(filepath_or_buffer=f, lineterminator='\n')
        self.assertEqual(len(combined_df.merge(accesories_df)), len(combined_df.drop_duplicates()))
        self.assertEqual(len(combined_df.merge(clothing_df)), len(combined_df.drop_duplicates()))
        self.assertEqual(len(combined_df.merge(household_cleaners_df)), len(combined_df.drop_duplicates()))

