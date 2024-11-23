
from api import DateTimeApi
from datetime import datetime, timedelta

class Difference(DateTimeApi):
    def __init__(self):
        super().__init__()

    def difference_with_current(self, date):
        date = datetime.strptime(date, '%Y-%m-%d')
        return (date - self.onlydateformated).days

    def difference(self, date1, date2):
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.strptime(date2, '%Y-%m-%d')
        return (date2 - date1).days

    def days_after(self, days):
        return (self.onlydateformated + timedelta(days=days)).strftime("%Y-%m-%d")

    def days_before(self, days):
        return (self.onlydateformated - timedelta(days=days)).strftime("%Y-%m-%d")

    def month_after(self, months):
        return (self.onlydateformated + timedelta(days=months*30)).strftime('%Y-%m-%d')

    def month_before(self, months):
        return (self.onlydateformated - timedelta(days=months*30)).strftime('%Y-%m-%d')
