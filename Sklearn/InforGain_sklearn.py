import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
import time
import graphviz 
from sklearn import preprocessing

def get_data_to_list(X):
    npoints = X.count()[0]
    list_X = []
    for n in range(npoints):
        x = X.iloc[n, :]
        list_X.append(x)
    return list_X

time_start = time.time()

df_train = pd.read_csv('training.csv')

#df_train.drop(df_train.columns[[42]], axis=1, inplace=True)

df_test = pd.read_csv('testing.csv')
#df_test.drop(df_test.columns[[42]], axis=1, inplace=True)

X_train = df_train.iloc[:, :-1]
y_train = df_train.iloc[:,-1]

X_test = df_test.iloc[:, :-1]
y_test = df_test.iloc[:, -1]




# attribute = ['dur', 'proto', 'service', 'state', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 'sttl', 'dttl', 'sload', 'dload', 'sloss', 'dloss', 'sinpkt', 'dinpkt', 'sjit', 'djit', 'swin', 'stcpb', 'dtcpb', 'dwin', 'tcprtt', 'synack', 'ackdat', 'smean', 'dmean', 'trans_depth', 'response_body_len', 'ct_srv_src', 'ct_state_ttl', 'ct_dst_ltm', 'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm', 'is_ftp_login', 'ct_ftp_cmd', 'ct_flw_http_mthd', 'ct_src_ltm', 'ct_srv_dst', 'is_sm_ips_ports', 'attack_cat']
# 43 features
# if dont want using feature, df_train.drop(df_train.columns[[0]], axis=1, inplace=True)

#X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size = 0.3)

clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=50, min_samples_leaf=2)
clf.fit(X_train, y_train)


pred = clf.predict(X_test)
print('rate:', metrics.accuracy_score(y_test, pred))

time_end = time.time()
print('time run:', time_end - time_start)

