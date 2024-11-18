from flask import Flask, request, jsonify, send_file, render_template
import pandas as pd
import joblib
from collections import Counter
import time  # Zaman ölçümü için
import os  # Dosya varlığını kontrol etmek için
from sklearn.preprocessing import StandardScaler
import uuid  # Benzersiz dosya isimleri için

app = Flask(__name__)

# Model ve özellikleri yükleme
model = joblib.load("catboost_model.pkl")
model_features = joblib.load("model_features.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Dosya yüklenmedi!"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Geçerli bir dosya seçin!"}), 400

    # Dosyayı oku
    start_time = time.time()  # Zaman ölçümünü başlat
    input_data = pd.read_csv(file)
    print(f"Yüklenen veri satır sayısı: {input_data.shape[0]}")

    # Eksik sütunları kontrol et
    missing_features = set(model_features) - set(input_data.columns)
    if missing_features:
        return jsonify({"error": f"Eksik özellikler: {missing_features}"}), 400

    # Sadece gerekli sütunları seç
    input_data = input_data[model_features]

    # Giriş verilerini ölçeklendirme
    scaler = StandardScaler()
    input_data[['Age', 'Annual_Premium', 'Policy_Sales_Channel', 'Region_Code']] = scaler.fit_transform(
        input_data[['Age', 'Annual_Premium', 'Policy_Sales_Channel', 'Region_Code']]
    )

    # Tahmin yap
    print("Tahmin işlemi başlıyor...")
    predictions = model.predict(input_data)
    print("Tahmin işlemi tamamlandı.")
    print(f"Tahmin edilen satır sayısı: {len(predictions)}")
    print(f"Tahmin süresi: {time.time() - start_time:.2f} saniye")  # Tahmin süresini yazdır

    input_data["Prediction"] = predictions

    # Tahmin oranlarını ve sınıf dağılımını hesapla
    prediction_counts = Counter(predictions)
    total = sum(prediction_counts.values())
    prediction_percentages = {
        "0": round((prediction_counts.get(0, 0) / total) * 100, 2),  # Almayacak
        "1": round((prediction_counts.get(1, 0) / total) * 100, 2)   # Alacak
    }

    # Benzersiz dosya ismi oluştur
    output_file = f"predictions_{uuid.uuid4().hex}.csv"
    input_data.to_csv(output_file, index=False)
    print(f"Sonuç dosyası kaydedildi: {output_file}")

    return jsonify({
        "message": "Tahmin başarıyla tamamlandı!",
        "download_url": f"/download/{output_file}",  # CSV dosyasını indirme linki
        "analysis": prediction_percentages,
        "distribution": {
            "alacak": prediction_counts.get(1, 0),
            "almayacak": prediction_counts.get(0, 0)
        }
    })

@app.route("/download/<filename>")
def download(filename):
    # Dosya varlığını kontrol et
    if not os.path.exists(filename):  # Eğer dosya yoksa
        return "Dosya bulunamadı! Lütfen tahmin işlemini tekrar yapın.", 404

    # Dosyayı gönder
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
