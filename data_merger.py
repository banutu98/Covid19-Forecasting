import pandas as pd


def melt_dataframe(df: pd.DataFrame, new_column_name):
    df = pd.melt(df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_name=new_column_name)
    df = df.rename(columns={'variable': 'Date'})
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    df = df.sort_values(['Country/Region', 'Date'])
    df.reset_index(inplace=True)
    del df['index']
    return df


def main():
    df_c = pd.read_csv('new_data/confirmed.csv')
    df_d = pd.read_csv('new_data/deaths.csv')
    df_r = pd.read_csv('new_data/recovered.csv')

    df_c = melt_dataframe(df_c, new_column_name='ConfirmedCases')
    df_d = melt_dataframe(df_d, new_column_name='Fatalities')
    df_r = melt_dataframe(df_r, new_column_name='RecoveredCases')

    final_df = df_c.merge(df_d)
    final_df = final_df.merge(df_r, how='left')
    final_df['Province/State'] = final_df['Province/State'].fillna('')
    final_df['RecoveredCases'] = final_df['RecoveredCases'].fillna(0)

    final_df.to_csv('new_data/train.csv', index_label='Id')


if __name__ == '__main__':
    main()
