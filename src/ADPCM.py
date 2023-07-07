from services import *
import numpy as np

def ADPCMencoder(input, numBits=8):
    '''
    Performs ADPCM encoding on a given input sequence.
    Args:
        input (list): The input sequence to be encoded.
        numBits (int, optional): The number of bits used for encoding the quantized errors. Defaults to 8.
    Returns:
        str: The binary representation of the encoded sequence.
    '''
    a = None # Adaptive coefficients
    buffer1 = [0] # Label
    buffer2 = [[0,0,1]] # feature matrix
    '''
        In formula: w =〖(X^T X)〗^(-1) X^T y
        w = a
        X = buffer2 
        y = buffer1
    ''' 
    errors = []
    for i in range(len(input)):
        # Calculate Adaptive coefficients
        if (i>50):
            X = np.array(buffer2[-50:])
            y = np.array([buffer1[-50:]]).T
        else:
            X = np.array(buffer2)
            y = np.array([buffer1]).T
        a = np.linalg.pinv(X.T @ X) @ (X.T) @ y
        # Predict next signal value
        pred = np.array([buffer2[-1]]) @ a
        pred = pred.tolist()[0][0]
        # Quantization Error
        error = input[i] - pred
        error = Quantizier(error)
        errors.append(error)
        # Update buffer
        recover = pred + DeQuantizier(error)
        buffer1.append(recover)
        buffer2.append([buffer1[-1], buffer1[-2], 1])
    output = ''.join([ConvertToBinary(i, numBits) for i in errors])
    return output

def ADPCMdecoder(input, numBits=8):
    '''
    Performs ADPCM decoding on a given input sequence.
    Args:
        input (str): The binary representation of the encoded sequence.
        numBits (int, optional): The number of bits used for encoding the quantized errors. Defaults to 8.
    Returns:
        list: The decoded output sequence.
    '''
    errors = []
    for i in range(0,len(input),numBits):
        errors.append(ConverToDecimal(input[i:i+numBits]))
    a = np.zeros((3,1)) # Adaptive coefficients
    buffer1 = [0] # Label
    buffer2 = [[0,0,1]] # feature matrix
    output = []
    '''
        In formula: w =〖(X^T X)〗^(-1) X^T y
        w = a
        X = buffer2 
        y = buffer1
    ''' 
    for i in range(len(errors)):
        # Predict next signal value
        e = DeQuantizier(errors[i],2)
        pred = (np.array([buffer2[-1]]) @ a).tolist()[0][0]+e
        output.append(round(pred))
        # Update Buffer
        buffer1.append(pred)
        buffer2.append([buffer1[-1], buffer1[-2], 1])
        # Update Adaptive coefficients
        if (i>50):
            X = np.array(buffer2[-50:])
            y = np.array([buffer1[-50:]]).T
        else:
            X = np.array(buffer2)
            y = np.array([buffer1]).T
        a = np.linalg.pinv(X.T @ X) @ (X.T) @ y
    return output