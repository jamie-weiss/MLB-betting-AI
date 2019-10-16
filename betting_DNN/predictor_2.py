import data_processor_2
import csv
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split


TRAINING_SET_FRACTION = 0.95

def main():
	FILENAME = "raw_data.csv"
	FEATURE_INDECIES = [3, 5, 6, 7, 10, 12, 13, 14, 15]
	X_training, X_testing, Y_training, Y_testing = split_data(FILENAME, FEATURE_INDECIES)
	
	
	column_names = data_processor_2.get_column_names(FILENAME, FEATURE_INDECIES)
	feature_names = column_names[:-1]


	feature_columns = [tf.feature_column.numeric_column(k) for k in feature_names]

	# Generate model and set parameters
	model = tf.estimator.DNNClassifier(
		model_dir='model/',
	    hidden_units=[10],
	    feature_columns=feature_columns,
	    n_classes=2,
	    #label_vocabulary=['H', 'A'],
	    #optimizer=tf.train.ProximalAdagradOptimizer(
	    #learning_rate=0.1,
	    #l1_regularization_strength=0.001
	  )#)
c
	model.train(input_fn=lambda: input_fn(X_training, Y_training))
	

	'''train_input_fn = tf.estimator.inputs.numpy_input_fn(
		x=X_training,
	  	y=Y_training,
	  	batch_size=500,
	  	num_epochs=None,
	  	shuffle=True
	  )

	

	test_input_fn = tf.estimator.inputs.numpy_input_fn(
	    x=X_testing,
	    y=Y_testing,
	    num_epochs=1,
	    shuffle=False
	)

	predictions = model.predict(input_fn=test_input_fn)'''

	

def split_data(filename, column_indecies):
	dataset = data_processor_2.csv_to_array(filename, column_indecies)
	training = []
	testing = []
	X = []
	Y = []
	for row in dataset:
		X.append(row[:-1])
		Y.append([row[-1]])
	test_size = 1 - TRAINING_SET_FRACTION
	X_training, X_testing, Y_training, Y_testing = train_test_split(X, Y,
										test_size=test_size, random_state=42)
	column_names = data_processor_2.get_column_names(filename, column_indecies)

	X_training_dict = {column_names[0]:[],
					   column_names[1]:[],
					   column_names[2]:[],
					   column_names[3]:[],
					   column_names[4]:[],
					   column_names[5]:[],
					   column_names[6]:[],
					   column_names[7]:[]}

	X_testing_dict = {column_names[0]:[],
					   column_names[1]:[],
					   column_names[2]:[],
					   column_names[3]:[],
					   column_names[4]:[],
					   column_names[5]:[],
					   column_names[6]:[],
					   column_names[7]:[]}
	
	
	for row in X_training:
		X_training_dict[column_names[0]].append(row[0])
		X_training_dict[column_names[1]].append(row[1])
		X_training_dict[column_names[2]].append(row[2])
		X_training_dict[column_names[3]].append(row[3])
		X_training_dict[column_names[4]].append(row[4])
		X_training_dict[column_names[5]].append(row[5])
		X_training_dict[column_names[6]].append(row[6])
		X_training_dict[column_names[7]].append(row[7])


	for row in X_testing:
		X_testing_dict[column_names[0]].append(row[0])
		X_testing_dict[column_names[1]].append(row[1])
		X_testing_dict[column_names[2]].append(row[2])
		X_testing_dict[column_names[3]].append(row[3])
		X_testing_dict[column_names[4]].append(row[4])
		X_testing_dict[column_names[5]].append(row[5])
		X_testing_dict[column_names[6]].append(row[6])
		X_testing_dict[column_names[7]].append(row[7])

	# convert arrays to numpy arrays
	for key in X_training_dict:
		X_training_dict[key] = np.array(X_training_dict[key])

	for key in X_testing_dict:
		X_testing_dict[key] = np.array(X_testing_dict[key])

	
	return X_training_dict, X_testing_dict, Y_training, Y_testing

def input_fn(X_training_dict, Y_training):
	return(X_training_dict, Y_training)


if __name__ == "__main__":
	main()