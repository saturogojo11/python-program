def determine_type(input_value):
    try:
        int(input_value)
        return "Integer"
    except ValueError:
        pass

    try:
        float(input_value)
        return "Float"
    except ValueError:
        pass

    if isinstance(input_value, str):
        return "String"
    elif isinstance(input_value, list):
        return "List"
    elif isinstance(input_value, tuple):
        return "Tuple"
    elif isinstance(input_value, dict):
        return "Dictionary"
    elif isinstance(input_value, bool):
        return "Boolean"
    elif input_value is None:
        return "None"
    else:
        return "Unknown"

input_value = input("Enter a value: ")
print(f"The type of the input is: {determine_type(input_value)}")