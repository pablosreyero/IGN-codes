import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt
import obspy
from obspy import read, UTCDateTime as UTC
from obspy.core import read, Stream
from obspy.clients.fdsn import Client
from seismic_attributes import seismic_attributes as sa
from obspy.signal.cross_correlation import correlation_detector
from obspy.signal.cross_correlation import correlate, _similarity_detector, correlate_stream_template

def correlacion_en_misma_estación():
    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/Swarm_data/VB.APOR..HHZ.D.2022.292")
    template.plot()
    template.filter('bandpass', freqmin=1, freqmax=20)
    template.plot()

    pick = UTC('2022-10-19T09:41:52')
    template.trim(pick, pick + 10) #lo tengo que poner en segundos
    template.plot()

    stream = read('/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/Swarm_data/VB.APOR..HHZ.D.2022.292')
    stream.filter('bandpass', freqmin=1, freqmax=20)
    height = 0.3  # similarity threshold
    distance = 10  # distance between detections in seconds
    detections, sims = correlation_detector(stream, template, height, distance, plot=stream)
    print("\n")
    for i in detections:
        print(i)

def correlacion_diferente_estación():
    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/Swarm_data/VB.APOR..HHZ.D.2022.292")
    template.plot()
    template.filter('bandpass', freqmin=1, freqmax=20)
    template.plot()

    pick = UTC('2022-10-19T11:56:46')
    template.trim(pick, pick + 4) #lo tengo que poner en segundos
    template.plot()

    stream = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/Swarm_data/VB.ATIN..HHZ.D.2022.292")
    stream.filter('bandpass', freqmin=1, freqmax=20)
    height = 0.1  # similarity threshold
    distance = 10  # distance between detections in seconds
    detections, sims = correlation_detector(stream, template, height, distance, plot=stream)
    ccs = correlate_stream_template(stream, template)
    print("\n")
    for i in detections:
        print(i)

        #TENGO QUE PROBAR CON OTRO TROZO he probado con otro troxo y nada de nada
def various_correlations():

    #Aqui se lee CART.mseed (el de las explosiones)
    stream = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/CART.mseed")
    stream.filter('bandpass', freqmin=0.5, freqmax=2)
    stream.plot()
    stream.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTExplosiones.png')
    print(stream[0])
    #Aqui se lee CART.mseed (el del terremoto)
    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/CART10horas.mseed")
    template.plot()
    template.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTTerremoto.png')
    print(template[0])
    print(template[0].stats.starttime + 37*60,template[0].stats.starttime + 38*60)
    #Ahora modificamos nuestro datos.plot para recortar el eje temporal y quedarnos solo con el terremoto
    template.trim(template[0].stats.starttime + 37*60, template[0].stats.starttime + 38*60) #11:19-- 11:21 para coger el terremoto de las 11:20:50
    print(template[0])
    template.plot()

    stream2 = stream.copy()
    stream2.filter('bandpass', freqmin=0.5, freqmax=2)
    pick1 = UTC('2022-10-19T08:47:10.998393Z')
    pick2 = UTC('2022-10-19T08:47:30.998393Z')
    stream2.trim(pick1,pick2)

    #Aqui recortamos la señal.
    #pick = UTC('2022-10-19T11:56:46')
    #stream.trim(pick, pick + 4) #lo tengo que poner en segundos
    #stream.plot()
    height = 0.3
    distance = 1
    detections, sims = correlation_detector(stream, stream2, height, distance, plot=stream)


def definitivo():

    stream = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/CART.mseed")
    stream.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTExplosionesSinFiltrar.png')
    stream.spectrogram()
    stream.filter('bandpass', freqmin=0.5, freqmax=2)
    stream.plot()
    stream.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTExplosionesFiltrado.png')
    #stream.spectrogram(log=True, title='Espectrograma explosiones CART ' + '08:00-09:00', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/espectrogramaVOLADURASCART.png')
    print(stream[0])

    #Aqui se lee CART.mseed (el del terremoto)
    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/CART10horas.mseed")
    template.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTTerremotoSinFiltrar.png')
    template.filter('bandpass', freqmin=0.5, freqmax=2)
    template.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTTerremotoFiltrado.png')
    template.plot()
    t_start = UTC('2022-10-19T10:37:20.998393Z')
    t_stop = UTC('2022-10-19T10:38:00.998393Z')
    template.trim(t_start,t_stop)
    template.spectrogram(log=True, title='Espectrograma terremoto CART ' + '10:37', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/espectrogramaTERREMOTOCART.png')

    """
    stream2 = stream.copy()
    stream2.filter('bandpass', freqmin=0.5, freqmax=2)
    pick1 = UTC('2022-10-19T08:47:10.998393Z')
    pick2 = UTC('2022-10-19T08:47:30.998393Z')
    stream2.trim(pick1,pick2)
    """

    #Aqui recortamos la señal.
    #pick = UTC('2022-10-19T11:56:46')
    #stream.trim(pick, pick + 4) #lo tengo que poner en segundos
    #stream.plot()
    height = 0.15
    distance = 1
    detections, sims = correlation_detector(stream, template, height, distance, plot=stream)

def definitivoTerremotos():

    stream = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15Marzo/EMLI.mseed")
    stream.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/EMLITerremotosSinFiltrar.png')
    stream.spectrogram()
    stream.filter('bandpass', freqmin=0.5, freqmax=2)
    stream.plot()
    stream.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/EMLITerremotosFiltrados.png')
    #stream.spectrogram(log=True, title='Espectrograma explosiones CART ' + '08:00-09:00', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/espectrogramaVOLADURASCART.png')
    print(stream[0])

    #Aqui se lee CART.mseed (el del terremoto)
    
    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/CART10horas.mseed")
    template.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTTerremotoSinFiltrar.png')
    template.filter('bandpass', freqmin=0.5, freqmax=2)
    template.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/CARTTerremotoFiltrado.png')
    template.plot()
    t_start = UTC('2022-10-19T10:37:20.998393Z')
    t_stop = UTC('2022-10-19T10:38:00.998393Z')
    template.trim(t_start,t_stop)
    template.spectrogram(log=True, title='Espectrograma terremoto CART ' + '10:37', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesCorrelaciones/espectrogramaTERREMOTOCART.png')

    """
    stream2 = stream.copy()
    stream2.filter('bandpass', freqmin=0.5, freqmax=2)
    pick1 = UTC('2022-10-19T08:47:10.998393Z')
    pick2 = UTC('2022-10-19T08:47:30.998393Z')
    stream2.trim(pick1,pick2)
    """

    #Aqui recortamos la señal.
    #pick = UTC('2022-10-19T11:56:46')
    #stream.trim(pick, pick + 4) #lo tengo que poner en segundos
    #stream.plot()
    height = 0.25
    distance = 1
    detections, sims = correlation_detector(stream, template, height, distance, plot=stream)

def correlacionAmano():
    stream = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15Marzo/EMLI.mseed")

    template = read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/CART10horas.mseed")
    t_start = UTC('2022-10-19T10:37:20.998393Z')
    t_stop = UTC('2022-10-19T10:38:00.998393Z')
    #template.trim(t_start,t_stop)

    #Ahora convertimos las señales oBspy en arrays numpy 
    stream2 = np.array(stream)
    template2 = np.array(template)

    print(len(stream2),len(template2))
    print(stream2)
    print(template2)
    # Pre-allocate correlation array
    corr = (len(stream2) - len(template2) + 1) * [0]

    # Go through lag components one-by-one
    for l in range(len(corr)):
        corr[l] = sum([stream2[i+l] * template2[i] for i in range(len(template2))])

    print('Esta es la correlación final: ', corr)

    correlacion = np.correlate(stream2, template2)
    print('Esta es la correlación final con numPy: ', correlacion)
    


#correlacion_en_misma_estación()
#correlacion_diferente_estación()
#various_correlations()
#definitivo()
#definitivoTerremotos()
correlacionAmano()