import streamlit as st

st.set_page_config(layout = "wide", page_title = "Home")
st.markdown("<h1 style='text-align: center'>Orientation diagnostiques en psychiatrie</h1>", unsafe_allow_html=True)
st.write("Bienvenue à mon projet de création d'une application web en Python pour l'orientation diagnostique en psychiatrie. Mon objectif est de mettre à disposition plusieurs échelles pour diagnostiquer des troubles tels que la dépression, le syndrome de stress post-traumatique (PTSD) et d'autres. Cependant, je tiens à souligner que ce projet n'est qu'un projet étudiant et que je ne suis pas un médecin ni psychologue. Par conséquent, il ne doit pas être utilisé comme support thérapeutique ou autre utilisation non supervisé ou encadré. En cas de besoin urgent, je vous recommande de contacter les services de secours appropriés ")
st.warning(" SAMU : 15 ou 112 Numéro national de prévention du suicide : 3114")
def page_0():
    st.empty()
def page_2():
    st.empty()

def page3():
    st.empty()



page_names_to_funcs = {
    "Home": page_0,
    "liens_court": page_2,
    "mdp": page3,

}