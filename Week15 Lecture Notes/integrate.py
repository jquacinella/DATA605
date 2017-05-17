def integrate(f, a, b):
    area = None
    old_area = None
    count = 0
    n = 2
    max_loops = 1000
    tolerance = 0.000001

    while True:
        # Divide the range into n pieces of size delta_x
        delta_x = (b - a) / n

        # Start with a, iterate over these pieces
        x = a
        area = 0
        while x < b:
            # Calculate the area using the mid point rule
            # NOTE: you could use x + delta_x, or x, depending on how you 
            # want to calculate areas; the midpoint rule is pretty accurate
            area += f(x + delta_x/2) * delta_x
            x += delta_x

        if old_area and (abs(area - old_area) < tolerance):
            return area
        else:
            # Otherwise, our current estimate becomes next iterations 'old' estimate
            print(area)
            old_area = area

        # Increment the number of pieces
        n += 1

        # This will prevent an infinite loop
        count += 1
        if count > max_loops:
            return area

def test_function(x):
    return 3*x*x + 4*x

print( integrate(test_function, 1, 3) )