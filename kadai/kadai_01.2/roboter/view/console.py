import os
import string

__HELLO_TEMPLATE_PATH = r'roboter/design/hello.txt'
__RECOMMEND_RESTAURANT_TEMPLATE_PATH = r'roboter/design/recommend_restaurant.txt'
__ASK_RESTAURANT_TEMPLATE_PATH = r'roboter/design/ask_restaurant.txt'
__GOOD_BYE_TEMPLATE_PATH = r'roboter/design/good_bye.txt'


def file_check(path):
    try:
        os.path.exists(path)
    except FileNotFoundError:
        print('指定テンプレートが見つかりません。')


def read_template(template_path):
    file_check(template_path)

    with open(template_path, 'r', encoding="utf-8") as f:
        template = string.Template(f.read())

    return template


def view_hello(robot_name):
    path = __HELLO_TEMPLATE_PATH

    file_check(path)
    tmp = read_template(path)
    contents = tmp.substitute(robot_name=robot_name)

    print(contents)


def view_recommend_restaurant(recommend_restaurant):
    path = __RECOMMEND_RESTAURANT_TEMPLATE_PATH

    file_check(path)
    tmp = read_template(path)
    contents = tmp.substitute(restaurant_name=recommend_restaurant)

    print(contents)


def view_ask_restaurant(user_name):
    path = __ASK_RESTAURANT_TEMPLATE_PATH
    file_check(path)
    tmp = read_template(path)
    contents = tmp.substitute(name=user_name)

    print(contents)


def view_good_bye(user_name):
    path = __GOOD_BYE_TEMPLATE_PATH
    file_check(path)
    tmp = read_template(path)
    contents = tmp.substitute(name=user_name)

    print(contents)
