import Chefboost as chef 
import pandas as pd
from commons import functions



df_test = pd.read_csv('dataset/training3.txt')

X_test = df_test.iloc[:, :-1]
y_test = df_test.iloc[:, -1]

total_rows = len(X_test)

moduleName = "outputs/rules/rules"
tree = functions.restoreTree(moduleName)

res = 0
for i in range(total_rows):
    x = X_test.iloc[i]
    tt = []
    for i, (key, value) in enumerate(x.items()):
        if i > 0 and i < 4:
            tt.append(value)
        else:
            tt.append(float(value))
    prediction = tree.findDecision(tt)
    if(prediction == y_test.iloc[i]):
        res = res + 1

print(res/total_rows)
exit()
x = X_test.iloc[1]
tt = []
for i, (key, value) in enumerate(x.items()):
    if i > 0 and i < 4:
        tt.append(value)
    else:
        tt.append(float(value))

#test_instance = [0.000004,"udp","-","INT",2,0,1454,0,250000.0006,254,0,1454000000,0,0,0,0.004,0,0,0,0,0,0,0,0,0,0,727,0,3,2,1,1,3,0,0,3]


prediction = tree.findDecision(tt)

print(prediction)