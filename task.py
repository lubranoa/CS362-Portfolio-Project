# A program by Noah Calhoun, Alex Lubrano, and Dacin Titus
#
#

import string


def conv_num_int_helper(num_str, intBased, hexBased):
    symbols = [".", "-"]
    failure = False
    negFound = 0
    for i in range(len(num_str)):
        # Handle base10 num
        num = num_str[i]
        # Check if not a number nor symbol
        if not num.isnumeric() and num not in symbols:
            failure = None
            break
        if num == "-":
            if negFound > 1:
                failure = True
                break
            else:
                negFound += 1
    if intBased:
        return failure, negFound


def conv_num_str_to_int(num_str, negFound):
    result = 0
    deciFound = 0
    deciLoc = 0
    for char in num_str:
        if char == '.':
            deciFound = True
            # continue
        elif char == '-':
            continue
        else:
            digit = ord(char) - ord('0')
            if deciFound:
                deciLoc += 1
                result += digit / (10 ** deciLoc)
            else:
                result = result * 10 + digit
    if negFound:
        result *= -1

    return result


def conv_num_hex_helper(num_str):
    failure = False
    result = 0
    place = len(num_str) - 1
    allowedAlph = ["0", "1", "2", "3", "4",
                   "5", "6", "7", "8", "9",
                   "A", "B", "C", "D", "E", "F"]
    for i in range(len(num_str)):
        num = num_str[i]
        if i == 1 or i == 0:
            place -= 1
            continue
        if num not in allowedAlph:
            failure = True
            break
        else:
            value = allowedAlph.index(num)
            result += value * (16 ** place)
            place -= 1

    return failure, result


def conv_num(num_str):
    """
    This function takes in a string
    and converts it into a base 10 number, and returns it.
    """
    hexBased = False
    intBased = False
    negFound = 0

    if num_str[0] == "0" and len(num_str) > 1 and num_str[1] == "x":
        hexBased = True
        failure, hexValue = conv_num_hex_helper(num_str)
    else:
        intBased = True
        failure, negFound = conv_num_int_helper(num_str, intBased, hexBased)
    if failure is True:
        return None
    # convert string to number for base10 string
    if intBased:
        return conv_num_str_to_int(num_str, negFound)

    if hexBased:
        return hexValue


def conv_endian(num, endian='big'):
    """Converts an integer from base 10 to a hexadecimal string in
    either big or little endian byte order. Returns None if value for
    endian is incorrect.

    :param int num: A negative or positive integer
    :param str endian: A byte order, 'big' or 'little', defaults to 'big'
    :return: The converted hex number string in specified byte order
    :rtype: string or None
    """

    hex_str = string.digits + string.ascii_uppercase[0:6]  # '0123456789ABCDEF'
    char_stack = []
    out_str = ''

    # Get hex digit char and append to modulo_list
    if num == 0:
        char_stack.append(hex_str[num])

    while num != 0:
        modulo = num % 16
        char_stack.append(hex_str[modulo])
        num //= 16

    # Construct string
    if len(char_stack) % 2 != 0:
        out_str += '0'

    while len(char_stack) != 0:
        out_str += char_stack.pop()

    return out_str
