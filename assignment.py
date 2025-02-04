def format_string(name: str, age: int) -> str:

    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    pass

    return f"My name is {name} and I am {age} years old"
    
str1 = format_string("John", 25)
str2 = format_string("Alice", 30)
print(str1)
print(str2)


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    pass
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
    
print(conditional_check(11))  # Output: Greater
print(conditional_check(2))   # Output: Lesser
print(conditional_check(10))  # Output: Equal


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    pass
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(loop_sum(5)) 
print(loop_sum(3)) 
print(loop_sum(1))

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    
    return (sum(numbers), max(numbers), min(numbers))
result1 = list_operations([1, 2, 3, 4, 5])
result2 = list_operations([10, 20, 30])
print(result1)
print(result2)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    pass

    return [name for name, score in students_dict.items() if score > 80]

students = {
    'Suman': 88,
    'Makai': 91,
    'Suraj': 85,
    'Saman': 75
    
}

result = dict_operations(students)
print(result)

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list


    Returns:
        set: Common elements
    """
    pass

    return set(list1).intersection(list2)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = set_operations(list1, list2)
print(result)

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    pass

# Initialize 
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
    }
    
    # avoid division by zero
    if b != 0:
        results['quotient'] = a / b
    else:
        results['quotient'] = None  # or you could use float('inf') to indicate infinity

    return results

result = arithmetic_ops(20, 1)
print(result) 



def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    pass

# Initialize a dictionary to store results of logical operations
    results = {
        'and': x and y,    
        'or': x or y,        
        'not_x': not x,      
        
    }
    return results
result = logical_ops(True, False)
print(result)  

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    pass
# bitwise operations
    results = {
        'and': a & b,            # Bitwise and
        'or': a | b,             # Bitwise or
        'xor': a ^ b,            # Bitwise xor
    }
    return results

result = bitwise_ops(10, 5)  
print(result)