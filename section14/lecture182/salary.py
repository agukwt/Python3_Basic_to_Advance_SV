import requests


class ThirdPartyBonusApi(object):
    def get_api_name(self):
        return 'Bonus'

    def bonus_price(self, year):
        r = requests.get('http://localhost/bonus', params={'year': year})
        # {"price": 100}
        # raise ConnectionRefusedError
        return r.json()['price']


class Salary(object):
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBonusApi()
        self.base = base
        self.year = year

    def calculation_salary(self):
        bonus = 0
        if self.year < 2020:
            try:
                bonus = self.bonus_api.bonus_price(year=self.year)
            except ConnectionRefusedError:
                bonus = 0
        return self.base + bonus

