# 🔒 Xavfsizlik Demo - IP, GPS va Kamera Ma'lumotlarini Yig'ish

## ⚠️ MUHIM OGOHLANTIRISH

**Bu loyiha faqat ta'lim va xavfsizlik tadqiqoti maqsadida yaratilgan!**

### ❌ Qonunga zid ishlatish taqiqlanadi:
- Boshqa odamlarga zarar yetkazish
- Ruxsatsiz ma'lumot yig'ish
- Phishing hujumlari
- Shaxsiy hayotni buzish

### ✅ Qonuniy foydalanish:
- O'z qurilmalaringizda test qilish
- Xavfsizlik zaifliklarini o'rganish
- Himoya mexanizmlarini tushunish
- Ethical hacking ta'limi

## 📋 Qanday ishlaydi?

Bu demo quyidagi ma'lumotlarni yig'ish jarayonini ko'rsatadi:

1. **IP Manzil** - Server tomonidan avtomatik aniqlanadi
2. **GPS Joylashuv** - Geolocation API orqali (foydalanuvchi ruxsati bilan)
3. **Kamera Rasmi** - MediaDevices API orqali (foydalanuvchi ruxsati bilan)
4. **Brauzer Ma'lumotlari** - User Agent, ekran o'lchami, til va h.k.

## 🚀 O'rnatish va Ishga Tushirish

### 1. Dependencies o'rnatish:
```bash
cd /home/kali/security-demo
pip3 install -r requirements.txt
```

### 2. Ilovani ishga tushirish:
```bash
python3 app.py
```

### 3. Brauzerda ochish:
```
http://localhost:5000
```

### 4. Test qilish:
- Asosiy sahifada "Sovg'ani Olish" tugmasini bosing
- GPS va kamera ruxsatini bering
- `/admin` sahifasida yig'ilgan ma'lumotlarni ko'ring

## 📁 Fayl Tuzilishi

```
security-demo/
├── app.py                    # Flask backend server
├── requirements.txt          # Python dependencies
├── collected_data.json       # Yig'ilgan ma'lumotlar (avtomatik yaratiladi)
├── templates/
│   ├── index.html           # Asosiy sahifa (ma'lumot yig'ish)
│   └── admin.html           # Admin panel (ma'lumotlarni ko'rish)
└── README.md                # Bu fayl
```

## 🛡️ Himoyalanish Yo'llari

Bu demo orqali quyidagilarni o'rganishingiz mumkin:

### 1. **Shubhali havola/sahifalardan ehtiyot bo'ling**
- Noma'lum manbalardan kelgan havolalarni ochmaslik
- URL manzilini tekshirish (https, domen nomi)

### 2. **Brauzer ruxsatlariga e'tibor bering**
- GPS joylashuv ruxsatini faqat ishonchli saytlarga berish
- Kamera/mikrofon ruxsatini ehtiyotkorlik bilan berish

### 3. **VPN va Privacy toollar**
- VPN ishlatib IP manzilni yashirish
- Privacy-focused brauzerlar (Brave, Firefox Focus)

### 4. **Antivirus va Firewall**
- Zamonaviy antivirus dasturidan foydalanish
- Firewall sozlamalarini tekshirish

## 🌐 Cloudflare'ga Deploy Qilish (Ixtiyoriy)

Agar bu demo'ni internetda test qilmoqchi bo'lsangiz:

### Workers orqali (Sodda):
```bash
# Cloudflare Wrangler CLI o'rnatish
npm install -g wrangler

# Workers loyihasini yaratish
wrangler init security-demo

# Deploy qilish
wrangler publish
```

### Pages orqali (To'liq):
1. GitHub'ga push qiling
2. Cloudflare Pages'da yangi project yarating
3. GitHub repository'ni ulang
4. Build settings:
   - Build command: `pip install -r requirements.txt`
   - Output directory: `/`

## 📊 Yig'ilgan Ma'lumotlar

Ma'lumotlar `collected_data.json` faylida saqlanadi:

```json
{
  "ip_address": "127.0.0.1",
  "location": {
    "latitude": 41.2995,
    "longitude": 69.2401,
    "accuracy": 30
  },
  "camera": {
    "captured": true,
    "image": "data:image/jpeg;base64,..."
  },
  "browser": {
    "userAgent": "Mozilla/5.0...",
    "language": "uz-UZ",
    "platform": "Linux"
  }
}
```

## 🎓 O'rganish Resurslari

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Security Academy](https://portswigger.net/web-security)
- [HackerOne](https://www.hackerone.com/)
- [Bug Bounty Programs](https://www.bugcrowd.com/)

## ⚖️ Qonuniy Mas'uliyat

Bu dastur faqat ta'lim maqsadida taqdim etilgan. Yaratuvchi qonunga zid ishlatishdan mas'ul emas.

**Eslatma:** Boshqa odamlarga zarar yetkazish maqsadida foydalanish jinoiy javobgarlikka olib keladi!

## 📞 Yordam

Savollar yoki muammolar bo'lsa:
- GitHub Issues ochish
- Ethical hacking forumlarga murojaat qilish
- Xavfsizlik ekspertlariga savol berish

---

**Xavfsiz bo'ling va mas'uliyat bilan o'rganing! 🛡️**
