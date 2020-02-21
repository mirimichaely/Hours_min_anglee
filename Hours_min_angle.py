def find_angle_btwn_hrs_min(x, y):

    hour_angle = (360 / 12) * x  # hours in full cycle divided by degrees in full circle
    revised_hour_angle= hour_angle + ((360/12)/60)*y
    min_angle = (360 / 60) * y #minutes in full cycle divided by degrees in full circle
    angle_btw = abs(revised_hour_angle - min_angle)
    return min(angle_btw, 360 - angle_btw) #returns the smallest angle between the two