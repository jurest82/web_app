# conda activate esclavos_energeticos_web_app
# streamlit run web_app.py 

import streamlit as st
#import numpy as np
#import matplotlib.pyplot as plt


# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
energy_consumption = st.sidebar.slider("Consumo mensual de energía en tu hogar en kWh", 10, 500, 5, 1)
#travels = st.sidebar.slider("Viajes en carro que realizan en tu hogar semanalmente", 1, 100, 1)


time_bike = int((energy_consumption*1)/80)
st.write('Su consumo equivale a {} de pedaleo'.format(time_bike))

for i in range(0, time_bike):
    #if i < 20:
        st.image('./electric-bike.png', 
        width=25)

    

