# A program by Noah Calhoun, Alex Lubrano, and Dacin Titus
#
#

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
