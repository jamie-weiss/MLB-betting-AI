import betting
import predictor
import csv
import data_processor_2

'''RANDOM_STATE = 42
TRAINING_SET_FRACTION = 0.98
FILENAME = "raw_data.csv"
COLUMN_INDECIES = [5, 6, 7, 12, 13, 14, 15]
THRESHOLD = 0.01
WAGER = 100'''


#HOME_PROB_OPEN = 0
HOME_PROB_CLOSE = 0
HOME_DIFF = 1
HOME_STREAK = 2
#AWAY_PROB_OPEN = 3
AWAY_PROB_CLOSE = 3
AWAY_DIFF = 4
AWAY_STREAK = 5
WIN = 6

# return (2, N # of rows) array of (Home payout, Away payout) * N rows
def get_payout(X_testing):
	converted_lines = []
	for row in X_testing:
		home_prob = row[HOME_PROB_CLOSE]
		away_prob = row[AWAY_PROB_CLOSE]
		home_dec = 1 / home_prob
		away_dec = 1 / away_prob
		home_payout = home_dec - 1
		away_payout = away_dec - 1
		payouts = [round(away_payout, 2), round(home_payout, 2)]
		converted_lines.append(payouts)
	return converted_lines


# return just H_prob and A_prob from X_testing in 2D array [[A_prob, H_prob]]
def get_given_probabilities(X_testing):
	given_probs = []
	for row in X_testing:
		given_probs.append([row[AWAY_PROB_CLOSE], row[HOME_PROB_CLOSE]])
	return given_probs


# UNCOMMENT FOR BET ANALYSIS
def get_bets(calculated_probs, given_probs, threshold, max_line, diff_threshold, abs_threshold):
	bets = [] # 0 = away bet, 1 = home bet, -1 = no bet
	testing = []
	for i in range(len(calculated_probs)):
		A_given = given_probs[i][0]
		H_given = given_probs[i][1]
		A_calc = calculated_probs[i][0]
		H_calc = calculated_probs[i][1]
		

		if A_given > max_line:
			bet = -1
		elif H_given > max_line:
			bet = -1
		elif A_calc - A_given > threshold:
			bet = 0
		elif H_calc - H_given > threshold:
			bet = 1
		elif A_calc - A_given > (H_calc - H_given) + diff_threshold:
			bet = 0
		elif H_calc - H_given > (A_calc - A_given) + diff_threshold:
			bet = 1
		elif abs(H_calc - H_given) + abs_threshold < abs(A_calc - A_given):
			bet = 1
		elif abs(A_calc - A_given) + abs_threshold < abs(H_calc - H_given):
			bet = 0
		else:
			bet = -1



		'''print("Away line: ", A_given)
		print("Away calc: ", A_calc)
		print("A diff:", round((A_calc - A_given), 3))
		print("Home line: ", H_given)
		print("Home calc: ", H_calc)
		print("H diff:", round((H_calc - H_given), 3))
		print("RESULT: ", Y_testing[i])
		print("Bet: ", bet)
		print()'''
		#print('{}, {}, {}, {}, {}, {}, {}'.format(A_given, A_calc, round((A_calc - A_given), 3), H_given, H_calc, round((H_calc - H_given), 3), Y_testing[i]))
		#testing_row = [A_given, A_calc, round((A_calc - A_given), 3), H_given, H_calc, round((H_calc - H_given), 3), Y_testing[i]]
		#testing.append(testing_row)
		bets.append(bet)
		
	return bets



def calculate_net_income(bets, payouts, Y_testing, wager):
	net = 0
	for i in range(len(Y_testing)):
		payout = payouts[i]
		bet = bets[i]
		result = Y_testing[i]
		if bet != -1:
			if bet == result:
				net = net + (wager * payout[bet])
			else:
				net = net - wager
	return net


def calculate_ROI(bets, net_income, wager):
	tickets = 0
	for bet in bets:
		if bet != -1:
			tickets = tickets + 1
	total_wager = tickets * wager
	roi = round((net_income / total_wager) * 100, 3)
	return roi


