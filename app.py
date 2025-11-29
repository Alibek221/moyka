from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import os
import requests

app = Flask(__name__)

# Ma'lumotlarni saqlash uchun
DATA_FILE = 'collected_data.json'

def get_ip_geolocation(ip):
    """IP orqali joylashuvni olish"""
    try:
        # ipapi.co - bepul IP geolocation service
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

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
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if ',' in ip:
            ip = ip.split(',')[0].strip()
        
        data['ip_address'] = ip
        data['user_agent'] = request.headers.get('User-Agent')
        data['timestamp'] = datetime.now().isoformat()
        
        # IP orqali joylashuvni olish
        geo_data = get_ip_geolocation(ip)
        if geo_data:
            data['ip_location'] = {
                'city': geo_data.get('city'),
                'region': geo_data.get('region'),
                'country': geo_data.get('country_name'),
                'latitude': geo_data.get('latitude'),
                'longitude': geo_data.get('longitude'),
                'timezone': geo_data.get('timezone'),
                'isp': geo_data.get('org')
            }
        
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
