import pandas as pd
import math
import numpy as np
import time
import imp
import pickle

from commons import functions
from training import Preprocess, Training
from tuning import randomforest

#------------------------

def fit(df, config):
	
	target_label = df.columns[len(df.columns)-1]
	if target_label != 'Decision':
		print("Expected: Decision, Existing: ",target_label)
		raise ValueError('Lỗi dữ liệu, hãy chuyển dữ liệu về đúng định dạng!')
	
	#------------------------
	
	#initialize params and folders
	config = functions.initializeParams(config)
	functions.initializeFolders()
	
	algorithm = config['algorithm']

	RandomForest = config['RandomForest']
	num_of_trees = config['num_of_trees']


	#------------------------
	raw_df = df.copy()
	num_of_rows = df.shape[0]; num_of_columns = df.shape[1]
	
	if algorithm == 'Regression':
		if df['Decision'].dtypes == 'object':
			raise ValueError('Lỗi dữ liệu khi chạy kết quả dạng Regression Tree')

	if df['Decision'].dtypes != 'object': 
		algorithm = 'Regression'
		config['algorithm'] = 'Regression'
		global_stdev = df['Decision'].std(ddof=0)

	#-------------------------
	
	print(algorithm,": Đang tiến hành tạo cây quyết định...")
	
	dataset_features = dict() # dictionary

	header = "def findDecision("
	header = header + "obj"
	header = header + "): #"
	
	num_of_columns = df.shape[1]-1
	for i in range(0, num_of_columns):
		column_name = df.columns[i]
		dataset_features[column_name] = df[column_name].dtypes
		header = header + "obj[" + str(i) +"]: "+column_name
		if i != num_of_columns - 1:
			header = header + ", "
	
	header = header + "\n"
		
	#------------------------
	
	begin = time.time()
	
	trees = []; alphas = []

				
	if RandomForest == True:
		trees = randomforest.apply(df, config, header, dataset_features)
	else: 
		root = 1; file = "outputs/rules/rules.py"
		functions.createFile(file, header)
		trees = Training.buildDecisionTree(df,root,file, config, dataset_features)
	
	print("Thuật toán chạy hoàn thành trong:  ",time.time() - begin," giây")
	
	obj = {
		"trees": trees,
		"alphas": alphas,
		"config": config
	}
	return obj
	
	#-----------------------------------------

def predict(model, param):
	
	trees = model["trees"]
	config = model["config"]
	alphas = model["alphas"]
	
	#-----------------------
	
	classification = False
	prediction = 0
	prediction_classes = []
	
	#-----------------------
	
	if len(trees) > 1: #boosting
		index = 0
		for tree in trees:
			
			custom_prediction = tree.findDecision(param)
			
			if custom_prediction != None:
				if type(custom_prediction) != str: #regression
					prediction += custom_prediction
				else:
					classification = True
					prediction_classes.append(custom_prediction)
			
			index = index + 1

	else: #regular decision tree
		tree = trees[0]
		prediction = tree.findDecision(param)
	
	if classification == False:
		return prediction
	else:
		unique_labels = np.unique(prediction_classes)
		prediction_counts = []
		
		for i in range(0, len(unique_labels)):
			count = 0
			for j in prediction_classes:
				if j == unique_labels[i]:
					count = count + 1
			prediction_counts.append(count)
		
		return unique_labels[np.argmax(prediction_counts)]

def save_model(base_model, file_name="model.pkl"):
	
	model = base_model.copy()
	
	#modules cannot be saved. Save its reference instead.
	module_names = []
	for tree in model["trees"]:
		module_names.append(tree.__name__)

	model["trees"] = module_names
	
	f = open("outputs/rules/"+file_name, "wb")
	pickle.dump(model,f)
	f.close()
	
def load_model(file_name="model.pkl"):
	f = open('outputs/rules/'+file_name, 'rb')
	model = pickle.load(f)
	
	#restore modules from its references
	modules = []
	for model_name in model["trees"]:
		module = functions.restoreTree(model_name)
		modules.append(module)
	
	model["trees"] = modules
	
	return model
