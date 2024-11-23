
import requests
from datetime import datetime

class DateTimeApi:
    def __init__(self):
        self.timelndia = requests.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata')
        self.timelndia = self.timelndia.json()
        self.onlydate = self.timelndia['datetime'][0:10]
        self.onlydateformated = datetime.strptime(self.onlydate, '%Y-%m-%d')
        self.onlytime = self.timelndia['datetime'][11:19]
