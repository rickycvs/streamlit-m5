import streamlit as st

def bienvenida(nombre):
    mymensaje = f'Bienvenido/a : {nombre}'
    return mymensaje

myname = st.text_input('nombre :')

if (myname):
    mensaje = bienvenida(myname)
    st.write("Resultado: "+mensaje)