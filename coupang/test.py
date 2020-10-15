import datetime

d1 = datetime.datetime(2008, 4, 1)
d2 = datetime.datetime(2018, 4, 1)
delta = d2 - d1
asdf = delta.total_seconds()
print(asdf)