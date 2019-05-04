from roboter.view import console
from roboter.model import ranking

ROBOT_NAME = 'Roboter'


class RestaurantRobot(object):
    def __init__(self):
        self.robot_name = ROBOT_NAME
        self.user_name = None
        self.agree_prefer_flag = False
        self.prefer_restaurant = None
        self.restaurant_list = None

    def say_hello(self):
        console.view_hello(self.robot_name)
        self.user_name = input()

    def recommend_restaurant(self):

        # check_there is a restaurant or not.
        if ranking.sort_restaurant_list() is not False:
            self.restaurant_list = ranking.sort_restaurant_list()

            restaurant_rank = 0
            for idx, row in self.restaurant_list.iterrows():
                console.view_recommend_restaurant(row['Name'])

                while True:
                    prefer_str = input()
                    if prefer_str.lower() == 'yes' or prefer_str.lower() == 'y':
                        self.agree_prefer_flag = True
                        self.prefer_restaurant = row['Name']
                        break

                    elif prefer_str.lower() == 'no' or prefer_str.lower() == 'n':
                        self.agree_prefer_flag = False
                        break

                    else:
                        print('指定した文字列を入力してください。')

                if self.agree_prefer_flag:
                    break
                else:
                    pass

        else:   # there is no restaurant so that Robot does not recommend.
            pass

    def ask_restaurant(self):

        if self.agree_prefer_flag:
            self.restaurant_list = ranking.countup_list(self.prefer_restaurant)
        else:
            console.view_ask_restaurant(self.user_name)
            users_prefer_restaurant = str(input())
            self.restaurant_list = ranking.add_new_restaurant(users_prefer_restaurant)

        ranking.write_list(self.restaurant_list)


    def say_good_bye(self):
        console.view_good_bye(self.user_name)
