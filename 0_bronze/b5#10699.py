import datetime as dt

x = dt.datetime.now()

print('{}-{}-{}'.format(x.year, x.strftime('%m'), x.strftime('%d')))
# 모범답안
import datetime

print(datetime.date.today())