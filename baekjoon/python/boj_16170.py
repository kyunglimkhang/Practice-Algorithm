import datetime
# https://www.acmicpc.net/problem/16170

today = datetime.datetime.today()

print(today.strftime("%Y"))
print(today.strftime("%m"))
print(today.strftime("%d"))