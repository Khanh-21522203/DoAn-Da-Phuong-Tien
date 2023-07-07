from services import *

def DPCMencoder(input, numBits=8):
    '''
    Performs DPCM encoding on a given input sequence.
    Args:
        input (list): The input sequence to be encoded.
        numBits (int, optional): The number of bits used for encoding the quantized errors. Defaults to 8.
    Returns:
        str: The binary representation of the encoded sequence.
    '''
    errors = []
    pred = 0
    for f in input:
        # Calculate and quantizier error
        error = f - pred
        error = Quantizier(error)
        errors.append(error)
        # Recover singal
        pred += DeQuantizier(error)
    # Convert errors to Binary
    output = ''.join([ConvertToBinary(i, numBits) for i in errors])
    return output

def DPCMdecoder(input, numBits=8):
    '''
    Performs DPCM decoding on a given input sequence.
    Args:
        input (str): The binary representation of the encoded sequence.
        numBits (int, optional): The number of bits used for encoding the quantized errors. Defaults to 8.
    Returns:
        list: The decoded output sequence.
    '''
    errors = []
    # Convert to Decimal
    for i in range(0,len(input),numBits):
        errors.append(ConverToDecimal(input[i:i+numBits]))
    pred = 0
    output = []
    for e in errors:
        # Recover signal
        pred = pred + DeQuantizier(e)
        output.append(pred)
    return output