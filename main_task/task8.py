speed=input("speed of the car: ")
speed=int(speed)
remainder=speed-70
points=round(remainder/5)
if remainder>0:
    if points<=12:
        print(f"Points:{points}")
    else:
        print("license suspended")
else:
    print("okay")