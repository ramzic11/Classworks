



# print(1 and 0)


# print(2 and 0)






hours = int(input(" enter ocklock: "))
mins = int(input(" enter minutes: "))
delta = int(input("enter delta: "))
result_hours = (hours + delta) % 24
if result_hours < 10 :
    result_hours = "0" + str(result_hours)
if mins < 10 :
    mins = "0" + str(mins)
print(f"{result_hours} : {mins}")





