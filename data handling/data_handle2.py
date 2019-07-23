import numpy as np 
import pandas as pd 

#author Flamesh

def entropy(freq):
    freq_0 = freq[np.array(freq).nonzero()[0]]
    prob_0 = freq_0/float(freq_0.sum())
    return -np.sum(prob_0*np.log(prob_0))

def _entropy(target, ids):
        # calculate entropy of a node with index ids
        if len(ids) == 0: return 0
        ids = [i+1 for i in ids] # panda series index starts from 1
        freq = np.array(target[ids].value_counts())
        return entropy(freq)

df_train = pd.DataFrame.from_csv('UNSW_NB15_training.csv')
df_train.drop(df_train.columns[[42]], axis=1, inplace=True)
X_train = df_train.iloc[:, :-1]
y_train = df_train.iloc[:, -1]
attributes = list(X_train)
Ntrain = X_train.count()[0]
ids = range(Ntrain)
sub_data = X_train.iloc[ids, :]

#print(_entropy(y_train, ids))
for i, att in enumerate(attributes):
    values = X_train.iloc[ids, i].unique().tolist()
    splits = []
    for val in values:
        sub_ids = sub_data.index[sub_data[att] == val].tolist() #get id
        splits.append([sub_id - 1 for sub_id in sub_ids])
    HxS = 0
    for split in splits:
         HxS += len(split)*_entropy(y_train, split)/len(ids)
    print(float(1-HxS))
  
    