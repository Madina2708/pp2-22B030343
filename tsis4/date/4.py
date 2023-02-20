from datetime import datetime
date1 = '25/5/2023 10:00:00'
date2 = '20/2/2023 19:13:17'
date_format_str = '%d/%m/%Y %H:%M:%S'
first = datetime.strptime(date1, date_format_str)
second =   datetime.strptime(date2, date_format_str)
diff = first - second
print('Difference between two datetimes in seconds:')
print(diff.total_seconds())