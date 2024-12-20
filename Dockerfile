# Kullanılacak temel image (örneğin, Python)
FROM python:3.9-slim

# Gerekli bağımlılıkları yükleme
RUN pip install flask

# Uygulama dosyasını kopyalama
COPY system.py /app/

# Çalışma dizinini ayarlama
WORKDIR /app

# Uygulamanın çalıştırılması
CMD ["python", "system.py"]
