import betting
import predictor
import csv
import results

RANDOM_STATE = 5
TRAINING_SET_FRACTION = 0.9672
MLB_DATA_FILENAME = "raw_data.csv"
LINE_DATA_FILENAME = "line_data.csv"
MLB_COLUMN_INDECIES = [5, 6, 7, 12, 13, 14, 15]
LINE_COLUMN_INDECIES = [0, 1, 2, 3, 4, 5, 6]
THRESHOLD = 0.01
WAGER = 10
MAX_LINE = 0.65
DIFF_THRESHOLD = 0.05

def main():
	rs = 1
	#total = 0
	for rs in range(100):
		X_training, X_testing, Y_training, Y_testing = predictor.split_data(MLB_DATA_FILENAME, MLB_COLUMN_INDECIES, rs, TRAINING_SET_FRACTION)
		model = predictor.generate_model()
		model = predictor.fit_model(model, X_training, Y_training)
		calculated_probs = betting.get_probabilities(model, X_testing)
		given_probs = results.get_given_probabilities(X_testing)
		bets = results.get_bets(calculated_probs, given_probs, THRESHOLD, MAX_LINE, DIFF_THRESHOLD)
		payouts = results.get_payout(X_testing)
		net = results.calculate_net_income(bets, payouts, Y_testing, WAGER)
		roi = results.calculate_ROI(bets, net, WAGER)
		print()
		print("---------------------")
		print("Net: ", net)
		print("ROI: ", roi)
		#print(net)
		#total = total + net
	#print("TOTAL: ", total)

	#return



if __name__ == "__main__":
	main()