import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
import csv
import data_processor_2 as dp
from sklearn.neural_network import MLPClassifier
import predictor

# AWAY = 0, HOME = 1
'''TRAINING_SET_FRACTION = 0.95
FILENAME = "raw_data.csv"
COLUMN_INDECIES = [3, 5, 6, 7, 10, 12, 13, 14, 15]'''


def get_class_predictions(model, X_testing):
	predicitons = model.predict(X_testing)
	return predicitons

def get_score(model, X_testing, Y_testing):
	score = model.score(X_testing, Y_testing)
	return score

def get_probabilities(model, X_testing):
	probabilities = model.predict_proba(X_testing)
	rounded = []
	for row in probabilities:
		rounded.append([round(row[0], 3), round(row[1], 3)])
	return rounded
