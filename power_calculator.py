import math
import sys

def to_int(user_input: str) -> int:
    try:
        return int(user_input)
    except:
        print('Invalid exponent input.')
        sys.exit(1)

def to_float(user_input: str) -> float:
    val = user_input.strip().lower()

    constants = {
        'e': math.e,
        'pi': math.pi,
        'tau': math.tau,
        'inf': float('inf'),
        'infinity': float('inf'),
        '-inf': float('-inf'),
        '-infinity': float('-inf'),
        'nan': float('nan')
    }
    try:
        if val in constants:
            return constants[val]
        return float(user_input)
    except:
        print('Invalid number input.')
        sys.exit(1)

def power(n: float, e: int) -> float:
    result = 1.0
    if e == 0:
        return result
    abs_exponent = abs(e)
    for _ in range(abs_exponent):
        result *= n
    return result if 0 < e else 1 / result

def main():
    number = input('Enter number: ')
    exponent = input('Enter exponent: ')
    pow = power(to_float(number), to_int(exponent))
    print(f'Result: {pow}')
    print(f'Compare: {to_float(number) ** to_int(exponent)}')

if __name__ == "__main__":
    main()
