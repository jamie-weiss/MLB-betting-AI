import betting
import predictor
import csv
import results
import process_gameday_data as pgd
import time
from datetime import date

 
# Wait for 5 seconds
#time.sleep(5)
TODAYS_DATE = date.today()
MOONS = ["NAIAD",
		 "THALASSA",
		 "DESPINA",
		 "GALATEA",
		 "LARISSA",
		 "HIPPOCAMP",
		 "PROTEUS",
		 "TRITON",
		 "NEREID",
		 "HALIMEDE",
		 "SAO",
		 "LAOMEDIA",
		 "PSAMATHE",
		 "NESO"]
CURRENT_VERSION = MOONS[1]
MLB_DATA_FILENAME = "raw_data.csv"
TESTING_PREPROCESSED_FILENAME = "MLB_gameday_data/gd_" + str(TODAYS_DATE) + ".csv"
LINE_DATA_FILENAME = "line_data.csv"
MLB_COLUMN_INDECIES = [5, 6, 7, 12, 13, 14, 15]
LINE_COLUMN_INDECIES = [0, 1, 2, 3, 4, 5, 6]
THRESHOLD = 0.01
WAGER = 10
MAX_LINE = 0.65
DIFF_THRESHOLD = 0.05
ABS_THRESHOLD = 0.01

def main():
	print()
	print()
	time.sleep(2)
	print("Welcome to NEPTUNE BETTING AI - Current Version: {}".format(CURRENT_VERSION))
	print("-Jamie Weiss")
	time.sleep(1)
	print()
	print("For dependencies and more information open README")
	time.sleep(1)
	print()
	print("Current Date: {}".format(TODAYS_DATE))
	time.sleep(1)
	print()
	print("Collecting Training Data......................[1/6]")
	X_training, Y_training = predictor.all_training(MLB_DATA_FILENAME, MLB_COLUMN_INDECIES)
	time.sleep(1)
	print("Getting Today's Gameday Data..................[2/6]")
	X_testing, team_ids = pgd.process_data(TESTING_PREPROCESSED_FILENAME)
	#X_testing, team_ids = pgd.process_data("MLB_gameday_data/gd_2019-03-27.csv")
	time.sleep(1)
	print("Generating Neural Network.....................[3/6]")
	time.sleep(2)
	model = predictor.generate_model()
	print("Training Model................................[4/6]")
	time.sleep(1)
	model = predictor.fit_model(model, X_training, Y_training)
	print("Calculating Probabilities.....................[5/6]")
	time.sleep(1)
	calculated_probs = betting.get_probabilities(model, X_testing)
	print("Generating Bets...............................[6/6]")
	time.sleep(2)
	given_probs = results.get_given_probabilities(X_testing)
	payouts = results.get_payout(X_testing)
	print()
	print()
	bets = results.get_bets(calculated_probs, given_probs, THRESHOLD, MAX_LINE, DIFF_THRESHOLD, ABS_THRESHOLD)
	for i in range(len(bets)):
		bet_num = bets[i]
		if bet_num != -1:
			bet_team_id = team_ids[i][bet_num]
			game_day_id = i + 1
			pay = payouts[i][bet_num] * WAGER
			print("{}:\t{} ML\t{} to win {}".format(game_day_id, bet_team_id, WAGER, round(pay,2)))
	print()
	print()
	print()
	return



if __name__ == "__main__":
	main()




