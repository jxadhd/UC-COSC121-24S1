"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""

from os.path import isfile as is_valid_file

def main():
    """Prompt the user to provide a csv file of rainfall data, process the 
       given file's data, and print the monthly rainfall totals. 
       The file is assumed to have the month number in column 1, the number 
       of days in the month in column 2, and the floating point rainfalls 
       (in mm) for that month in the remaining columns of the row.
    """
    filename = input('Input csv file name? ')
    while not is_valid_file(filename):
        print('File does not exist.')
        filename = input('Input csv file name? ') 
    datafile = open(filename) 
    data = datafile.read().splitlines()
    datafile.close()
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns = line.split(',')
        month = int(columns[0])
        num_days = int(columns[1])
        total_rainfall = 0
        for col in columns[2:2 + num_days]:
            total_rainfall += float(col)
        results.append((month, total_rainfall))

    print('Monthly rainfalls')
    for (month, total_rainfall) in results:
        print(f'Month {month:2}: {total_rainfall:.1f}')


main()
