import math
temper = float(input())
wind_sp = float(input())
if(temper <= 10 and wind_sp > 4.8):
    print(13.12+0.6215*temper-11.37 * math.pow(wind_sp, 0.16) + 0.3965*temper*math.pow(wind_sp, 0.16))
else: print("Not valid, recheck input values")