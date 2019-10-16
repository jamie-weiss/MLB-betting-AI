import driver
import results
import betting
import predictor


RANDOM_STATE = 69
TRAINING_SET_FRACTION = 0.9672
FILENAME = "raw_data.csv"
COLUMN_INDECIES = [5, 6, 7, 12, 13, 14, 15]
THRESHOLD = 0.01
WAGER = 100
MAX_LINE = 0.65
DIFF_THRESHOLD = 0.05

game_num = 1
for game_num in range(4929):
	X_training, X_testing, Y_training, Y_testing = predictor.test_one_game(FILENAME, COLUMN_INDECIES, game_num)
	model = predictor.generate_model()
	model = predictor.fit_model(model, X_training, Y_training)
	calculated_probs = betting.get_probabilities(model, X_testing)
	given_probs = results.get_given_probabilities(X_testing)
	bets = results.get_bets(calculated_probs, given_probs, Y_testing, THRESHOLD, MAX_LINE, DIFF_THRESHOLD)

