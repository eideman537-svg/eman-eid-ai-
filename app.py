from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)
CORS(app)

# دي معناها: لو لقيت مفتاح في إعدادات الجهاز خده، لو ملقيتش خد المفتاح المكتوب ده
api_key = os.environ.get("GROQ_API_KEY") or "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"
client = Groq(api_key=api_key)

# تعريف شخصية البوت
SYSTEM_PROMPT = "أنت Eman Eid AI، مساعد ذكاء اصطناعي متخصص للطلاب الجامعيين، صممته الطالبة إيمان عيد."

@app.route("/")
def index():
    # التأكد من فتح صفحة الشات بوت
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_messages = data.get("messages", [])
        
        # استخراج آخر رسالة بعتيها
        latest_user_message = user_messages[-1]['content'] if user_messages else ""

        # استخدام الموديل الجديد المتاح في 2026
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": latest_user_message}
            ],
            model="llama-3.3-70b-versatile",
        )
        
        return jsonify({"reply": chat_completion.choices[0].message.content})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # تشغيل السيرفر على بورت 5000
    app.run(debug=True, port=5000)