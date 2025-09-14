import time

def log_exec_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)  
        end_time = time.time()
        execution_time = end_time - start_time
        fname = function.__name__
        print(f"Function '{fname}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Example usage
@log_exec_time
def process_data(data):
    total = 0
    for i in data:
        total += i ** 2
        time.sleep(0.01) 
    return total

if __name__ == "__main__":
    numbers = range(100)
    result = process_data(numbers)
    print("Result:", result)
