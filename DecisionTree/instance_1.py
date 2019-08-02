import DecisionTree as tree 
import pandas as pd 

df = pd.read_csv('dataset/data_training.txt')

config = {'algorimthm': 'ID3'}

model = tree.fit(df, config)
tree.save_model(model, "model.pkl")

