import streamlit as st
import pandas as pd
from datetime import date, time

# Import du dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url, sep=',')

# Définition des variables
pickup_list= df['pickup_borough'].unique().tolist()
dico_images = {'Manhattan':'https://www.travelandleisure.com/thmb/1pUBfq--CfF0kwVRYFs5P9RVPnw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/manhattanhenge-new-york-42nd-street-MNHTNHNGE0520-43a173535778405c989daf86add8e1a2.jpg',
               'Queens':'https://junehomes.com/blog/wp-content/uploads/2023/06/harry-gillen-c6fFCbbQky8-unsplash-1536x864.webp',
               'Bronx':'https://www.reddit.com/r/nyc/comments/ke1orm/todays_sunset_from_bronx/#lightbox', 
               'Brooklyn':'https://triptins.com/wp-content/uploads/2021/07/Brooklyn-Bridge-Sunrise-Photo-720x540.jpeg.webp', 
               'nan':'https://www.blind-magazine.com/fr/stories/sur-la-route/'}


# Titre principal de l'application (affiché en haut de la page)
st.title("Bienvenue sur le site web de Kiwiline0406")


# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
choice = st.selectbox("Indiquez votre arrondissement de récupération",
             pickup_list, placeholder= "Pourquoi tu n'as toujours rien renseigné ?") 


# Affichage du résultat sélectionné
if choice:
    st.write(f"Vous avez sélectionné : **{choice}**")
    # Affichage de l'image correspondante si elle existe
    if choice in dico_images:
        st.image(dico_images[choice], caption=f"Vue de {choice}", use_container_width=True)
    else:
        st.warning("Pas d'image disponible pour cet arrondissement.")
