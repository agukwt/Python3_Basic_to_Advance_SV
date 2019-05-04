import os
import csv
import pandas as pd

__RANKING_CSV_PATH = r'restaurant_list.csv'


def echo_exist_restaurant():
    try:
        list_df = pd.read_csv(__RANKING_CSV_PATH, encoding='utf-8').sort_values('Count')
        return list_df.empty

    except FileNotFoundError:
        print('ランキングファイルが見つかりません。')


def sort_restaurant_list():
    try:
        list_df = pd.read_csv(__RANKING_CSV_PATH, encoding='utf-8') \
            .sort_values('Count', ascending=False)
        # print(list_df)

        # print(list_df.size)
        # for idx, rec in list_df.iterrows():
        #     print(rec['Name'])

        if list_df.empty:
            return False
        else:
            return list_df

    except FileNotFoundError:
        print('ランキングファイルが見つかりません。')

    except AttributeError:
        return False


def countup_list(restaurant_name):
    try:
        list_df = pd.read_csv(__RANKING_CSV_PATH, encoding='utf-8') \
            .sort_values('Count', ascending=False)

        now_num = list_df.loc[list_df['Name'] == restaurant_name, 'Count']
        list_df.loc[list_df['Name'] == restaurant_name, 'Count'] = now_num + 1

    except FileNotFoundError:
        print('ランキングファイルが見つかりません。')

    return list_df


def add_new_restaurant(restaurant_name):
    try:
        list_df = pd.read_csv(__RANKING_CSV_PATH, encoding='utf-8') \
            .sort_values('Count', ascending=False)

        restaurant_name_list = list_df['Name'].values.tolist()
        if restaurant_name in restaurant_name_list:
            # print('exit')
            return countup_list(restaurant_name)
        else:
            # print('no exist')
            add_row = pd.DataFrame([[restaurant_name, 1]], columns=['Name', 'Count'])
            return list_df.append(add_row)

    except FileNotFoundError:
        print('ランキングファイルが見つかりません。')

def write_list(dataflame):
    dataflame.to_csv(__RANKING_CSV_PATH, encoding='utf-8', header=True, index=False)
