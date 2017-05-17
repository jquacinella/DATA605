def derivative(f, x):
    count = 0           # Keep track of the numvber of loops
    h = 1               # h is our parameter we need to calculate a derivative
    delta_h = 0.01      # What do we decrement h by
    tolerance = 0.0001  # How accurate do we want our derivatives to be
    max_loops = 1000    # Maximum number of loops to prevent an infinite loop
    old_deriv = None

    while True:
        # Calculate an approximation to the derivative for our h
        deriv = ( f(x+h) - f(x) ) / h
        print(deriv)

        # If the difference between our current estimate and our old estimate
        # is less than some tolerance, return it
        if old_deriv and (abs(deriv - old_deriv) < tolerance):
            return deriv
        else:
            # Otherwise, our current estimate becomes next iterations 'old' estimate
            old_deriv = deriv

        # Here we check that if we were to update h that we would not end up
        # negative or at 0. The h value cannot be 0 in the equation above
        if h - delta_h <= 0:
            delta_h = delta_h / 10.0

        # Update h to get closer to 0
        h = h - delta_h

        # This will prevent an infinite loop
        count += 1
        if count > max_loops:
            return deriv

def test_function(x):
    return x*x*x + 2*x*x

print( derivative(test_function, 2) )