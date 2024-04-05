from data_cleaning import data_cleaning
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image

def data_vis():
    data = data_cleaning()
    column = list(data.columns)


    column_to_remove = ["currdebtcredtyperange_828A", "lastapprcommoditycat_1041M", "lastrejectcommoditycat_161M",
                        "maritalst_385M", "person_housetype", "pmts_dpdvalue_108P_over31", "totalsettled_863A", "target", 
                        "lastrejectreasonclient_4145040M", "annuitynextmonth_57A", "lastcancelreason_561M"]
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)
#     
    columns_to_remove_outliers = ["annuity_780A", "annuitynextmonth_57A",
                                  "lastrejectreason_759M", "mainoccupationinc_384A_max"]

    for col in columns_to_remove_outliers:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        data = data.loc[(data[col] < upper_limit) & (data[col] > lower_limit)]


    for i in column:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"{i}_hist.jpg")

    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"{i}_box.jpg")

    columns_to_remove=["target"]
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark', width=1800, height=1400)
    # fig.show()
    fig.write_image("img.jpg")


    return data

data_vis()