import data_processor_2 as dp

def process_data(filename):
	preprocessed = dp.string_conversion(filename, [0, 1, 2, 3, 4, 5, 6, 7])
	processed = []
	teams = []
	for row in preprocessed:
		processed_row = []
		team_ids = []
		H_ml_open = row[1]
		H_ml_close = row[2]
		H_streak = row[3]
		A_ml_open = row[5]
		A_ml_close = row[6]
		A_streak = row[7]
		if H_ml_open < 0:
			H_prob_open = -H_ml_open / (-H_ml_open + 100)
		if H_ml_open > 0:
			H_prob_open = 100 / (H_ml_open + 100)
		if H_ml_close < 0:
			H_prob_close = -H_ml_close / (-H_ml_close + 100)
		if H_ml_close > 0:
			H_prob_close = 100 / (H_ml_close + 100)
		if A_ml_open < 0:
			A_prob_open = -A_ml_open / (-A_ml_open + 100)
		if A_ml_open > 0:
			A_prob_open = 100 / (A_ml_open + 100)
		if A_ml_close < 0:
			A_prob_close = -A_ml_close / (-A_ml_close + 100)
		if A_ml_close > 0:
			A_prob_close = 100 / (A_ml_close + 100)
		H_diff = H_prob_close - H_prob_open
		A_diff = A_prob_close - A_prob_open
		processed_row = [round(H_prob_close,3), round(H_diff,3), round(H_streak,3), round(A_prob_close,3), round(A_diff,3), round(A_streak,3)]
		processed.append(processed_row)
		team_ids = [row[4], row[0]]
		teams.append(team_ids)
	return processed, teams






