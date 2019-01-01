from datetime import date,datetime,timedelta,timezone
import time 
today = date.fromtimestamp(time.time())
print(today)
a = datetime.strftime(datetime.now(),"%Y/%m/%d %H:%M:%S")
print(a)