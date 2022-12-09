from datetime import datetime
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

result = datetime1 - datetime2
print(type(result))
print(result)
print(result.seconds)
print(result.total_seconds())
