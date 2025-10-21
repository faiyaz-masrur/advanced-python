
x = "global x"

def outer_function():
    x = "outer x"

    def inner_function():
        x = "inner x"
        print("Inside inner_function:", x)

    def modify_outer():
        nonlocal x  
        x = "modified by inner (nonlocal)"
        print("Inside modify_outer:", x)

    inner_function()
    modify_outer()
    print("Inside outer_function after modification:", x)

def global_modifier():
    global x  
    x = "modified globally"
    print("Inside global_modifier:", x)

print("Initially:", x)
outer_function()
print("After outer_function:", x)
global_modifier()
print("After global_modifier:", x)
