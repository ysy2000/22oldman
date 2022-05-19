import wave

def get_duration(file_path):
    audio = wave.open(file_path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames / float(rate)
    return duration
