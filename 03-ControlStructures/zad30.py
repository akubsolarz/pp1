time = input("Enter time (24-hour format): ")
go = int(time[0:2])
if int(time[0:2]) >  12 :
    print(f"Time in 12-hour format: {int(time[0:2])-12}:{time[3:]}pm")
else: 
    print(f"Time in 12-hour format: {time}am")