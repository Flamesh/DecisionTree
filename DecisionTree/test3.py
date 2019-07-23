import Chefboost as chef 
import pandas as pd 

df = pd.read_csv('dataset/training2.txt')
df_test = pd.read_csv('dataset/testing3.txt')

X_test = df_test.iloc[:, :-1]
y_test = df_test.iloc[:, -1]

config = {'RandomForest': True, 'num_of_tree': 1}
    
model = chef.fit(df, config)
res = 0
total_rows = len(X_test)
for i in range(total_rows):
    x = X_test.iloc[i]
    prediction = chef.predict(model, x)
    if(prediction == y_test.iloc[i]):
        res = res + 1

#print(res/total_rows)

