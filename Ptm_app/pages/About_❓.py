# -*- coding: utf-8 -*-

import streamlit as st
import os 
path=os.getcwd()

st.title('About')
st.header("L'équipe Pytmosphere")
st.subheader('_:blue[Morgane Andrès]_  ' )
st.subheader('_:blue[Quang Hai Bui]_' )
st.subheader('_:blue[Charles Hiribarrondo]_' )

st.header('Sources')

st.write(" [Agence européenne de l'environnement (EEA)](https://www.eea.europa.eu/data-and-maps/data/co2-cars-emission-20)")
st.write(" [Loi climat et résiliences](https://www.ecologie.gouv.fr/loi-climat-resilience)")
st.write("[Niveau d'émission des véhicules (étiquette énergie)](http://www.vedura.fr/guide/ecolabel/etiquette-energie-CO2-voiture)")