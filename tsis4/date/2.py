import datetime 
сегодня  = datetime.date.today()
вчера = сегодня - datetime.timedelta(days = 1)
завтра = сегодня + datetime.timedelta(days = 1) 
print('Yesterday : ',вчера)
print('Today : ',сегодня)
print('Tomorrow : ',завтра)