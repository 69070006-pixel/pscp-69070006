"""divide10loop"""
number = int(input())
firstoutput = (number // 10) * 10
for i in range(firstoutput, -10, -10):
    print(i, end=" ")
