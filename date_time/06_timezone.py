import persiantools
import datetime

import time
import pytz
from persiantools.jdatetime import JalaliDate

print(time.asctime())
Moscow = pytz.timezone('Europe/Moscow')
London = pytz.timezone('Europe/London')
New_York = pytz.timezone('America/New_York')

print('Moscow time : ',datetime.datetime.now(tz=Moscow))
print('London time : ',datetime.datetime.now(tz=London))
print('New York time : ',datetime.datetime.now(tz=New_York))
print(JalaliDate.today())