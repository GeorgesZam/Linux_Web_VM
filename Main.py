import streamlit as st
import subprocess

st.title("Terminal Linux Simulé avec Streamlit")

# Entrée utilisateur pour saisir une commande
command = st.text_input("Saisissez une commande Linux :")

if st.button("Exécuter"):
    if command:
        # Exécute la commande dans le terminal et récupère la sortie
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            st.text_area("Résultat de la commande", result.stdout + result.stderr)
        except Exception as e:
            st.error(f"Erreur lors de l'exécution de la commande : {e}")
    else:
        st.warning("Veuillez saisir une commande.")
