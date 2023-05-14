import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib as mp
import obspy 
from obspy.clients.fdsn import Client
client = Client("IRIS")
from seismic_attributes import seismic_attributes as sa
import pylatex as latex
import matplotlib as plt
mp.rcParams['text.usetex'] = False


t1 = sa.UTCDateTime("2022-10-19T08:00:00.0Z")
t2 = sa.UTCDateTime("2022-10-19T09:00:00.0Z")


stream = obspy.read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/CART.mseed")

print(stream)

stream.plot()

print("\n")
print("Este es el tamaño del stream",stream)
print("\n")

events = sa.get_events(stream, t1, t2, trigger_type='recstalta', sta=0.5, lta=10, thr_on=2, thr_off=1, thr_event_join=5)#sta y lta compara la media de las ultimas 100 muestras/segundos con el ruido de fondo y si aumenta mucho es un terremoto
#events = sa.get_events(stream1+stream2+stream3, t1, t2, trigger_type='multistalta', sta=0.5, lta=10, delta_sta=18, delta_lta=56, epsilon=10, avg_wave_speed=2, thr_event_join=10, thr_coincidence_sum=3)

events[0].to_csv('/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/event_catalogue.csv')
events[1].to_csv('/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/trace_catalogue.csv')


#sa.plot_events(events, stream, t1, t2)
#sa.plot_waveforms(events, '20180101T025446Z', start_buffer=30, end_buffer=60)
#attributes = sa.get_attributes(events, stream, sa.spectral_attributes, sa.polarity_attributes)
#attributes = sa.get_attributes(events, stream, sa.waveform_attributes, sa.spectral_attributes)
attributes = sa.get_attributes(events, stream, sa.spectral_attributes)
print(attributes)
attributes.to_csv('/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/15MarzoB/attribute_catalogue_backUp2.csv')

sa.plot_attributes(attributes)
sa.plot_correlations(attributes)





