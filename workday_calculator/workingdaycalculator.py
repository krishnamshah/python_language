"""
This program should allow you to input a start date and time, add or subtract a certain number of working days, and
output the resulting date and time based on the specified working hours and holidays.
"""


import datetime


class WorkingDayCalculator:

    def __init__(self, start_time=datetime.time(8, 0), end_time=datetime.time(16, 0)):
        self.start_time = start_time
        self.end_time = end_time
        self.holidays = []
        self.recurring_holidays = []

    def set_holidays(self, holidays):
        self.holidays = holidays

    def set_recurring_holidays(self, recurring_holidays):
        self.recurring_holidays = recurring_holidays


    def is_workday(self, date):
        """
        Checks if the given date is a workday or not.
        :param date: datetime
        :return: True if workday, otherwise False
        """
        if date.weekday() > 4:
            return False
        # if date in self.holidays:
        #     return False
        for holiday in self.holidays:
            if date.year == holiday.year and date.month == holiday.month and date.day == holiday.day:
                return False
        for recurr_holiday in self.recurring_holidays:
            if date.month == recurr_holiday.month and date.day == recurr_holiday.day:
                return False
        return True

    def extracting_decimal_points(self, num_workdays):
        """
        Extracts the decimal part at the same time tries to avoid Rounding Error.
        :param num_workdays: float
        :return: first_part : int
                second_parts : int
        """
        string = str(num_workdays)
        first_part = int(string.split(".")[0])
        second_part = string.split(".")[1]
        second_parts = int(second_part) / 10 ** (int(len(second_part)))
        return first_part, second_parts

    def add_workdays(self, start_date, num_workdays):
        """
        It adds the given number of working dates and gives the final result which is also a working day at the same
        time checks wherever necessary if the date is working day or not.
        :param start_date: datetime
        :param num_workdays: float
        :return: result_date : float
        """
        num_workdays = float(num_workdays)
        # Adjust the start date to the nearest working hour
        start_time = start_date.time()
        if start_time < self.start_time:
            start_date = datetime.datetime.combine(start_date.date(), self.start_time)
        elif start_time > self.end_time:
            start_date = datetime.datetime.combine(start_date.date() + datetime.timedelta(days=1), self.start_time)

        # Check if the current day is a working day
        while not self.is_workday(start_date):
            start_date += datetime.timedelta(days=1)

        if num_workdays == 0:
            return start_date

        # Calculate the integer and decimal part of num_workdays
        int_part, dec_part = self.extracting_decimal_points(num_workdays)
        int_part = int(int_part)
        dec_part = round(dec_part, 3)
        dec_part = int(dec_part * 8 * 60 * 60) # Convert decimal part to seconds

        # Add the integer part of num_workdays
        sign = 1 if int_part > 0 else -1
        int_part = abs(int_part)
        cur_date = start_date

        while int_part > 0:
            if sign == -1:
                cur_date -= datetime.timedelta(days=1)
            else:
                cur_date += datetime.timedelta(days=1)

            if self.is_workday(cur_date):
                int_part -= 1

        # Add the decimal part of num_workdays
        while dec_part > 0:

            if sign == 1:
                cur_date += datetime.timedelta(seconds=1)
                while not self.is_workday(cur_date) or cur_date.time() > self.end_time:
                    cur_date += datetime.timedelta(days=1)
                    cur_date = datetime.datetime.combine(cur_date.date(), self.start_time)
                dec_part -= 1

            else:
                cur_date -= datetime.timedelta(seconds=1)
                while not self.is_workday(cur_date) or cur_date.time() < self.start_time:
                    cur_date -= datetime.timedelta(days=1)
                    cur_date = datetime.datetime.combine(cur_date.date(), self.end_time)
                dec_part -= 1


        curr_date = cur_date.strftime("%Y-%m-%d %H:%M")
        result_date = datetime.datetime.strptime(curr_date, "%Y-%m-%d %H:%M")
        return result_date


# Example usage:
calculator = WorkingDayCalculator()
calculator.set_recurring_holidays([datetime.date(2004, 5, 17)])
calculator.set_holidays([datetime.date(2004, 5, 27)])
start_date = datetime.datetime(2004, 5, 24, 19, 3)
result = calculator.add_workdays(start_date, 44.723656)
print(result)  # Output: 2004-05-14 12:00:00
# print("\n Expected:")
# print(datetime.datetime(2004, 7, 27, 13, 47))


