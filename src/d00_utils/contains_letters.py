import re
import argparse

def contains_letters(value):
    return bool(re.match(r'^\d+$', value))


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('value', type=str, help='Value to check')

    args = parser.parse_args()
    value = args.value
    result = contains_letters(value)
    
    if result:
        print(f"'{value}' contains only digits.")
    else:
        print(f"'{value}' not contains only digits")   
