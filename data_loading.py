# import polars as pl
# import numpy as np
# import pandas as pd
# import pathlib
# from pathlib import Path

# data_path = "C:/Users/PraveenVanapalliClou/Downloads/home-credit-credit/"

# def set_table_dtypes(df: pl.DataFrame) -> pl.DataFrame:
#     for col in df.columns:
#         #Last letter of the column name
#         if col[-1] in ("P", "A"):
#             df = df.with_columns(pl.col(col).cast(pl.Float64).alias(col))
#     return df

# def convert_strings(df: pl.DataFrame) -> pl.DataFrame:
#     for col in df.columns:
#         if df[col].dtype.name in ['object', 'string']:
#             df[col] = df[col].astype("string").astype('category')
#             current_categories = df[col].cat.categories
#             new_categories = current_categories.to_list() + ["Unknown"]
#             new_dtype = pd.CategoricalDtype(categories=new_categories, ordered=True)
#             df[col] = df[col].astype(new_dtype)

#     return df

# train_basetable = pl.read_csv(data_path + "csv_files/train/train_base.csv")
# train_static = pl.concat([pl.read_csv(data_path + "csv_files/train/train_static_0_0.csv").pipe(set_table_dtypes), 
#                           pl.read_csv(data_path + "csv_files/train/train_static_0_1.csv").pipe(set_table_dtypes)],
#                           how="vertical_relaxed")

# train_static_cb = pl.read_csv(data_path + "csv_files/train/train_static_cb_0.csv").pipe(set_table_dtypes)
# train_person_1 = pl.read_csv(data_path + "csv_files/train/train_person_1.csv").pipe(set_table_dtypes)
# train_credit_bureau_b_2 = pl.read_csv(data_path + "csv_files/train/train_credit_bureau_b_2.csv").pipe(set_table_dtypes)


# train_person_1_feats_1 = train_person_1.group_by("case_id").agg(
#     pl.col("mainoccupationinc_384A").max().alias("mainoccupationinc_384A_max"),
#     (pl.col("incometype_1044T") == "SELFEMPLOYED").max().alias("mainoccupationinc_384A_any_selfemployed")
# )

# # Here num_group1=0 has special meaning, it is the person who applied for the loan.
# train_person_1_feats_2 = train_person_1.select(["case_id", "num_group1", "housetype_905L"]).filter(
#     pl.col("num_group1") == 0
# ).drop("num_group1").rename({"housetype_905L": "person_housetype"})

# # Here we have num_goup1 and num_group2, so we need to aggregate again.
# train_credit_bureau_b_2_feats = train_credit_bureau_b_2.group_by("case_id").agg(
#     pl.col("pmts_pmtsoverdue_635A").max().alias("pmts_pmtsoverdue_635A_max"),
#     (pl.col("pmts_dpdvalue_108P") > 31).max().alias("pmts_dpdvalue_108P_over31")
# )

# # We will process in this examples only A-type and M-type columns, so we need to select them.
# selected_static_cols = []
# for col in train_static.columns:
#     if col[-1] in ("A", "M"):
#         selected_static_cols.append(col)
# #print(selected_static_cols)

# selected_static_cb_cols = []
# for col in train_static_cb.columns:
#     if col[-1] in ("A", "M"):
#         selected_static_cb_cols.append(col)
# #print(selected_static_cb_cols)

# # Join all tables together.
# data = train_basetable.join(
#     train_static.select(["case_id"]+selected_static_cols), how="left", on="case_id"
# ).join(
#     train_static_cb.select(["case_id"]+selected_static_cb_cols), how="left", on="case_id"
# ).join(
#     train_person_1_feats_1, how="left", on="case_id"
# ).join(
#     train_person_1_feats_2, how="left", on="case_id"
# ).join(
#     train_credit_bureau_b_2_feats, how="left", on="case_id"
# )

# data_path_str = "C:/Users/PraveenVanapalliClou/Downloads/home-credit-credit/"

# # Convert the string to a Path object
# data_path = Path(data_path_str)

# # Assuming 'data' is your DataFrame
# path = data_path / "new_file.csv"
# data.write_csv(path, separator=",")


import pandas as pd
import boto3

def data_loading():
    path = "https://stock-market-usecase.s3.amazonaws.com/new_file.csv"
    df = pd.read_csv(path, low_memory=False)
    print(df)

    return df
data_loading()