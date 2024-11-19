# Insurance Prediction Project

Bu proje, kullanıcıların sigorta satın alma olasılığını tahmin etmek için bir makine öğrenimi modeli geliştirme ve Flask tabanlı bir web uygulaması oluşturmayı içerir.

## 🎯 Projenin Amacı
Kullanıcıların demografik ve geçmiş sigorta bilgilerine dayanarak, sigorta satın alma olasılıklarını tahmin etmek. Proje, sigorta şirketlerinin hedef müşteri kitlesini daha iyi anlamalarına ve doğru stratejiler geliştirmelerine yardımcı olmayı amaçlamaktadır.

## 📊 Veri Hakkında
Veri Kaggle'dan alınmıştır ve aşağıdaki özellikleri içermektedir:

- **Age**: Kullanıcının yaşı
- **Gender**: Kullanıcının cinsiyeti
- **Driving_License**: Ehliyet sahibi olup olmadığı (1: Evet, 0: Hayır)
- **Previously_Insured**: Daha önce sigorta sahibi olup olmadığı (1: Evet, 0: Hayır)
- **Vehicle_Age**: Araç yaşı
- **Annual_Premium**: Yıllık sigorta primi
- **Policy_Sales_Channel**: Sigorta satış kanalı
- **Vintage**: Müşteri şirketle ne kadar süredir ilişkide

Veri üzerinde eksik değer kontrolü, aykırı değer tespiti, dengesizlik analizi yapılmış ve uygun veri işleme teknikleri uygulanmıştır.

---

## 🚀 Denediğim Modeller
Bu proje kapsamında çeşitli modeller denenmiş ve aşağıdaki sonuçlar elde edilmiştir:

### 1. **Logistic Regression**
- Performans: Basit ve hızlı bir model, ancak doğruluk düşük.

### 2. **Random Forest**
- Avantaj: Overfitting riskini azaltır.
- Dezavantaj: Büyük veri setlerinde yavaş çalışabilir.

### 3. **CatBoost (En İyi Performans Gösteren Model)**
- Avantaj: Kategorik verilerle çok iyi çalışır.
- Sonuç: Tahmin başarısı en yüksek olan modeldir.

### 4. **XGBoost**
- Avantaj: Daha hızlı eğitim süresi.
- Sonuç: Dengeli bir doğruluk sağladı ancak CatBoost kadar iyi değil.


## 📜 Medium Yazısı
Proje boyunca karşılaştığım süreçleri ve çözümlerimi Medium üzerinde detaylı bir şekilde ele aldım. Daha fazla bilgi için yazımı okuyabilirsiniz:

🔗 [Proje Süreci ve Deneyimlerim](https://medium.com/@meltemdanismaz/dengesiz-veri-setleriyle-%C3%A7al%C4%B1%C5%9Fmak-health-insurance-cross-sell-prediction-catboost-4c45a6bb0c61)

---

## 📂 Kaggle Çalışmaları
Kaggle'da farklı modeller ve optimizasyonlar üzerine çalıştım. Bu çalışmalara erişmek için aşağıdaki bağlantılara göz atabilirsiniz:

🔗 [Catboost ile Sigorta Tahmini](https://www.kaggle.com/code/meltemdanmaz/insurance-cross-sell-prediction-catboost)

---

## 📂 Proje Yapısı
insurance-prediction-project/ ├── data/ │ ├── raw/ # Ham veri dosyaları (işlenmemiş) │ │ ├── generated_dataset.csv │ │ ├── test.csv │ │ ├── train.csv │ ├── processed/ # İşlenmiş ve temizlenmiş veriyle model geliştirme │ ├── Insurance_Data_With_ROC.ipynb├── src/ # Kaynak kodlar │ ├── app.py # Flask uygulaması │ ├── model/ │ ├── catboost_model.pkl # Eğitimli model dosyası │ ├── model_features.pkl # Modelde kullanılan özellikler ├── static/ # Statik dosyalar ( görseller) │ ├── download.png ├── templates/ # HTML şablonları │ ├── index.html # Ana sayfa │ ├── thank_you.html # İndirme sonrası teşekkür sayfası ├── notebooks/ # Colab Notebook dosyaları │ ├── README.md # Proje açıklaması ve yönergeler


## 🛠️ Kullanılan Teknolojiler
- **Python**: Veri analizi ve makine öğrenimi
- **Flask**: Web uygulaması geliştirme
- **CatBoost**: Makine öğrenimi modeli
- **Pandas, Scikit-learn**: Veri işleme ve modelleme
- **Bootstrap**: Frontend tasarım
- **Colab Notebook**: Veri analizi ve model geliştirme



## 🚀 Uygulamanın Çalıştırılması

### 1. Gerekli Kütüphaneleri Yükleyin
Projede kullanılan bağımlılıkları yüklemek için şu komutu çalıştırın:
```bash
pip install -r requirements.txt

