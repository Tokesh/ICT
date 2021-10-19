import datetime
secondz = int(input())
x = datetime.timedelta(seconds = secondz)
print(x)

#OR

time = float(input())
day = time // (24 * 3600)
time = time % (24 * 3600)

hour = int(time // 3600)
time %= 3600
hour_str = str(hour)
if(len(hour_str)==1): hour_str = "0" + hour_str

minutes = int(time // 60)
time %= 60
minutes_str = str(minutes)
if(len(minutes_str)==1): minutes_str = "0" + minutes_str

seconds = int(time)
seconds_str = str(seconds)
if(len(seconds_str)==1): seconds_str = "0" + seconds_str
print(str(int(day)) + ":" + hour_str + ":" + minutes_str + ":" + seconds_str)