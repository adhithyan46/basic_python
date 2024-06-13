# import time
# crnt_time=time.time()
# print("current time=",crnt_time)


# #Local time

# import time
# time_sec=time.time() #time will be in seconds
# local_time=time.ctime(time_sec)#time converted into local time
# print("local time=",local_time)

# #

# import time
# crnt_time=time.time()
# date=time.localtime(crnt_time)
# print("date=",date)
# print("\n year=",date.tm_year)#printing only year

#date in formate

import time
crnt_time=time.localtime()
date_time=time.strftime("%d/%m/%Y \n%H:%M:%S",crnt_time)
print(date_time)

