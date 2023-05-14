import pandas as pd
import numpy as np 
import seaborn as sb
import matplotlib as mp
import obspy 
from obspy.clients.fdsn import Client
#client = Client("IRIS")
from seismic_attributes import seismic_attributes as sa
import pylatex as latex
import matplotlib as plt


t1 = sa.UTCDateTime("2021-08-28T00:00:00.0Z")
t2 = sa.UTCDateTime("2021-08-29T00:00:00.0Z")
stream = obspy.read("/Users/pablosreyero/Documents/Universidad/Practicas2022:2023/Prácticas IGN/8Marzo/EALB20210828.mseed")
print(stream)

events = sa.get_events(stream, t1, t2, trigger_type='recstalta', sta=1, lta=1000, thr_on=5, thr_off=1, thr_event_join=5)#sta y lta compara la media de las ultimas 100 muestras/segundos con el ruido de fondo y si aumenta mucho es un terremoto
events[0].to_csv('event_catalogue.csv')
events[1].to_csv('trace_catalogue.csv')

#sa.plot_events(events, stream, t1, t2)
#sa.plot_waveforms(events, '20180101T025446Z', start_buffer=30, end_buffer=60)

#attributes = sa.get_attributes(events, stream, sa.spectral_attributes, sa.polarity_attributes)
attributes = sa.get_attributes(events, stream, sa.spectral_attributes)
#attributes.to_csv('attribute_catalogue.csv')

sa.plot_attributes(attributes)
sa.plot_correlations(attributes)






