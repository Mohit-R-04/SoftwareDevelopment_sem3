
from datetime import datetime

class Validity:
    def is_valid_time(self, time):
        try:
            datetime.strptime(time, '%H:%M:%S')
            return True
        except ValueError:
            return False

    def is_valid_date(self, date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False
