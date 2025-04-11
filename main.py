from app import app  # app.py faylından Flask tətbiqini idxal et

if __name__ == "__main__":
    # Portu mühit dəyişənindən al, yoxsa 5000 istifadə et
    port = int(os.environ.get("PORT", 5000))  # PORT mühit dəyişəni, 5000 default portdur
    app.run(host="0.0.0.0", port=port)
