# Eman Eid AI — 2026
مساعد ذكاء اصطناعي للطلاب الجامعيين

## تشغيل المشروع على جهازك

### الخطوة 1 — احصلي على API Key
1. روحي على: https://console.anthropic.com
2. سجّلي حساب جديد
3. اضغطي "API Keys" ثم "Create Key"
4. انسخي الـ Key

### الخطوة 2 — حطي الـ API Key
افتحي ملف `.env` وحطي الـ Key:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxx
```

### الخطوة 3 — نزّلي المكتبات
```bash
pip install -r requirements.txt
```

### الخطوة 4 — شغّلي المشروع
```bash
python app.py
```

### الخطوة 5 — افتحي المتصفح
روحي على: http://localhost:5000

## رفع المشروع على الإنترنت (Vercel)
1. نزّلي Vercel CLI: `npm i -g vercel`
2. في مجلد المشروع: `vercel`
3. اتبعي التعليمات وأضيفي ANTHROPIC_API_KEY في Environment Variables

## المميزات
- شات بوت ذكي يرد على أي سؤال
- متخصص في البرمجة والذكاء الاصطناعي
- مساعدة في الدراسة والبحوث الأكاديمية
- تعلم اللغات والسفر
- بحث في يوتيوب وجوجل مباشرة
- تصميم داكن احترافي
