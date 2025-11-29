from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# Ma'lumotlarni saqlash uchun
DATA_FILE = 'collected_data.json'

@app.route('/')
def index():
    """Asosiy sahifa - bu yerda foydalanuvchi ma'lumotlari yig'iladi"""
    return render_template('index.html')

@app.route('/api/collect', methods=['POST'])
def collect_data():
    """Ma'lumotlarni serverga yuborish"""
    try:
        data = request.get_json()
        
        # Server tarafdan IP manzilni olish
        data['ip_address'] = request.remote_addr
        data['user_agent'] = request.headers.get('User-Agent')
        data['timestamp'] = datetime.now().isoformat()
        
        # Ma'lumotlarni faylga saqlash
        save_data(data)
        
        return jsonify({'status': 'success', 'message': 'Data collected'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/admin')
def admin():
    """Yig'ilgan ma'lumotlarni ko'rish"""
    data = load_data()
    return render_template('admin.html', data=data)

def save_data(data):
    """Ma'lumotlarni JSON faylga saqlash"""
    existing_data = load_data()
    existing_data.append(data)
    
    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f, indent=2)

def load_data():
    """Saqlangan ma'lumotlarni o'qish"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
