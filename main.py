import base64

import streamlit as st
import pandas as pd
from datetime import date, timedelta

# main page css
st.markdown("""
<style>
/* Page background color */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(100deg,  #ccffff, #ffffff);
}
</style>
""", unsafe_allow_html=True)

# Title Page config
st.set_page_config(page_title="Soma Tour & Travels", page_icon="🚌", layout="wide")

# Function to convert image to Base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Convert local image
title_img = get_base64("B11R-cover-image.jpg")  # Change to your file path

st.markdown(f"""
<style>
.hero {{
    position: relative;
    height: 70vh;
    background-image: url("data:image/jpg;base64,{title_img}");
    border-radius: 15px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}}
.overlay {{
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.45);
}}
.hero-content {{
    position: relative;
    padding: 230px;
    color: white;
    z-index: 1;
}}
.hero h1 {{
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}}
.hero p {{
    font-size: 1.25rem;
}}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
<div class="hero">
  <div class="overlay"></div>
  <div class="hero-content">
    <h1>Soma Tour & Travels</h1>
    <p>Premium Bus Services • Comfort | Safety | On Time</p>
  </div>
</div>
""", unsafe_allow_html=True)


# Popular Routes
st.markdown("---")
st.markdown("## Popular Routes")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Kanpur ⇄ Delhi-NCR","From ₹499","55+ daily services")
col2.metric("Kanpur ⇄ Madhya Pradesh","From ₹499","Luxury coach")
col3.metric("Kanpur ⇄ rajasthan","From ₹499","AC Sleeper/Seater")
col4.metric("Kanpur ⇄ Uttrakhand","From ₹699","Non-AC Sleeper/Seater")
col5.metric("Kanpur ⇄ Bihar","From ₹699","Safe-clean coach")
col6.metric("Kanpur ⇄ Gujrat","From ₹699","Onboarding Offers")


# Honeymoon Special
st.markdown("---")
st.markdown("## Honeymoon Special")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Kanpur ⇄ Dehradun","From ₹999")
col2.metric("Kanpur ⇄ Nainital","From ₹999")
col3.metric("Kanpur ⇄ Haldwani","From ₹999")
col4.metric("Kanpur ⇄ Jaipur","From ₹999")
col5.metric("Kanpur ⇄ Udaipur","From ₹999")
col6.metric("Kanpur ⇄ Jaisalpur","From ₹999")


# Family Special
st.markdown("## Family Special")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Kanpur ⇄ Vrindavan","From ₹799")
col2.metric("Kanpur ⇄ Mehandipur","From ₹599")
col3.metric("Kanpur ⇄ Khatushyamji","From ₹999")
col4.metric("Kanpur ⇄ Ayodhya","From ₹699")
col5.metric("Kanpur ⇄ Kaichi-Dhaam","From ₹899")
col6.metric("Kanpur ⇄ Haridwar","From ₹999")


# Package Tour
st.markdown("---")
st.markdown("## Package Tour")
f1, f2, f3, f4 = st.columns(4)
f1.info("**1999 Only** \n\n AC/N-AC seater Bus \n\nMehandipurBalaji, Khatu Shyamji, Salasar Hanumanji, Kaila Devi Mata, Mathura, Vrindavan")
f2.info("**4999 Only** \n\n AC/N-AC seater Bus \n\nHaridwar, Vaishno Devi Jammu, Bagha Border, Swarn Temple Amritsar, Mathura, Vrindavan")
f3.info("**1999 Only** \n\n AC/N-AC seater Bus \n\nKashi Vishwanath, Varanasi, Vindwashini Mirzapur, Triveni Sangam, Hanuman Temple Prayagraj")
f4.info("**One Day Tour** \n\n 17 Seater AC Traveller - 999 Only \n\n 26 Seater AC Traveller - 1499 Only \n\n 66 Seater N-AC Bus - 799 Only \n\nKashi Ayodhya, Sarayu ghat, Hanuman Garhi, Kanak Bhawan, Dashrath Mahal, Sita Rasoi")

# \n Balaji \nKhatu Shyamji \nSalasar Hanumanji \nKaila Devi Mata \nMathura \nVrindavan


# Features
st.markdown("---")
st.markdown("## Why Choose Soma Tour & Travels?")
f1, f2, f3 = st.columns(3)
f1.info("🧼 **Ultra-Clean Coaches**\n\nSanitized after every trip.")
f2.info("🛡️ **Verified Drivers**\n\nExperienced & background-checked.")
f3.info("📡 **Live GPS Tracking**\n\nShare your ride in real-time.")

# Contact
st.markdown("---")
st.markdown("## Contact Us")
st.write("📞 **Phone:** +91-8353973005/+91-7905762829")
st.write("💬 **WhatsApp:** +91-8353973005")
st.write("✉️ **Email:** somatourtravel19@gmail.com")
st.write("📍 **Address:** KB-II/129 Barra-2 80 feet road, Kanpur Nagar, UP 208027")


# Note
st.markdown("---")
st.markdown("## Soma Tour & Travels")
st.write("Buses available for long-distance travel, tourism/sightseeing, school or college trips, weddings or family functions, and corporate/office trips")

