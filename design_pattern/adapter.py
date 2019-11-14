# -*- coding: utf-8 -*-
import datetime

class AgeCalculator:
    def __init__(self, birthday):
        # birthday = "1970-01-01"
        self.year, self.month, self.day = (int(i) for i in birthday.split("-"))

    def calculate_age(self, date):
        year, month, day = (int(i) for i in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age

class DateAgeAdapter:
    def _str_date(self,date):
        return date.strftime("%Y-%m-%d")

    def __init__(self,birthday):
        birthday = self._str_date(birthday)
        self.calculate = AgeCalculator(birthday)

    def get_age(self, date):
    # def calculate_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)


# class AgeableDate(datetime.date):
#     def split(self):
#         return self.year, self.month, self.day
#
# s = datetime.datetime(2001,1,11).strftime("%Y-%m-%d")
# year, month, day = (int(i) for i in s.split("-"))
#
# bd = AgeableDate(1975, 6, 14)
# today = AgeableDate.today()
# today.split()
# bd.split()
# a = AgeCalculator(bd)
# a.calculate_age(today)