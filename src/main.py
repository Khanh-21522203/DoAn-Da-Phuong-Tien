from DPCM import *
from ADPCM import *
from AudioFileProcess import *

# Encode and Decode music
filename = './audioFiles/origin-music.wav'
# Get samples of origin music audio
samples = getSamplesFromAudio(filename)

# DPCM encode
DPCMencode = DPCMencoder(samples[10000:])   # encode from 10000th signal
# Save DPCM encoder output
with open("./binary/DPCM-music-binaryString.txt", "a") as file:
    file.write(DPCMencode)
# DPCM decoder
DPCMdecode = DPCMdecoder(DPCMencode)
# Save DPCM dencoder output to .wav file
convertSamplesToAudio(DPCMdecode, './audioFiles/DPCM-music.wav')

# ADPCM encode
ADPCMencode = ADPCMencoder(samples[10000:])   # encode from 10000th signal
# Save ADPCM encoder output
with open("./binary/ADPCM-music-binaryString.txt", "a") as file:
    file.write(ADPCMencode)
# ADPCM decoder
ADPCMdecode = ADPCMdecoder(ADPCMencode)
# Save ADPCM dencoder output to .wav file
convertSamplesToAudio(ADPCMdecode, './audioFiles/ADPCM-music.wav')


# Encode and Decode human voice
filename = './audioFiles/origin-voice.wav'
# Get samples of origin music audio
samples = getSamplesFromAudio(filename)

# DPCM encode
DPCMencode = DPCMencoder(samples[10000:])   # encode from 10000th signal
# Save DPCM encoder output
with open("./binary/DPCM-voice-binaryString.txt", "a") as file:
    file.write(DPCMencode)
# DPCM decoder
DPCMdecode = DPCMdecoder(DPCMencode)
# Save DPCM dencoder output to .wav file
convertSamplesToAudio(DPCMdecode, './audioFiles/DPCM-voice.wav')

# ADPCM encode
ADPCMencode = ADPCMencoder(samples[10000:])   # encode from 10000th signal
# Save ADPCM encoder output
with open("./binary/ADPCM-voice-binaryString.txt", "a") as file:
    file.write(ADPCMencode)
# ADPCM decoder
ADPCMdecode = ADPCMdecoder(ADPCMencode)
# Save ADPCM dencoder output to .wav file
convertSamplesToAudio(ADPCMdecode, './audioFiles/ADPCM-voice.wav')