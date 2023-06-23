import sounddevice as sd
import soundfile as sf


def kaydet(sure, dosya_adi, kanal_sayisi):
    # Ses ayarları
    frekans = 44100  # Örnekleme frekansı
    sd.default.samplerate = frekans
    sd.default.channels = kanal_sayisi

    # Ses kaydı
    print("Kayıt başlıyor...")
    ses = sd.rec(int(sure * frekans), channels=kanal_sayisi)
    sd.wait()  # Kaydın tamamlanmasını bekler

    # Ses kaydını dosyaya yazma
    sf.write(dosya_adi, ses, frekans)
    print(f"Kayıt tamamlandı. Ses dosyası: {dosya_adi}")


# Kayıt süresi (saniye)
sure = 5

# Kaydedilecek dosya adı
dosya_adi = "kayit.wav"

# Kaydedilecek kanal sayısı
kanal_sayisi = 1  # Örneğin, stereo (2 kanal)

# Kaydetme işlemi
kaydet(sure, dosya_adi, kanal_sayisi)
