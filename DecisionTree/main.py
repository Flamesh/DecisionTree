import Chefboost as chef
import pandas as pd


while(1):
    print("Chọn loại thuật toán sử dụng (ID3, C4.5, CART, RandomForest): ")
    decisionTree = input()
    if(decisionTree == "RandomForest"):
        print("Nhập số cây muốn tạo: ")
        num_of_tree = input()
        config = {'RandomForest': True, 'num_of_tree': num_of_tree}
    
    else:
        config = {'algorithm': decisionTree}
        
    print("Nhập đường dẫn tới file chứa dữ liệu: ")
    dataFile = input()
    df = pd.read_csv(dataFile)
    
    model = chef.fit(df, config)

    print("Kết thúc chương trình (yes/no) ??: ")
    end = input()
    if(end == 'yes'):
        exit()