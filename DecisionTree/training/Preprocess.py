import numpy as np

import math

from training import Training

def processContinuousFeatures(algorithm, df, column_name, entropy, config):
	unique_values = sorted(df[column_name].unique())
	#print(column_name,"->",unique_values)
	
	subset_gainratios = []; subset_gains = []; subset_ginis = []; subset_red_stdevs = []
	
	for i in range(0, len(unique_values)-1):
		threshold = unique_values[i]
		
		subset1 = df[df[column_name] <= threshold]
		subset2 = df[df[column_name] > threshold]
		
		subset1_rows = subset1.shape[0]; subset2_rows = subset2.shape[0]
		total_instances = df.shape[0] #subset1_rows+subset2_rows
		
		subset1_probability = subset1_rows / total_instances
		subset2_probability = subset2_rows / total_instances
		
		if algorithm == 'ID3' or algorithm == 'C4.5':
			threshold_gain = entropy - subset1_probability*Training.calculateEntropy(subset1, config) - subset2_probability*Training.calculateEntropy(subset2, config)
			subset_gains.append(threshold_gain)
		
		if algorithm == 'C4.5':
			threshold_splitinfo = -subset1_probability * math.log(subset1_probability, 2)-subset2_probability*math.log(subset2_probability, 2)
			gainratio = threshold_gain / threshold_splitinfo
			subset_gainratios.append(gainratio)
				
		elif algorithm == 'CART':
			decision_for_subset1 = subset1['Decision'].value_counts().tolist()
			decision_for_subset2 = subset2['Decision'].value_counts().tolist()
			
			gini_subset1 = 1; gini_subset2 = 1
			
			for j in range(0, len(decision_for_subset1)):
				gini_subset1 = gini_subset1 - math.pow((decision_for_subset1[j]/subset1_rows),2)
			
			for j in range(0, len(decision_for_subset2)):
				gini_subset2 = gini_subset2 - math.pow((decision_for_subset2[j]/subset2_rows),2)
			
			gini = (subset1_rows/total_instances)*gini_subset1 + (subset2_rows/total_instances) * gini_subset2
			
			subset_ginis.append(gini)
		
		#----------------------------------
		elif algorithm == 'Regression':
			superset_stdev = df['Decision'].std(ddof=0)
			subset1_stdev = subset1['Decision'].std(ddof=0)
			subset2_stdev = subset2['Decision'].std(ddof=0)
			
			threshold_weighted_stdev = (subset1_rows/total_instances)*subset1_stdev + (subset2_rows/total_instances)*subset2_stdev
			threshold_reducted_stdev = superset_stdev - threshold_weighted_stdev
			subset_red_stdevs.append(threshold_reducted_stdev)
			
		#----------------------------------
	
	if algorithm == "C4.5":
		winner_one = subset_gainratios.index(max(subset_gainratios))
	elif algorithm == "ID3":
		winner_one = subset_gains.index(max(subset_gains))
	elif algorithm == "CART":
		winner_one = subset_ginis.index(min(subset_ginis))
	elif algorithm == "Regression":
		winner_one = subset_red_stdevs.index(max(subset_red_stdevs))
		
	winner_threshold = unique_values[winner_one]
	
	#print("theshold is ",winner_threshold," for ",column_name)
	df[column_name] = np.where(df[column_name] <= winner_threshold, "<="+str(winner_threshold), ">"+str(winner_threshold))
	
	return df