import numpy as np
import pathlib
import imp

def restoreTree(moduleName):
   fp, pathname, description = imp.find_module(moduleName)
   return imp.load_module(moduleName, fp, pathname, description)

def softmax(w):
	e = np.exp(np.array(w, dtype=np.float32))
	dist = e / np.sum(e)
	return dist

def sign(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

def formatRule(root):
	resp = ''
	for i in range(0, root):
		resp = resp + '   '
	return resp	

def storeRule(file,content):
	f = open(file, "a+")
	f.writelines(content)
	f.writelines("\n")

def createFile(file,content):
	f = open(file, "w")
	f.write(content)

def initializeFolders():
	import sys
	sys.path.append("..")
	pathlib.Path("outputs").mkdir(parents=True, exist_ok=True)
	pathlib.Path("outputs/data").mkdir(parents=True, exist_ok=True)
	pathlib.Path("outputs/rules").mkdir(parents=True, exist_ok=True)

def initializeParams(config):
	algorithm = 'ID3'
	RandomForest = False; num_of_trees = 5; enableMultitasking = False
	for key, value in config.items():
		if key == 'algorithm':
			algorithm = value
		#---------------------------------	
		elif key == 'RandomForest':
			RandomForest = value
		elif key == 'num_of_trees':
			num_of_trees = value
		

	config['algorithm'] = algorithm
	config['RandomForest'] = RandomForest
	config['num_of_trees'] = num_of_trees
	
	return config
