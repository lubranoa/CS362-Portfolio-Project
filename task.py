# A program by Noah Calhoun, Alex Lubrano, and Dacin Titus
#
#

def conv_num_int_helper(num_str):
    """
    Parses through string to verify integrity
    and check if value is negative.
    """
    symbols = [".", "-"]
    neg_found = 0
    for i in range(len(num_str)):
        # Handle base10 num
        num = num_str[i]
        # Check if not a number nor symbol
        if not num.isnumeric() and num not in symbols:
            return None
        if num == "-":
            if neg_found >= 1:
                return None
            else:
                neg_found += 1
    int_value = conv_num_str_to_int(num_str, neg_found)
    return int_value


def conv_num_str_to_int(num_str, neg_found):
    """
    Converts and returns a Base10 string
    as a base10 int
    """
    result = 0
    deci_found = 0
    deci_location = 0
    for char in num_str:
        if char == '.':
            deci_found = True
        elif char == '-':
            continue
        else:
            digit = ord(char) - ord('0')
            if deci_found:
                deci_location += 1
                result += digit / (10 ** deci_location)
            else:
                result = result * 10 + digit
    if neg_found:
        result *= -1

    return result


def conv_num_hex_helper(num_str):
    """
    Takes in a base16 string,
    Returns a base10 int
    """
    result = 0
    hex_index = len(num_str) - 1
    allowed_alph = ["0", "1", "2", "3", "4",
                    "5", "6", "7", "8", "9",
                    "A", "B", "C", "D", "E", "F"]
    # Iterate through string to convert
    #   base16 string to base10 int
    for i in range(len(num_str)):
        num = num_str[i]
        if i == 1 or i == 0:        # ignore 0x values in hex
            hex_index -= 1
            continue
        if num not in allowed_alph:
            return None
        # Convert hex vlaue to base10, add to total, and decrement hex_index
        else:
            value = allowed_alph.index(num)
            result += value * (16 ** hex_index)
            hex_index -= 1

    return result


def conv_num(num_str):
    """
    This function takes in a string, parses it for base10 or base16 input,
    then converts and returns it as a base 10 int.
    """
    hex_based = False
    int_based = False

    # Check if input is base16 or base10
    if num_str[0] == "0" and len(num_str) > 1 and num_str[1] == "x":
        hex_based = True
        hex_value = conv_num_hex_helper(num_str)
    else:
        int_based = True
        int_value = conv_num_int_helper(num_str)

    # Return None if hex or int conversion failed
    if hex_based and hex_value is None:
        return None
    if int_based and int_value is None:
        return None

    # Return converted values
    if int_based:
        return int_value
    elif hex_based:
        return hex_value
    else:
        return None
