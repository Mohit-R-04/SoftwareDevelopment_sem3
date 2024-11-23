
from datetime import datetime
from api import DateTimeApi

class Date(DateTimeApi):
    def __init__(self):
        super().__init__()

    def currentDate(self):
        '''returns current date in dd-mm-yyyy format'''
        return self.onlydateformated.strftime("%d-%m-%Y")

    def currentDateFormatMDY(self):
        '''returns current date in mm-dd-yyyy format'''
        return self.onlydateformated.strftime("%m-%d-%Y")

    def currentTime(self):
        '''returns current time in hh:mm:ss format'''
        return self.onlytime

    def createDate(self, year, month, day):
        '''returns date in dd-mm-yyyy format'''
        return datetime(year, month, day).strftime("%d-%m-%Y")

    def currentDatestr(self):
        '''returns current date in "Month Day, Year" format'''
        return datetime.strptime(self.onlydate, '%Y-%m-%d').strftime("%B %d, %Y")
