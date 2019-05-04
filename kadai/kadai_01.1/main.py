#!/usr/bin/python
# -*- coding: utf8 -*-

import re

import pandas as pd
import csv


class Inquire(object):
    def __init__(self):
        # class variable
        self.name = None
        self.restaurant = None

        # read statement
        # statement_path = r'design/statement.txt'
        self.statements = pd.read_csv("design/statement.txt", encoding='utf8', engine='python')

        # read past preference data
        # preference_data_path = r'preference_data.csv'
        self.preference_data = pd.read_csv("preference_data.csv", encoding='utf8', engine='python')

    def reg_statement(self, statement, reg_dict):
        reg_statement = statement

        for key, value in reg_dict.items():
            reg_statement = re.sub(key, value, reg_statement)

        return reg_statement

    def check_preference(self, shop):
        pass

    def register_data(self, prefer_shop):
        # 登録嗜好データの店舗の重複削除
        preference_shop_set = set(self.preference_data['NAME'].unique())

        # 好みの店舗が登録嗜好データにあるかで挙動変更
        register_df = pd.DataFrame()
        if(self.restaurant in preference_shop_set):
            # count up
            num1 = self.preference_data['NAME']
            print(num1)
            num = self.preference_data['NAME'].values.tolist().index(self.restaurant)
            print(num)


            now_count = self.preference_data.iloc[num][1]

            self.preference_data.iloc[num, 1] = str(int(now_count) + 1)
            register_df = self.preference_data
        else:
            append_df = pd.DataFrame([[self.restaurant, 1]], columns=['NAME', 'COUNT'])
            register_df = pd.concat([self.preference_data, append_df])

        # write down register_df
        # ?? not cool
        register_df.to_csv("preference_data.csv", header=True, index=False,
                           encoding='utf8', quoting=csv.QUOTE_NONE, quotechar="")




    def greeting(self):
        # 初期挨拶
        # ??辞書推奨
        print(self.statements.iloc[0][1])

        # get name
        self.name = str(input())

    def recommend_shop(self):
        try:
            sort_preference_data = self.preference_data.sort_values('COUNT')

            breakout_flag = False
            for shop in sort_preference_data['NAME']:
                breakout_flag = self.check_preference(shop)

                if (breakout_flag == True):
                    break

        except Exception:
            pass


    def ask_prefer_shop(self):
        # ??Not cool
        reg_dic = {'\$NAME\$': self.name}

        # 好みのレストランを聞く（名前入り）
        # ??辞書推奨
        base_str = str(self.statements.iloc[1][1])
        print(self.reg_statement(base_str, reg_dic))

        # get prefer shop
        self.restaurant = str(input())

        self.register_data(self.restaurant)





def main():
    inq = Inquire()
    inq.greeting()
    inq.recommend_shop()
    inq.ask_prefer_shop()


def test():
    statements = pd.read_csv("design/statement.txt", encoding='utf8', engine='python')
    print(type(statements))


if __name__ == '__main__':
    main()
    #test()