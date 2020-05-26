from scipy.io import wavfile

class AudioFile:
    def __init__(self, path):
        self.rate, self.wav = wavfile.read(path)

    def _time_to_index(self, t):
        return int(t * self.rate)

    def interval(self, start, end):
        return self.wav[self._time_to_index(start):self._time_to_index(end)]

    def display(self, wav, **kwargs):
        from IPython.display import Audio
        return Audio(wav, rate=self.rate, **kwargs)

    def write(self, path, wav):
        return wavfile.write(path, self.rate, wav)
