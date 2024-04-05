from sklearn.calibration import LabelEncoder
from data_analysis import data_analysis


def data_cleaning():
    data = data_analysis()

    label_encoder = LabelEncoder()

    columns_to_encode = ['pmts_dpdvalue_108P_over31', 'person_housetype', 'mainoccupationinc_384A_any_selfemployed', 'description_5085714M', 'education_1103M', 'education_88M', 'maritalst_385M', 'maritalst_893M', 'previouscontdistrict_112M',
                         'lastrejectreasonclient_4145040M', 'lastrejectreason_759M', 'lastrejectcommodtypec_5251769M', 'lastrejectcommoditycat_161M', 'lastcancelreason_561M',
                         'lastapprcommoditytypec_5251766M', 'lastapprcommoditycat_1041M', 'date_decision']

    # Apply label encoding to specified columns
    for column in columns_to_encode:
        data[column] = label_encoder.fit_transform(data[column])

    data.drop(['pmtaverage_4527227A', 'totaldebt_9A', 'sumoutstandtotal_3546847A',
                'sumoutstandtotalest_4493215A', 'maxoutstandbalancel12m_4187113A',
                'maxdebt4_972A', 'inittransactionamount_650A', 'disbursedcredamount_1113A',
                'currdebt_22A', 'credamount_770A', 'avginstallast24m_3658937A', 'avglnamtstart24m_4525187A',
                'avgoutstandbalancel6m_4187114A', 'avgpmtlast12m_4525200A', 'date_decision', 'MONTH', 'WEEK_NUM',
                'education_88M', 'maritalst_893M', 'maxpmtlast3m_4525190A', 'totinstallast1m_4525188A', 'mainoccupationinc_384A_any_selfemployed',
                'pmtaverage_3A', 'pmtssum_45A', 'pmtaverage_4955615A', 'description_5085714M', 'price_1097A', 'maxannuity_4075009A',
                'lastrejectcommodtypec_5251769M', 'downpmt_116A', 'lastapprcommoditytypec_5251766M', 'pmts_pmtsoverdue_635A_max', 'maxlnamtstart6m_4525199A',
                'maxinstallast24m_3658928A', 'maxannuity_159A', 'maininc_215A', 'lastrejectcredamount_222A', 'lastotherlnsexpense_631A', 'lastotherinc_902A', 'lastapprcredamount_781A',
                'amtinstpaidbefduel24m_4187115A'], axis=1, inplace=True  )


    data.dropna().sum()

    return data

data_cleaning()