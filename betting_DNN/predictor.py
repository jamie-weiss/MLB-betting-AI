import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
import csv
import data_processor_2 as dp
from sklearn.neural_network import MLPClassifier


'''TRAINING_SET_FRACTION = 0.95
FILENAME = "raw_data.csv"
COLUMN_INDECIES = [3, 5, 6, 7, 10, 12, 13, 14, 15]'''


# Function: split_data
# Parameters: filename - string name of file to grab data from,
#						 file must have a header row and be of type csv
# Return: X_training - 2D array of features for training
#         X_testing - 2D array pf features for testing
#		  Y_training - 2D array of training labels (int) (each label is wrapped in an array)
#		  Y_testing - 2D array of validation labels (int) (each label is wrapped in an array)
def split_data(filename, column_indecies, random_state, training_set_fraction):
	dataset = dp.csv_to_array(filename, column_indecies)
	X = []
	Y = []
	for row in dataset:
		X.append(row[:-1])
		Y.append(int(row[-1]))
	test_size = 1 - training_set_fraction
	X_training, X_testing, Y_training, Y_testing = train_test_split(X, Y,
										test_size=test_size, random_state=random_state)
	return X_training, X_testing, Y_training, Y_testing


def test_one_game(filename, column_indecies, game_number):
	dataset = dp.csv_to_array(filename, column_indecies)
	X = []
	Y = []
	X_testing = []
	Y_testing = []
	X_training = []
	Y_training = []
	for row in dataset:
		X.append(row[:-1])
		Y.append(int(row[-1]))
	X_testing.append(X[game_number - 1])
	del X[game_number - 1]
	Y_testing.append(Y[game_number - 1])
	del Y[game_number - 1]
	X_training = X
	Y_training = Y
	return X_training, X_testing, Y_training, Y_testing

def all_training(filename, column_indecies):
	X_training = []
	Y_training = []
	dataset = dp.csv_to_array(filename, column_indecies)
	for row in dataset:
		X_training.append(row[:-1])
		Y_training.append(int(row[-1]))
	return X_training, Y_training

# Function: generate_model
# Parameters: none
# Return: model - a MLP neural network classifier with atributes listed below
def generate_model():
	model = MLPClassifier(solver='lbfgs',
						alpha=1e-5,
                   		hidden_layer_sizes=(5, 2),
                   		random_state=1)
	return model


# Function: fit_model
# Parameters: model - a generated MLP classifier model
#			  X_train - 2D list of training features (# of features, # of rows)
#		      Y_train - 1D list of labels (# of rows,)
def fit_model(model, X_train, Y_train):
	model.fit(X_train, Y_train)
	return model

