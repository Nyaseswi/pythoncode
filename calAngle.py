def problem():
    hour = 3
    minute = 44
    # Calculate the angle
    angle = (360/12 *hour)
    minute = (360/60 *minute)
    subs = minute - hour
    print('The angle between circle and hours is :', angle)
    print('The angle between circle and minute is :', minute)
    print('Value of minute minus hour is:',subs)
problem()