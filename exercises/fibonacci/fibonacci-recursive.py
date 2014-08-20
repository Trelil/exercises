input = int(raw_input("Enter a number: "));
# Alternatively:
# input = input("Enter a number; ");
# The difference is that input() parameter is evaluated as a command,
# whereas raw_input() evaluates the parameter as a string

def next_fibonacci(prev, curr, stop_after):
    """Recursively searches for the fibonacci number that
    comes after the stop_after value"""
    
    # Stop if the sought fibonacci number has been found.
    # (The only reason I chose to look at the previous of the two numbers
    # is that I want it to include 0 as a possible return value as well,
    # which will happen with a negative input value).
    if (prev > stop_after):
        return prev;
    return next_fibonacci(curr, curr + prev, stop_after)
    
print next_fibonacci(0, 1, input);