import predictor
import betting
from sklearn import tree
import graphviz
from sklearn.ensemble import RandomForestClassifier

FILENAME = "line_data.csv"
COLUMN_INDECIES = [0, 1, 2, 3, 4, 5, 6]
RANDOM_STATE = 42
TRAINING_SET_FRACTION = 0.9672

FEATURE_NAMES = ["A_given", "A_calc", "A_diff", "H_given", "H_calc", "H_diff"]
CLASS_NAMES = ["away", "home"]
X_training, X_testing, Y_training, Y_testing = predictor.split_data(FILENAME, COLUMN_INDECIES, RANDOM_STATE, TRAINING_SET_FRACTION)

#clf = tree.DecisionTreeClassifier(min_samples_leaf=5, min_samples_split=10)
clf = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=0)
clf = clf.fit(X_training, Y_training)

'''dot_data = tree.export_graphviz(clf,
								out_file=None, 
								feature_names=FEATURE_NAMES,  
                     			class_names=CLASS_NAMES) 
graph = graphviz.Source(dot_data) 
graph.render("MLB-AI") '''

predictions = clf.predict(X_testing)

correct = 0
total_net = 0.0
for i in range(162):
	if Y_testing[i] == predictions[i]:
		correct = correct + 1
		if predictions[i] == 0:
			line = X_testing[i][0]
		if predictions[i] == 1:
			line = X_testing[i][1]
		total_net = total_net + (100 * line)
	else:
		total_net = total_net - 100

#print(correct)
print(total_net)

#model = predictor.generate_model()
#model = predictor.fit_model(model, X_training, Y_training)
#predictions = betting.get_class_predictions(model, X_testing)
#score = betting.get_score(model, X_testing, Y_testing)
#print(predictions)

for i in range(162):
	print(X_testing[i])
	print(predictions[i], ":", Y_testing[i])
	print()


#print(score)