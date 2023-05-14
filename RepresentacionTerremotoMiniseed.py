import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt
import obspy
from obspy.core import read, Stream
from obspy.clients.fdsn import Client
from seismic_attributes import seismic_attributes as sa
import pylatex as latex

def lecturaCART10Horas():

    datos = obspy.read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/CART10horas.mseed")
    datos2 = datos.copy()
    datos3 = datos.copy()
    datos4 = datos.copy()
    new_array = np.array(datos)

    print(datos[0])
    datos.plot()
    #Aqui se plotea la magntiud en el tiempo 
    datos.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/TerremotoCartagena/terremotoCartagenaTotal.png')
    #Aqui se plotea el "One-day plot" AKA: helicorder
    #datos.plot(type='dayplot',outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesTerremotoMelilla/helicorder.png')

    print(datos3[0].stats.starttime + 37*60,datos2[0].stats.starttime + 38*60)

    #Ahora modificamos nuestro datos.plot para recortar el eje temporal y quedarnos solo con el terremoto (madrugada)
    datos3.trim(datos3[0].stats.starttime + 37*60, datos2[0].stats.starttime + 38*60) #11:19-- 11:21 para coger el terremoto de las 11:20:50
    print(datos3[0].stats.starttime)
    print(datos3[0].stats.endtime)
    print(datos3[0])
    datos3.plot()

    datos3.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/TerremotoCartagena/sentemporalCortadaTerremotoCART.png')

    #Ahora filtramos la señal original:
    filtered_signal1 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 16, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)
    filtered_signal2 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 16, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)

    #Ahora filtramos los dos terremotos por separado
    terremoto_filtrado1 = obspy.signal.filter.bandpass(datos3[0], freqmin = 4, freqmax = 16, df = datos3[0].stats.sampling_rate ,corners = 4, zerophase = False)
    terremoto_filtrado2 = obspy.signal.filter.bandpass(datos2[0], freqmin = 4, freqmax = 16, df = datos2[0].stats.sampling_rate ,corners = 4, zerophase = False)

    datos2.trim(datos[0].stats.starttime + 47*60, datos[0].stats.starttime + 49*60)
    datos2.spectrogram(log=True, title='Espectrograma Terremoto CART' + '10:37', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/TerremotoCartagena/espectrogramaTERREMOTOCART.png')



def PrimeraLectura():

    datos = obspy.read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/CART.mseed")
    datos2 = datos.copy()
    datos3 = datos.copy()
    datos4 = datos.copy()
    new_array = np.array(datos)

    print(datos[0])
    datos.plot()
    #Aqui se plotea la magntiud en el tiempo 
    datos.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/voladurasCartagena/sentemporal.png')
    #Aqui se plotea el "One-day plot" AKA: helicorder
    #datos.plot(type='dayplot',outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesTerremotoMelilla/helicorder.png')

    print(datos3[0].stats.starttime + 47*60,datos2[0].stats.starttime + 49*60)

    #Ahora modificamos nuestro datos.plot para recortar el eje temporal y quedarnos solo con el terremoto (madrugada)
    datos3.trim(datos3[0].stats.starttime + 47*60, datos2[0].stats.starttime + 49*60) #11:19-- 11:21 para coger el terremoto de las 11:20:50
    print(datos3[0].stats.starttime)
    print(datos3[0].stats.endtime)
    print(datos3[0])
    datos3.plot()

    datos3.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/voladurasCartagena/sentemporalCortada.png')

    #Ahora filtramos la señal original:
    filtered_signal1 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 16, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)
    filtered_signal2 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 16, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)

    #Ahora filtramos los dos terremotos por separado
    terremoto_filtrado1 = obspy.signal.filter.bandpass(datos3[0], freqmin = 4, freqmax = 16, df = datos3[0].stats.sampling_rate ,corners = 4, zerophase = False)
    terremoto_filtrado2 = obspy.signal.filter.bandpass(datos2[0], freqmin = 4, freqmax = 16, df = datos2[0].stats.sampling_rate ,corners = 4, zerophase = False)

    datos2.trim(datos[0].stats.starttime + 47*60, datos[0].stats.starttime + 49*60)
    datos2.spectrogram(log=True, title='Espectrograma VOLADURA' + '08:47', outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/voladurasCartagena/espectrogramaVOLADURA.png')

    plt.subplot(211)
    plt.plot(datos[0].times("matplotlib"), datos[0].data, "b-")
    plt.title("Señal original")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")

    plt.subplot(212)
    plt.plot(filtered_signal2, "b-")
    plt.title("Señal después del BPF")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show()


    datos.resample(100.0)
    #datos3.resample(100.0)

    #Ahora dibujamos el spcegram en un subplot
    plt.subplot(211)
    plt.specgram(datos[0], Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram de la señal original")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")

    plt.subplot(212)
    plt.specgram(filtered_signal2, Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram de la señal original filtrada")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show() 
    print(datos[0])
    print(filtered_signal2)
    #Ahora ploteamos el specgram de los dos terremotos
    plt.subplot(211)
    plt.specgram(datos3[0], Fs=datos3[0].stats.sampling_rate)
    plt.title("Specgram del terremoto original")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")

    plt.subplot(212)
    plt.specgram(terremoto_filtrado1, Fs=datos3[0].stats.sampling_rate)
    plt.title("Specgram del terremoto filtrado")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show() 

def SegundaLectura():


    datos = obspy.read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15Marzo/EMLI.mseed")
    datos2 = datos.copy()
    datos3 = datos.copy()
    datos4 = datos.copy()
    new_array = np.array(datos)

    print(datos[0])
    datos.plot()
    #Aqui se plotea la magntiud en el tiempo 
    datos.plot(outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesTerremotoMelilla/sentemporal.png')
    #Aqui se plotea el "One-day plot" AKA: helicorder
    #datos.plot(type='dayplot',outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesInformeFinal/ImagenesTerremotoMelilla/helicorder.png')

    print(datos3[0].stats.starttime + ((11 * 60) + 19)*60,datos2[0].stats.starttime + ((11 * 60) + 21)*60)

    #Ahora modificamos nuestro datos.plot para recortar el eje temporal y quedarnos solo con el terremoto (madrugada)
    datos3.trim(datos3[0].stats.starttime + 19*60, datos2[0].stats.starttime + 21*60) #11:19-- 11:21 para coger el terremoto de las 11:20:50
    print(datos3[0].stats.starttime)
    print(datos3[0].stats.endtime)
    print(datos3[0])
    datos3.plot()

    #Ahora modificamos nuestro datos.plot para recortar el eje temporal y quedarnos solo con el terremoto (mediodia)
    datos2.trim(datos2[0].stats.starttime + 0 * 60, datos2[0].stats.starttime + 1 * 60)
    datos2.plot() #pasar todo a segundos, si el terremoto esta en 22:36 horas pasamos 22 horas a minutos + 36 minutos y todo esto ((22*60)+36)*60


    #Aqui ploteamos con matplotlib
    fig = plt.figure(1)
    ax = fig.add_subplot(121)
    ax.plot(datos[0].times("matplotlib"), datos[0].data, "b-")
    ax.xaxis_date()
    fig.autofmt_xdate()

    fig2 = plt.figure(2)
    ax2 = fig.add_subplot(122)
    ax2.plot(obspy.signal.filter.bandpass(datos[0], freqmin = 2, freqmax = 8, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False), "b-")
    ax2.xaxis_date()
    fig2.autofmt_xdate()


    #Ahora filtramos la señal original:
    filtered_signal1 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 8, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)
    filtered_signal2 = obspy.signal.filter.bandpass(datos[0], freqmin = 4, freqmax = 8, df = datos[0].stats.sampling_rate ,corners = 4, zerophase = False)

    #Ahora filtramos los dos terremotos por separado
    terremoto_filtrado1 = obspy.signal.filter.bandpass(datos3[0], freqmin = 4, freqmax = 8, df = datos3[0].stats.sampling_rate ,corners = 4, zerophase = False)
    terremoto_filtrado2 = obspy.signal.filter.bandpass(datos2[0], freqmin = 4, freqmax = 8, df = datos2[0].stats.sampling_rate ,corners = 4, zerophase = False)


    plt.subplot(211)
    plt.plot(datos[0].times("matplotlib"), datos[0].data, "b-")
    plt.title("Señal original")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")

    plt.subplot(212)
    plt.plot(filtered_signal2, "b-")
    plt.title("Señal después del BPF")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show()

    #Ahora ploteamos la señal entera junto al terremoto y a su replica
    plt.subplot(311)
    plt.plot(datos[0].times("matplotlib"), datos[0].data, "b-")
    plt.title("Señal original")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")

    plt.subplot(312)
    plt.plot(datos2[0].times("matplotlib"), datos2[0].data, "b-")
    plt.title("Señal del TERREMOTO (mediodia)")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.subplot(313)
    plt.plot(datos3[0].times("matplotlib"), datos3[0].data, "b-")
    plt.title("Señal del TERREMOTO (madrugada)")
    plt.xlabel("tiempo")
    plt.ylabel("Amplitud")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show()

    datos.resample(10.0)

    print(datos3[0])
    datos.spectrogram(log=True, title='Espectrograma TOTAL' + str(datos3[0].stats.starttime), outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesGuardadas/espectrogramaGENERAL.png')

    #Ahora pintamos el espectrograma del trozo del terremoto, para ello cogemos solo la parte del terremoto
    datos2.spectrogram(log=True, title='Espectrograma TERREMOTO' + str(datos2[0].stats.starttime), outfile = '/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/ImagenesGuardadas/espectrogramaTERREMOTO.png')


    #Ahora dibujamos el spcegram en un subplot
    plt.subplot(211)
    plt.specgram(datos[0], Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram de la señal original")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")

    plt.subplot(212)
    plt.specgram(filtered_signal2, Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram de la señal original filtrada")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show() 

    #Ahora ploteamos el specgram de los dos terremotos
    plt.subplot(211)
    plt.specgram(datos3[0], Fs=datos3[0].stats.sampling_rate)
    plt.title("Specgram del terremoto original")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")

    plt.subplot(212)
    plt.specgram(terremoto_filtrado1, Fs=datos2[0].stats.sampling_rate)
    plt.title("Specgram del terremoto filtrado")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show() 

    #Ahora ploteamos el especgram de los dos terremotos, pero esta vez filtrados
    plt.subplot(211)
    plt.specgram(terremoto_filtrado1, Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram del terremoto (madrugada)")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")

    plt.subplot(212)
    plt.specgram(terremoto_filtrado2, Fs=datos[0].stats.sampling_rate)
    plt.title("Specgram del terremoto (mediodia)")
    plt.xlabel("tiempo")
    plt.ylabel("frecuencia [Hz]")
    plt.tight_layout() #Para que no haga overlap el eje x con el titulo de la figura de abajo

    plt.show()

#si quiero pintar sesenta segundos tengo que multiplicar por 100, osea 60*100 = 6000 muestras