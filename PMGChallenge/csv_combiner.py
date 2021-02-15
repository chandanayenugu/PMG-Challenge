"""
file: csv_combiner.py
coding challenge link: https://github.com/AgencyPMG/ProgrammingChallenges/tree/master/csv-combiner
"""
import sys
import os
import pandas as pd


class CSVCombiner:

    def csvcombine_files(self, argument: list):
        'arguments needs to be valid csv paths'
        'This fucntion merges the csv files'
        chunksize = 10 ** 7
        combined_list = []

        if self.validate_paths(argument):
            list_files = argument[1:]

            for path in list_files:

                # we try to read files as chunks to prevent memory issues
                # using pandas to read the csv files
                for chunk in pd.read_csv(path, chunksize=chunksize):

                    # get the file name from the path
                    file_name = os.path.basename(path)

                    # add the 'filename' column to the chunk
                    #As mentioned we add a new column of file_name to the final output
                    chunk['file_name'] = file_name
                    combined_list.append(chunk)

            # flag to indicate if a header should be added
            header = True

            # we combine all the rows and display the combined csv file
            for chunk in combined_list:
                print(chunk.to_csv(header=header, index=False, line_terminator='\n', chunksize=chunksize), end='')
                header = False
        else:
            return
    
    @staticmethod
    def validate_paths(argument):
       
        'This function ensures that the arguments entered by the users and the file-paths with them are valid.'
        
        'returns boolean value true if all the paths are valid else false'

        if len(argument) <= 1:
            print("Error: No file-paths input.Please enter the valid file paths: \n")
                  
            return False
        
        list_files = argument[1:]

        for path in list_files:
            if not os.path.exists(path):
                print("Error: No such File or directory is found: " + path)
                return False
            if os.stat(path).st_size == 0:
                print("Warning: The following file is empty or null: " + path)
                return False
        return True


# finally we call the functions inside the main method by passing valid csv file paths as inputs
def main():
    combine_csv = CSVCombiner()
    combine_csv.csvcombine_files(sys.argv)

if __name__ == '__main__':
    main()
