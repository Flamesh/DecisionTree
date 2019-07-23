import pandas as pd 
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_extraction import DictVectorizer
import re 

def get_data_to_list(X):
    npoints = X.count()[0]
    list_X = []
    for n in range(npoints):
        x = X.iloc[n, :]
        list_X.append(x)
    return list_X

def get_array(feature_names, feature_score):
    names = []
    scores = []
    #total_score = 0
    for score, fname in sorted(zip(feature_score, dv.get_feature_names()), reverse = True):
        name = re.findall(r"[\w']+", fname)
        names.append(name[0])
        scores.append(float(score))
        #total_score += score
    #print(total_score)
    return names, scores


df = pd.DataFrame.from_csv('datasets/training_data.csv')
X = df.iloc[: ,:-1]
y = df.iloc[:, -1]
feature_names = list(X)
X = get_data_to_list(X)
dv = DictVectorizer()

X_vec = dv.fit_transform(X)
feature_score = mutual_info_classif(X_vec, y, discrete_features=True)
names, scores = get_array(feature_names, feature_score)

sum_score = []
for i in range(len(feature_names)):
    total_score = 0
    for j in range(len(names)):
        if(feature_names[i] == names[j]):
            total_score += scores[j]
    sum_score.append({feature_names[i]: float(total_score)})

for i in sum_score:
    print(i)

#for score, fname in sorted(zip(feature_score, dv.get_feature_names()), reverse = True): print(fname, score)
#for score, fname in sorted(zip(feature_scores, dv.get_feature_names()), reverse = True):
    #print(fname, score)
