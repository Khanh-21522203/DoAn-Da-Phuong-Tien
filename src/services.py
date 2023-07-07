def Quantizier(number, stepsize=4, max=127, min=-128):
    '''
    Quantizes a given number using a specified step size within a given range.
    Args:
        number (float): The number to be quantized.
        stepsize (float, optional): The step size used for quantization. Defaults to 4.
        max (float, optional): The maximum value allowed for the quantized number. Defaults to 127.
        min (float, optional): The minimum value allowed for the quantized number. Defaults to -128.
    Returns:
        float: The quantized number within the specified range.
    '''
    temp = round(number/stepsize)
    if temp > max:
        temp = max
    if temp < min:
        temp = min
    return temp

def DeQuantizier(number, stepsize=4):
    '''
    Dequantizes a given number using a specified step size.
    Args:
        number (float): The quantized number to be dequantized.
        stepsize (float, optional): The step size used for dequantization. Defaults to 4.
    Returns:
        float: The dequantized number.
    '''
    return round(number*stepsize)


def ConvertToBinary(number, numBits=8):
    '''
    Converts a decimal number to its two's complement binary representation.
    Args:
        number (int): The decimal number to be converted.
        numBits (int, optional): The number of bits in the binary representation. Defaults to 8.
    Returns:
        str: The two's complement binary representation of the decimal number.
    ''' 
    if number<0:
        return '1' + bin(2**(numBits-1) + number)[2:].zfill(numBits-1)
    else:
        return '0' + bin(number)[2:].zfill(numBits-1)

def ConverToDecimal(number, numBits=8):
    '''
    Converts a two's complement binary number to its decimal representation.
    Args:
        number (str): The two's complement binary number to be converted.
        numBits (int, optional): The number of bits in the binary representation. Defaults to 8.
    Returns:
        int: The decimal representation of the two's complement binary number.
    '''
    if number[0] == '1':
        return int(number[1:], 2) - 2**(numBits-1)
    else:
        return int(number[1:], 2)