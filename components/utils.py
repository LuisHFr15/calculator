def is_valid_number(string: str) -> bool:
    if string == '0':
        return False
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def is_empty(string: str) -> bool:
    return len(string) == 0