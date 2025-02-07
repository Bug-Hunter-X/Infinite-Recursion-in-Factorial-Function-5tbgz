def function(x):
    if x < 0:
        return "Input must be a non-negative integer"
    elif x == 0:
        return 1
    else:
        return x * function(x-1)

print(function(5)) # Output: 120
print(function(-1)) # Output: Input must be a non-negative integer