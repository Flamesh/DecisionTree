import Chefboost as chef 
import pandas as pd 

df = pd.read_csv('dataset/training3.txt')
df_test = pd.read_csv('dataset/testing2.txt')

X_test = df_test.iloc[:, :-1]
y_test = df_test.iloc[:, -1]

test_instance = X_test.head(0)

config = {'algorimthm': 'ID3'}

model = chef.fit(df, config)
chef.save_model(model, "model.pkl")

prediction = chef.predict(model, test_instance)
print(prediction)