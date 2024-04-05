from data_cleaning import data_cleaning

def feat_eng():
    data = data_cleaning()
    print(data)

    data.to_csv("Home_credit.csv", index=False)

    return data

feat_eng()