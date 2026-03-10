#differnce between arguments (*args) and keyword arguments (**kwargs)
def function_with_args(*args):
    for arg in args:
        print(arg)

def function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print("Using *args:")
function_with_args(1, 2, 3, "hello")
print("\nUsing **kwargs:")
function_with_kwargs(name="Alice", age=30, city="New York")