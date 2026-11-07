distance_mi=5
is_raining=True
has_car=True
has_bike=True
has_ride_sharp_app=0




if not distance_mi<= 0:
    print(False)
elif  distance_mi <=1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <=6:
    if has_bike and not is_raining :
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_sharp_app:
        print(True)
    else:
        print(False)

