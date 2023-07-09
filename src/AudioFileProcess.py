import pyaudio
import wave
import numpy as np
import struct

def RecordAudio(filename):
    '''
    Records audio for a specified duration and saves it to a WAV file.
    Args:
        filename (str): The name of the WAV file to save the recorded audio.
    Returns:
        None
    '''
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100  # frames per channel
    seconds = 10 # Record 10s
    p = pyaudio.PyAudio()
    print("Recording ...")
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    frames = []
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("... Ending Recording")
    # Convert audio data to a numpy array
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    # Amplify the amplitudes of the audio data
    amplification_factor = 4.0
    amplified_audio_data = (audio_data * amplification_factor).astype(np.int16)
    # Save the audio data with amplified amplitudes to a file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(amplified_audio_data.tobytes())
        wf.close()
    print("Recording saved with amplified audio.")


def getSamplesFromAudio(filename):
    '''
    Retrieves audio samples from a WAV file.
    Args:
        filename (str): The name of the WAV file.
    Returns:
        list: A list of audio samples as integers.
    '''
    # Mở file .wav
    with wave.open(filename, 'rb') as wav_file:
        # Get information about the .wav file
        sample_width = wav_file.getsampwidth()  # Number of bytes per audio sample
        num_channels = wav_file.getnchannels()  # Number of audio channels (mono: 1, stereo: 2)
        frame_rate = wav_file.getframerate()    # Sample rate (number of audio samples per second)
        # Read the audio data from the .wav file
        frames = wav_file.readframes(wav_file.getnframes())
    # Convert the audio data from bytes to integers
    if sample_width == 2:
        # For 16-bit audio
        samples = [int.from_bytes(frames[i:i+sample_width], byteorder='little', signed=True) for i in range(0, len(frames), sample_width)]
    else:
        return []
    return samples


def convertSamplesToAudio(samples, filename):
    '''
    Converts audio samples to a WAV file.
    Args:
        samples (list): A list of audio samples as integers.
        filename (str): The name of the output WAV file.
    Returns:
        None
    '''
    # Audio information
    sample_width = 2           # Number of bytes per audio sample (16-bit = 2 bytes)
    num_channels = 1           # Number of audio channels (mono: 1, stereo: 2)
    frame_rate = 44100         # Sample rate (number of audio samples per second)
    # Create a wave writer object
    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)          # Set the number of channels
        wav_file.setsampwidth(sample_width)          # Set the number of bytes per sample
        wav_file.setframerate(frame_rate)            # Set the sample rate
        # Convert audio samples to bytes and write to the .wav file
        for sample in samples:
            # Convert audio sample to bytes
            wav_file.writeframes(struct.pack('<h', sample))