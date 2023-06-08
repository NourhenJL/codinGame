def closestToZero(ts):
    if not ts:  # Empty list
        return 0

    closest_temp = ts[0]  # Initialize closest_temp with the first temperature in the list

    for temp in ts:
        if abs(temp) < abs(closest_temp) or (abs(temp) == abs(closest_temp) and temp > closest_temp):
            closest_temp = temp

    return closest_temp




l= [2,3,5,-1]

print(closestToZero(l))

