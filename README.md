# 🛡️ Proxy Checker

Knight Online sunucusuna hızlı bir şekilde proxy doğrulama işlemleri yapan, asenkron yapıda geliştirilmiş masaüstü uygulaması.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

---

## 📚 Proje Hakkında

Proxy Checker uygulaması, kullanıcı tarafından verilen proxy listesini [Knight Online](https://www.knightonline.world) sunucusuna bağlanarak doğrular ve sonuçları hızlıca gösterir. Asenkron yapı (`asyncio` + `aiohttp`) kullanılarak yüksek performans sağlanır.

Uygulama modern, karanlık temalı bir **Tkinter GUI** arayüzüne sahiptir ve başarılı proxy bağlantıları ile başarısız olanları renkli olarak ayırt eder.

### 🔹 Proxy Formatı

Proxy listesini aşağıdaki formatta girin:

```
ip:port kullanıcı:şifre
```

**Örnek:**
```
123.45.67.89:8080 user1:pass1
98.76.54.32:3128 user2:pass2
```

> ⚠️ **Not:** Proxy kimlik doğrulaması gerekmeyen proxyler desteklenmez. (Şu anda sadece user:pass formatlı proxyler test edilmektedir.)

---

## 🚀 Özellikler

- ✅ **Asenkron** proxy doğrulama (çok hızlı tarama)
- ✅ **Ping Süresi** hesaplama (milisaniye cinsinden)
- ✅ **Başarı / Hata** durumlarının renkli gösterimi (Yeşil/Kırmızı)
- ✅ **Karanlık Tema** destekli modern GUI
- ✅ **Timeout** ve **Kimlik Doğrulama Hatalarını** yönetme
- ✅ **Format Hatalarını** tespit edip uyarı verme
- ✅ Hafif ve kullanıcı dostu

---

## 🛠️ Kurulum

İlk olarak, bu repoyu klonlayın:

```bash
git clone https://github.com/KULLANICI_ADIN/proxy-checker.git
cd proxy-checker
```

Gereken Python paketlerini yükleyin:

```bash
pip install aiohttp
```

> **Not:** `tkinter` modülü Python ile birlikte gelir, ekstra kurulum gerekmez.

---

## ⚡ Kullanım

Uygulamayı başlatmak için:

```bash
python proxy_checker.py
```

1. Proxy listesini uygulamada üstteki kutuya girin.
2. **Check Proxies** butonuna tıklayın.
3. Sonuçlar anlık olarak listelenecek:
   - 🟢 Başarılı bağlantılar yeşil ile gösterilir.
   - 🔴 Hatalı veya zaman aşımına uğrayan bağlantılar kırmızı ile gösterilir.

---

## 📷 Ekran Görüntüsü

![Proxy Checker Arayüzü](screenshot.png) 

> Uygulamanın çalışır halini gösteren ekran görüntüsü.

---

## 📦 Gereksinimler

- Python 3.8 veya üzeri
- aiohttp
- tkinter (Python'un standart modüllerinden biri)

---

## 📌 Bilgilendirme

- **SSL hatalarını** önlemek için aiohttp'da `ssl=False` opsiyonu kullanılmaktadır.
- **Timeout** 10 saniye olarak ayarlanmıştır.
- Proxy sunucu kimlik doğrulama hataları, doğru giriş yapılmadıysa ayrı olarak belirtilir.
- Giriş yapılan proxy listesinde **hatalı formatlar** ayrı ayrı tespit edilip raporlanır.

---

## 📝 Lisans

Bu proje [MIT License](LICENSE) ile lisanslanmıştır. İstediğiniz gibi kullanabilir, değiştirebilir ve dağıtabilirsiniz.

---


