import pandas as pd


def melt_data_frame(df: pd.DataFrame, new_column_name):
    df = pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_name=new_column_name)
    df = df.rename(columns={'variable': 'Date'})
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    df = df.sort_values(['Country/Region', 'Date'])
    df.reset_index(inplace=True)
    del df['index']
    return df


def create_test_data():
    train_df = pd.read_csv('new_data/train.csv')
    test_df = train_df[['Province_State', 'Country_Region']].copy()
    test_df['Province_State'] = test_df['Province_State'].fillna('')
    dates = pd.date_range(start='2020-04-19', end='2020-05-30')
    groups = test_df.groupby(['Country_Region', 'Province_State'])
    test_df = test_df[test_df.Province_State.isna()]
    test_df['Date'] = 0
    for group in groups:
        country = group[0][0]
        province = group[0][1]
        for date in dates:
            date = str(date).split()[0]
            test_df = test_df.append({'Province_State': province, 'Country_Region': country, 'Date': date},
                                     ignore_index=True)
    test_df['Date'] = pd.to_datetime(test_df['Date'], infer_datetime_format=True)
    test_df.to_csv('new_data/test.csv', index_label='ForecastId')


def main():
    df_c = pd.read_csv('new_data/confirmed.csv')
    df_d = pd.read_csv('new_data/deaths.csv')
    df_r = pd.read_csv('new_data/recovered.csv')

    df_c = melt_data_frame(df_c, new_column_name='ConfirmedCases')
    df_d = melt_data_frame(df_d, new_column_name='Fatalities')
    df_r = melt_data_frame(df_r, new_column_name='RecoveredCases')

    final_df = df_c.merge(df_d)
    final_df = final_df.merge(df_r, how='left')
    final_df['Province/State'] = final_df['Province/State'].fillna('')
    final_df['ConfirmedCases'] = final_df['ConfirmedCases'].fillna(0)
    final_df['Fatalities'] = final_df['Fatalities'].fillna(0)
    final_df['RecoveredCases'] = final_df['RecoveredCases'].fillna(0)
    final_df = final_df.rename(columns={'Province/State': 'Province_State', 'Country/Region': 'Country_Region'})

    final_df.to_csv('new_data/train.csv', index_label='Id')


if __name__ == '__main__':
    main()
