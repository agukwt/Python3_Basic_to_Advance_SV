from roboter.model import robot


class ConversationRobot(object):
    talk_restaurant_robot = robot.RestaurantRobot()
    talk_restaurant_robot.say_hello()
    talk_restaurant_robot.recommend_restaurant()
    talk_restaurant_robot.ask_restaurant()
    talk_restaurant_robot.say_good_bye()
