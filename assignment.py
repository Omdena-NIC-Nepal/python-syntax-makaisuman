def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    
    return f"My name is {name} and I am {age} years old" 

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sumOfNumber = 0
    for i in range(1, n + 1):
        sumOfNumber= sumOfNumber + i
    return sumOfNumber

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    # Initialize sum, max, and min
    sumOfNumber = 0
    max_value = numbers[0]
    min_value = numbers[0]
    
    # Loop through the list to calculate sum, max, and min
    for num in numbers:
        # Calculate the sum
        sumOfNumber = sumOfNumber + num
        
        # Update max_value if current number is greater
        if num > max_value:
            max_value = num
        
        # Update min_value if current number is smaller
        if num < min_value:
            min_value = num
    
    return sumOfNumber, max_value, min_value

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    above_80_students = []
    
    # Loop through the dictionary
    for student, score in students_dict.items():
        if score > 80:
            above_80_students.append(student)
    
    return above_80_students

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    #converting list to sets    
    set1= set(list1)
    set2= set(list2)
    #finding common elements
    common_elements = set1.intersection(set2)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b if b != 0 else None,
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return{
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b,
    }