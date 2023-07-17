import numpy as np
import pyaudio
import struct
import time

class AudioStream(object):
    def __init__(self):
        self.CHUNK=1024*2
        self.FORMAT=pyaudio.paInt16
        self.CHANNELS=1
        self.RATE=48000
        self.pause = False

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )

        self.detected_notes = []

    def start_plot(self):
        print('Stream started')
        frame_count=0
        start_time=time.time()

        while not self.pause:
            data=self.stream.read(self.CHUNK)
            data_int=np.frombuffer(data, dtype='h')
            f_vec = self.RATE*np.arange(self.CHUNK/2)/self.CHUNK
            mic_low_freq=40
            low_freq_loc = np.argmin(np.abs(f_vec-mic_low_freq))
            fft_data=(np.abs(np.fft.fft(data_int))[0:int(np.floor(self.CHUNK/2))])/self.CHUNK
            max_loc = np.argmax(fft_data[low_freq_loc:])+low_freq_loc

            if 980 <= f_vec[max_loc] <=990:
                self.detected_notes.append("B5")
                print("B5")
            if 865 <= f_vec[max_loc] <=895:
                self.detected_notes.append("A5")
                print("A5")
            if 775 <= f_vec[max_loc] <=800:
                self.detected_notes.append("G5")
                print("G5")
            if 690 <= f_vec[max_loc] <=710:
                self.detected_notes.append("F5")
                print("F5")
            if 650 <= f_vec[max_loc] <=670:
                self.detected_notes.append("E5")
                print("E5")
            if 585 <= f_vec[max_loc] <=595:
                self.detected_notes.append("D5")
                print("D5")
            if 515 <= f_vec[max_loc] <=550:
                self.detected_notes.append("C5")
                print("C5")
            if 490 <= f_vec[max_loc] <=500:
                self.detected_notes.append("B4")
                print("B4")
            if 437 <= f_vec[max_loc] <=390:
                self.detected_notes.append("A4")
                print("A4")
            if 390 <= f_vec[max_loc] <=400:
                self.detected_notes.append("G4")
                print("G4")
            if 345 <= f_vec[max_loc] <=355:
                self.detected_notes.append("F4")
                print("F4")
            if 325 <= f_vec[max_loc] <=335:
                self.detected_notes.append("E4")
                print("E4")
            if 290 <= f_vec[max_loc] <=300:
                self.detected_notes.append("D4")
                print("D4")
            if 255 <= f_vec[max_loc] <=280:
                self.detected_notes.append("C4")
                print("C4")
            if 243 <= f_vec[max_loc] <=253:
                self.detected_notes.append("B3")
                print("B3")
            if 215 <= f_vec[max_loc] <=225:
                self.detected_notes.append("A3")
                print("A3")
            if 192 <= f_vec[max_loc] <=202:
                self.detected_notes.append("G3")
                print("G3")
            if 172 <= f_vec[max_loc] <=177:
                self.detected_notes.append("F3")
                print("F3")
            if 162 <= f_vec[max_loc] <=167:
                self.detected_notes.append("E3")
                print("E3")
            if 144 <= f_vec[max_loc] <=150:
                self.detected_notes.append("D3")
                print("D3")
            if 127 <= f_vec[max_loc] <=133:
                self.detected_notes.append("C3")
                print("C3")
            
            frame_count+=1

        else:
            self.fr = frame_count/(time.time() - start_time)
            print("avg frame rate = {:.0f} FPS".format(self.fr))
            self.exit_app()

    def exit_app(self):
        print('Stream closed')
        self.p.close(self.stream)

    def onClick(self, event):
        self.pause = True

if __name__ == '__main__':
    audio_stream = AudioStream()
    audio_stream.start_plot()