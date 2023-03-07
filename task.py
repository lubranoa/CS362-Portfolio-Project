# A program by Noah Calhoun, Alex Lubrano, and Dacin Titus
#
#


def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number, and returns it."""
    periodFound = 0
    hexValue = False
    intValue = False
    symbols = [".", "-"]
    # numbers = [0,1,2,3,4,5,6,7,8,9]
    negFound = 0
    deciFound = 0
    deciLoc = 0

    if num_str[0] == "0" and len(num_str) > 1 and num_str[1] == "x":
        hexValue = True
    else:
        intValue = True

    for i in range(len(num_str)):
        # Handle base10 num
        if intValue:
            num = num_str[i]
            if periodFound > 1:     # check if multiple . found
                return None
            if num == ".":
                periodFound += 1
            # Check if not a number nor symbol
            if not num.isnumeric() and num not in symbols:
                return None

            if num == "-":
                if negFound > 1:
                    return None
                else:
                    negFound += 1

        # Handle hex num
        elif hexValue:
            return num_str

        else:
            return None

    # convert string to number for base10 string
    if intValue:
        result = 0
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

    if hexValue:
        return num_str
