import DecisionTree as tree 
import pandas as pd
from commons import functions
import imp 
from training import Training


moduleName = "outputs/rules/rule_0"
tree = functions.restoreTree(moduleName)

df_test = pd.read_csv('dataset/data_testing.txt')

raw_df = df_test.copy()
raw_df['Prediction'] = raw_df.apply(Training.findPrediction, axis=1)

len_of_data = raw_df.shape[0]

idx = raw_df[raw_df['Prediction'] == raw_df['Decision']].index

True_positive = 0
True_negative = 0
False_positive = 0
False_negative = 0
for i in range(len_of_data):
    if (raw_df['Prediction'][i] == raw_df['Decision'][i] and raw_df['Prediction'][i] == 'Yes'):
        True_positive = True_positive + 1
        
    if((raw_df['Prediction'][i] != raw_df['Decision'][i] and raw_df['Prediction'][i] == 'No')):
        False_negative = False_negative + 1
    
    if((raw_df['Prediction'][i] != raw_df['Decision'][i] and raw_df['Prediction'][i] == 'Yes')):
        False_positive = False_positive + 1

idx = raw_df[raw_df['Prediction'] == raw_df['Decision']].index

accuracy = 100*len(idx)/len_of_data
precision = 100*True_positive/(True_positive + False_positive)
recall = 100*True_positive/(True_positive + False_negative)

F1_score = 2*(precision*recall)/(precision+recall)
print("accuracy: ", accuracy,"% trên tổng số ",len_of_data,"phép thử")
print("precision: ", precision, "% ")
print("recall: ", recall, "% ")
print("F1 score: ", F1_score)