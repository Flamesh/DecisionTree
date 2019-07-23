import math
import imp

from training import Preprocess
from commons import functions

def calculateEntropy(df, config):
	
	algorithm = config['algorithm']
	
	#--------------------------
	
	if algorithm == 'Regression':
		return 0
	
	#print(df)

	instances = df.shape[0]; columns = df.shape[1]
	#print(instances," rows, ",columns," columns")

	decisions = df['Decision'].value_counts().keys().tolist()

	entropy = 0

	for i in range(0, len(decisions)):
		decision = decisions[i]
		num_of_decisions = df['Decision'].value_counts().tolist()[i]
		#print(decision,"->",num_of_decisions)
		
		class_probability = num_of_decisions/instances
		
		entropy = entropy - class_probability*math.log(class_probability, 2)
		
	return entropy

def findDecision(df, config):
	
	algorithm = config['algorithm']
	
	#-----------------------------
	
	if algorithm == 'Regression':
		stdev = df['Decision'].std(ddof=0)
		
	
	entropy = 0
	
	if algorithm == "ID3" or algorithm == "C4.5":
		entropy = calculateEntropy(df, config)
	#print("entropy: ",entropy)

	columns = df.shape[1]; instances = df.shape[0]

	gains = []; gainratios = []; ginis = []; reducted_stdevs = []

	for i in range(0, columns-1):
		column_name = df.columns[i]
		column_type = df[column_name].dtypes
		
		#print(column_name,"->",column_type)
		
		if column_type != 'object':
			df = Preprocess.processContinuousFeatures(algorithm, df, column_name, entropy, config)
		
		classes = df[column_name].value_counts()
		
		gain = entropy * 1; splitinfo = 0; gini = 0; weighted_stdev = 0
		
		for j in range(0, len(classes)):
			current_class = classes.keys().tolist()[j]
			#print(column_name,"->",current_class)
			
			subdataset = df[df[column_name] == current_class]
			#print(subdataset)
			
			subset_instances = subdataset.shape[0]
			class_probability = subset_instances/instances
			
			if algorithm == 'ID3' or algorithm == 'C4.5':
				subset_entropy = calculateEntropy(subdataset, config)
				#print("entropy for this sub dataset: ", subset_entropy)
				gain = gain - class_probability * subset_entropy			
			
			if algorithm == 'C4.5':
				splitinfo = splitinfo - class_probability*math.log(class_probability, 2)
			
			elif algorithm == 'CART': #GINI index
				decision_list = subdataset['Decision'].value_counts().tolist()
				
				subgini = 1
				
				for k in range(0, len(decision_list)):
					subgini = subgini - math.pow((decision_list[k]/subset_instances), 2)
				
				gini = gini + (subset_instances / instances) * subgini
			
			elif algorithm == 'Regression':
				subset_stdev = subdataset['Decision'].std(ddof=0)
				weighted_stdev = weighted_stdev + (subset_instances/instances)*subset_stdev
		
		#-------------------------------
		
		if algorithm == "ID3":
			gains.append(gain)
		
		elif algorithm == "C4.5":
		
			if splitinfo == 0:
				splitinfo = 100

			gainratio = gain / splitinfo
			gainratios.append(gainratio)
		
		elif algorithm == "CART":
			ginis.append(gini)
		
		elif algorithm == 'Regression':
			reducted_stdev = stdev - weighted_stdev
			reducted_stdevs.append(reducted_stdev)
	
	#print(df)
	if algorithm == "ID3":
		winner_index = gains.index(max(gains))
	elif algorithm == "C4.5":
		winner_index = gainratios.index(max(gainratios))
	elif algorithm == "CART":
		winner_index = ginis.index(min(ginis))
	elif algorithm == "Regression":
		winner_index = reducted_stdevs.index(max(reducted_stdevs))
	winner_name = df.columns[winner_index]

	return winner_name

def buildDecisionTree(df,root,file, config, dataset_features):

	models = []

	if root == 1:
		if config['RandomForest'] != True:
			raw_df = df.copy()
	
	algorithm = config['algorithm']
	
	#--------------------------------------
	
	#print(df.shape)
	charForResp = "'"
	if algorithm == 'Regression':
		charForResp = ""

	tmp_root = root * 1
	
	df_copy = df.copy()
	
	winner_name = findDecision(df, config)
	
	j = 0 
	for i in dataset_features:
		if i == winner_name:
			winner_index = j
		j = j + 1
	
	numericColumn = False
	if dataset_features[winner_name] != 'object':
		numericColumn = True
	
	#restoration
	columns = df.shape[1]
	for i in range(0, columns-1):
		column_name = df.columns[i]; column_type = df[column_name].dtypes
		if column_type != 'object' and column_name != winner_name:
			df[column_name] = df_copy[column_name]
	
	classes = df[winner_name].value_counts().keys().tolist()

	for i in range(0,len(classes)):
		current_class = classes[i]
		subdataset = df[df[winner_name] == current_class]
		subdataset = subdataset.drop(columns=[winner_name])
		
		if numericColumn == True:
			compareTo = current_class 
		else:
			compareTo = " == '"+str(current_class)+"'"
		
		#print(subdataset)
		
		terminateBuilding = False
		
		#-----------------------------------------------
		if len(subdataset['Decision'].value_counts().tolist()) == 1:
			final_decision = subdataset['Decision'].value_counts().keys().tolist()[0] 
			terminateBuilding = True
		elif subdataset.shape[1] == 1: 
			final_decision = subdataset['Decision'].value_counts().idxmax() 
			terminateBuilding = True
		elif algorithm == 'Regression' and subdataset.shape[0] < 5: 

			final_decision = subdataset['Decision'].mean() 
			terminateBuilding = True
		#-----------------------------------------------
		
		if i == 0:
			check_condition = "if"
		else:
			check_condition = "elif"
		
		functions.storeRule(file,(functions.formatRule(root),"",check_condition," obj[",str(winner_index),"]",compareTo,":"))
		
		#-----------------------------------------------
		
		if terminateBuilding == True: 
			functions.storeRule(file,(functions.formatRule(root+1),"return ",charForResp+str(final_decision)+charForResp))
			
		else:
			root = root + 1
			buildDecisionTree(subdataset, root, file, config, dataset_features)
		
		root = tmp_root * 1
	
	#---------------------------------------------
	
	#calculate accuracy metrics
	if root == 1:
		if config['RandomForest'] != True:
			moduleName = "outputs/rules/rules"
			fp, pathname, description = imp.find_module(moduleName)
			myrules = imp.load_module(moduleName, fp, pathname, description) 
			models.append(myrules)
			
			num_of_features = df.shape[1] - 1
			instances = df.shape[0]
			classified = 0; mae = 0; mse = 0

			raw_df['Prediction'] = raw_df.apply(findPrediction, axis=1)
			#print(raw_df['Prediction'])
			total_rows = len(raw_df)
			num_of_predict_yes = 0
			num_of_predict_no = 0
			instance_is_yes = 0
			instance_is_no = 0

			for i in raw_df['Prediction']:
				if i == "No":
					num_of_predict_no = num_of_predict_no + 1
				num_of_predict_yes = total_rows - num_of_predict_no
			for i in raw_df['Decision']:
				if i == 'No':
					instance_is_no = instance_is_no + 1
				instance_is_yes = total_rows - instance_is_no
			#print(num_of_predict_no, num_of_predict_yes, instance_is_no, instance_is_yes)
			#exit()
			if algorithm != 'Regression':
				
				True_positive = 0
				True_negative = 0
				False_positive = 0
				False_negative = 0
				for i in range(instances):
					if (raw_df['Prediction'][i] == raw_df['Decision'][i] and raw_df['Prediction'][i] == 'Yes'):
						True_positive = True_positive + 1
					
					if((raw_df['Prediction'][i] != raw_df['Decision'][i] and raw_df['Prediction'][i] == 'No')):
						False_negative = False_negative + 1
					
					if((raw_df['Prediction'][i] != raw_df['Decision'][i] and raw_df['Prediction'][i] == 'Yes')):
						False_positive = False_positive + 1

			

				idx = raw_df[raw_df['Prediction'] == raw_df['Decision']].index

				accuracy = 100*len(idx)/instances
				precision = 100*True_positive/(True_positive + False_positive)
				recall = 100*True_positive/(True_positive + False_negative)

				F1_score = 2*(precision*recall)/(precision+recall)
				print("accuracy: ", accuracy,"% trên tổng số ",instances,"phép thử")
				print("precision: ", precision, "% ")
				print("recall: ", recall, "% ")
				print("F1 score: ", F1_score)

			
			else:
				raw_df['Absolute_Error'] = abs(raw_df['Prediction'] - raw_df['Decision'])
				raw_df['Absolute_Error_Squared'] = raw_df['Absolute_Error'] * raw_df['Absolute_Error']
				
				#print(raw_df)
				
				mae = raw_df['Absolute_Error'].sum()/instances
				print("MAE: ",mae)
				
				mse = raw_df['Absolute_Error_Squared'].sum()/instances
				rmse = math.sqrt(mse)
				print("RMSE: ",rmse)
				
				mean = raw_df['Decision'].mean()
				print("Mean: ", mean)
				
				if mean > 0:
					print("MAE / Mean: ",100*mae/mean,"%")
					print("RMSE / Mean: ",100*rmse/mean,"%")
	
	return models
			
def findPrediction(row):
	params = []
	num_of_features = row.shape[0] - 1
	for j in range(0, num_of_features):
		params.append(row[j])
	
	moduleName = "outputs/rules/rules"
	fp, pathname, description = imp.find_module(moduleName)
	myrules = imp.load_module(moduleName, fp, pathname, description) #rules0
	#print(myrules)

	prediction = myrules.findDecision(params)
	return prediction
	
