# data_processory.py
# Purpose: Parse data from csv to use for ML
# Notes: CSV file must have header row, and contain only float type metrics

import csv
import numpy as np

'''
def main():
	FEATURE_INDECIES = [3, 5, 6, 7, 10, 12, 13, 14, 15]
	FILENAME = "raw_data.csv"
	column_names = get_column_names(FILENAME, FEATURE_INDECIES)
	print(column_names)
	dataset = csv_to_array(FILENAME, FEATURE_INDECIES)
	print(dataset)
'''


# Function:	get_column_names
# Parameters: filename - string name of csv file to be parsed
#			  column_indecies - array of indecies we want to parse
# Returns: column_names - 1D array of strings holding the names of columns we parsed
def get_column_names(filename, column_indecies):
	data_f = open(filename)
	data_csv = csv.reader(data_f)
	column_names = []
	for row in data_csv:
		for i in column_indecies:
			column_names.append(row[i])
		break
	return column_names



# Function:	csv_to_array
# Parameters: filename - string name of csv file to be parsed
#			  column_indecies - array of indecies we want to parse
# Returns: dataset - 2D array of floats holding the data from columns we parsed
def csv_to_array(filename, column_indecies):
	data_f = open(filename)
	data_csv = csv.reader(data_f)
	dataset = []
	float_row = []
	next(data_csv)
	for row in data_csv:
		formatted_row = []
		for i in column_indecies:
			formatted_row.append(row[i])
		float_row = list(map(float, formatted_row))	
		dataset.append(float_row)
	return dataset

def string_conversion(filename, column_indecies):
	data_f = open(filename)
	data_csv = csv.reader(data_f)
	dataset = []
	float_row = []
	next(data_csv)
	for row in data_csv:
		formatted_row = []
		for i in column_indecies:
			formatted_row.append(row[i])
		formatted_row[1] = float(formatted_row[1])
		formatted_row[2] = float(formatted_row[2])
		formatted_row[3] = float(formatted_row[3])
		formatted_row[5] = float(formatted_row[5])
		formatted_row[6] = float(formatted_row[6])
		formatted_row[7] = float(formatted_row[7])
		dataset.append(formatted_row)
	return dataset


'''
if __name__ == "__main__":
	main()
'''

