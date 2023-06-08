def solve(width, height, length, mass):
    is_heavy = mass >= 20
    is_bulky = False
    if width * height * length >= 10000000:
        is_bulky = True
    if width * height >= 150:
        is_bulky = True
    if width * length >= 150:
        is_bulky = True
    if length * height >= 150:
        is_bulky = True
    if is_heavy and is_bulky:
        return ("rejected")
    if not is_heavy and not is_bulky:
        return("standard")
    if is_heavy or is_bulky:
        return("special")
    

  #exemple
print(solve(10,10,10,10))
print(solve(1000,1000,1000,10))
print(solve(10,10,10000,30))


