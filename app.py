import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import urllib.parse
from dotenv import load_dotenv

# API ve Çevre Ayarları
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key.strip())

def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt, image])
    return response.text

# Google Görseller Linki Oluşturma Fonksiyonu
def create_google_search_link(recipe_name):
    query = urllib.parse.quote(recipe_name + " yemeği")
    return f"https://www.google.com/search?tbm=isch&q={query}"

# --- Sayfa Ayarları ---
st.set_page_config(page_title="ChefVision Pro", page_icon="🍳", layout="wide")

st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] { padding: 10px 30px; font-weight: bold; }
    .search-link { 
        display: inline-block; padding: 10px 20px; background-color: #4285F4; 
        color: white; text-decoration: none; border-radius: 5px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍳 ChefVision: Akıllı Şef Asistanı")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    uploaded_file = st.file_uploader("Buzdolabı fotoğrafı yükle...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Senin Dolabın', use_container_width=True)
        submit = st.button("Şefe Danış!", use_container_width=True)

with col2:
    if uploaded_file and submit:
        with st.spinner('Şef malzemeleri inceliyor ve tarifleri hazırlıyor...'):
            prompt = """
            Resimdeki malzemeleri listele. 
            Ardından bu malzemelerle yapılacak 3 farklı tarifi şu başlıklarla ver:
            TARIF_1_ISIM: [Yemek Adı]
            TARIF_1_DETAY: [Malzemeler ve Hazırlanış]
            TARIF_2_ISIM: [Yemek Adı]
            TARIF_2_DETAY: [Malzemeler ve Hazırlanış]
            TARIF_3_ISIM: [Yemek Adı]
            TARIF_3_DETAY: [Malzemeler ve Hazırlanış]
            """
            try:
                res = get_gemini_response(image, prompt)
                
                # Veriyi parçalama (Parsing)
                def get_part(text, start_key, end_key=None):
                    try:
                        start = text.find(start_key) + len(start_key)
                        end = text.find(end_key) if end_key else len(text)
                        return text[start:end].strip(": \n")
                    except: return "Tarif alınamadı."

                t1_name = get_part(res, "TARIF_1_ISIM", "TARIF_1_DETAY")
                t1_content = get_part(res, "TARIF_1_DETAY", "TARIF_2_ISIM")
                
                t2_name = get_part(res, "TARIF_2_ISIM", "TARIF_2_DETAY")
                t2_content = get_part(res, "TARIF_2_DETAY", "TARIF_3_ISIM")
                
                t3_name = get_part(res, "TARIF_3_ISIM", "TARIF_3_DETAY")
                t3_content = get_part(res, "TARIF_3_DETAY")

                # Sekmeli Görünüm
                tab1, tab2, tab3 = st.tabs([f"🍴 {t1_name[:20]}", f"🥗 {t2_name[:20]}", f"🍕 {t3_name[:20]}"])
                
                with tab1:
                    st.subheader(t1_name)
                    st.write(t1_content)
                    st.markdown(f'<a href="{create_google_search_link(t1_name)}" target="_blank" class="search-link">🖼️ Yemeğin Nasıl Göründüğüne Bak</a>', unsafe_allow_html=True)

                with tab2:
                    st.subheader(t2_name)
                    st.write(t2_content)
                    st.markdown(f'<a href="{create_google_search_link(t2_name)}" target="_blank" class="search-link">🖼️ Yemeğin Nasıl Göründüğüne Bak</a>', unsafe_allow_html=True)

                with tab3:
                    st.subheader(t3_name)
                    st.write(t3_content)
                    st.markdown(f'<a href="{create_google_search_link(t3_name)}" target="_blank" class="search-link">🖼️ Yemeğin Nasıl Göründüğüne Bak</a>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Hata: {e}")
    else:
        st.info("👈 Başlamak için sol taraftan bir fotoğraf yükleyin.")