# 🍳 ChefVision AI: Akıllı Mutfak Asistanı

ChefVision AI, buzdolabınızdaki malzemeleri yapay zeka ile analiz eden ve saniyeler içinde size özel yemek tarifleri sunan modern bir web uygulamasıdır. Google'ın en yeni nesil **Gemini 2.5 Flash** modelinin görüntü işleme gücünü kullanarak mutfaktaki "Bugün ne pişirsem?" derdine son verir.

---

## ✨ Öne Çıkan Özellikler

* **🔍 Akıllı Malzeme Tespiti:** Yüklenen fotoğraftaki sebze, meyve, et ve diğer gıda ürünlerini otomatik olarak listeler.
* **🍽️ Kişiselleştirilmiş Tarif Önerileri:** Eldeki malzemelerle hazırlanabilecek, yaratıcı ve detaylı 3 farklı tarif sunar.
* **📑 Sekmeli (Tab) Arayüz:** Kullanıcı deneyimini artırmak için tarifleri yan yana sekmelerde sunar; böylece ekranı aşağı kaydırmanıza gerek kalmaz.
* **🖼️ Görsel Önizleme:** Her tarifin altında bulunan "Yemeğin Nasıl Göründüğüne Bak" butonu ile yemeğin gerçek görüntülerine anında ulaşmanızı sağlar.

---

## 🛠️ Kullanılan Teknolojiler

* **🐍 Python:** Uygulamanın temel motoru.
* **🤖 Google Gemini 2.5 Flash:** Görüntü analizi ve doğal dil işleme (LLM).
* **🎨 Streamlit:** Hızlı ve şık web arayüzü tasarımı.
* **🖼️ Pillow (PIL):** Görsel yükleme ve ön işleme süreçleri.
* **🔐 python-dotenv:** API anahtarlarının ve çevre değişkenlerinin güvenli yönetimi.

---

## 🚀 Yerel Kurulum (Local Setup)

1. **Projeyi Klonlayın:**
   git clone https://github.com/kullaniciadi/ChefVision-AI.git
   cd ChefVision-AI

2. **Gerekli Kütüphaneleri Yükleyin:**
   pip install -r requirements.txt

3. **API Anahtarını Yapılandırın:**
   Klasör içinde bir .env dosyası oluşturun ve Google API anahtarınızı ekleyin:
   GOOGLE_API_KEY="BURAYA_API_KEY_GELECEK"

4. **Uygulamayı Çalıştırın:**
   streamlit run app.py

---

## 🔐 Güvenlik ve Gizlilik Prensipleri

Bu proje geliştirilirken siber güvenlik en iyi uygulamaları (best practices) dikkate alınmıştır:
* **🔑 API Key Güvenliği:** API anahtarları asla kodun içinde saklanmaz; .env dosyası aracılığıyla yönetilir.
* **☁️ Cloud Secrets:** Canlı ortamda (Streamlit Cloud) anahtarlar "Secrets Management" panelinden güvenli bir şekilde aktarılır.

---

**👨‍🍳 Şefin Notu:** Afiyet olsun! Projeyi beğendiyseniz GitHub üzerinden yıldız (star) vermeyi unutmayın.