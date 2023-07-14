import matplotlib.pyplot as plt #Para las gráficas
import numpy as np #para los cálculos
import pyaudio #para acceder al mic
import struct #para manipular los datos de audio
import sys #para interactuar con el sistema
import time #para medir el tiempo

class AudioStream(object):
    def __init__(self): #constructor de la clase
        self.CHUNK=1024*2 #tamaño de los fragmentos
        self.FORMAT=pyaudio.paInt16
        self.CHANNELS=1
        self.RATE=48000 #FS 
        self.pause = False

        #Para capturar el audio
        self.p = pyaudio.PyAudio() #creación de instancia de audio
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK,
        )
        self.detected_notes = [] #para almacenar las notas
        self.init_plots() #ventana para graficas
        self.start_plot() #valores en graficas

        #Para almacenar las notas
        self.detected_notes = []

    #Para las gráficas
    def init_plots(self):
        x = np.arange(0,2*self.CHUNK,2) #tiempo
        xf = np.linspace(0,self.RATE, self.CHUNK) #frecuencia

        self.fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick) #salir al hacer click

        #Mientras no se recibe nada (para que el programa continue)
        self.line, = ax1.plot(x, np.random.rand(self.CHUNK), linestyle='-', linewidth=2)
        self.line2, = ax1.plot(xf, np.random.rand(self.CHUNK), linestyle='-', linewidth=2)
        self.line_fft, = ax2.plot(xf, np.random.rand(self.CHUNK), linestyle='-', linewidth=2)

        #self.line = ax1.plot(x,np.random.rand(self.CHUNK, '-', 1w=2)) #REVISAR ESTA Y LA DE ABAJO
        #self.line = ax2.plot(xf,np.random.rand(self.CHUNK, '-', 1w=2))

        #limites de la gráfica
        #en tiempo
        ax1.set_title('Audio (tiempo)')
        ax1.set_ylabel('Vol')
        ax1.set_ylim(-10000,10000)
        ax1.set_xlim(0,2*self.CHUNK)
        plt.setp(
            ax1, yticks=[10],
            xticks=[0, self.CHUNK, 2*self.CHUNK], #valores marcados en la gráfica
        )
        #en frecuencia
        ax2.set_title('Audio en frecuencia')
        ax2.set_xlabel('Frecuencia')
        ax2.set_ylabel('Amplitud')
        ax2.set_xlim(20, self.RATE / 12)
        plt.setp(
            ax2, yticks=[0,5,10,15,20],
                 xticks=[0,100,200,300,1000,3000,4000]
        )

        #Ventana
        mngr = plt.get_current_fig_manager()
        #mngr.window.setGeometry_(5, 120, 1910, 1070)
        mngr.resize(1910, 1070)
        plt.show(block=False)

#Graficas en tiempo real y procesamiento de audio
    def start_plot(self):
        print('Stream started')
        frame_count=0
        start_time=time.time()

        while not self.pause:
            #valores del mic
            data=self.stream.read(self.CHUNK)

            #los pasamos a int para poder graficar
            data_int=np.frombuffer(data, dtype='h')

            #los ponemos en un array
            data_np = np.array(data_int,dtype='h')

            #graficamos
            self.line.set_ydata(data_np)

            #FFT
            yf=np.fft.fft(data_int)
            #graficamos
            self.line_fft.set_ydata(
                np.abs(yf[0:self.CHUNK])/(128*self.CHUNK)
            )

            #identificamos picos de frecuencia
            f_vec = self.RATE*np.arange(self.CHUNK/2)/self.CHUNK #Vector de frecuencia
            mic_low_freq=40 #min que va a detectar el mic
            low_freq_loc = np.argmin(np.abs(f_vec-mic_low_freq)) #absoluto por si la resta llegara a reultar en negativo
            fft_data=(np.abs(np.fft.fft(data_int))[0:int(np.floor(self.CHUNK/2))])/self.CHUNK

            #para la mayor frecuencia
            max_loc = np.argmax(fft_data[low_freq_loc:])+low_freq_loc #a qué frecuencia corresponde la máxima amplitud

            #Detección de nota musical
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
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()
            frame_count+=1
        else:
            self.fr = frame_count/(time.time() - start_time)
            print("avg frame rate = {:.0f FPS".format(self.fr))
            self.exit_app()

    def exit_app(self):
        print('stream closed')
        self.p.close(self.stream)

    def onClick(self, event): # para terminar el programa al hacer click
        self.pause = True

if __name__ == '__main__':
    AudioStream()