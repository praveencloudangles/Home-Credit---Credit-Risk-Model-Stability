from data_cleaning import data_cleaning

def feat_eng():
    data = data_cleaning()
    print(data)

    data = data.dropna(axis=1)
    
    data.to_csv("Home_credit.csv", index=False)

    return data

feat_eng()
