import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np 
from sklearn import metrics
import time
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer 

def get_data_to_list(X):
    npoints = X.count()[0]
    list_X = []
    for n in range(npoints):
        x = X.iloc[n, :]
        list_X.append(x)
    return list_X


feature_in_rank = ['sload', 'rate', 'dur', 'sbytes', 'dload', 'dinpkt', 'sinpkt', 'sjit', 'stcpb', 'dtcpb', 'djit', 'tcprtt', 'synack', 'ackdat',
'ct_state_ttl', 'smean', 'dbytes', 'state', 'dmean', 'dttl', 'sttl', 'dpkts', 'proto', 'ct_dst_sport_ltm', 'spkts', 'service', 'dloss', 'ct_src_dport_ltm', 'ct_srv_dst', 'sloss', 'ct_srv_src', 'swin', 'dwin', 'ct_dst_src_ltm', 'ct_dst_ltm', 'ct_src_ltm', 'response_body_len', 'is_sm_ips_ports', 'ct_flw_http_mthd', 'trans_depth', 'is_ftp_login', 'ct_ftp_cmd']
lent_feature = len(feature_in_rank)
queue = []
f = open('ID3.txt', 'w')
while(1):

    lent_feature -=1
    if(lent_feature<0): exit()
    queue.append(feature_in_rank[lent_feature])

    df = pd.read_csv('UNSW_NB15_validation.csv')
    df.drop(columns = [i for i in queue], axis=1, inplace=True)
    #df_test = pd.read_csv('datasets/test.csv')
    X = df.iloc[:, :-1]
    y = df.iloc[:,-1]
    X = get_data_to_list(X)
    dv = DictVectorizer()
    dv.fit(X)

    X_vec = dv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size = 0.5)

    
    clf = DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=50, min_samples_leaf=2)
    clf.fit(X_train, y_train)

    #clf.fit(X_train, y_train)
    print('-----------build tree complete-------')
    pred = clf.predict(X_test)
    print('-----------predicting--------------')
    #print('rate:', metrics.accuracy_score(y_test, pred))
    rate = metrics.accuracy_score(y_test, pred)
    f.write('right rate: {} : {} \n'.format(lent_feature, rate))
    print('------------done--------------')
    

'''
clf = RandomForestClassifier(n_estimators=100)

dv = DictVectorizer()
dv.fit(X_train)
X_vec = dv.fit_transform(X_train)
clf.fit(X_vec, y_train)
#y_pred = clf.predict(X_test)


#print('rate :', metrics.accuracy_score(y_test, y_pred))
'''