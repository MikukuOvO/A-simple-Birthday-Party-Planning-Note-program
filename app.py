from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return render_template('index.html')

items = [
    {"id": 1, "name": "小红", "relation": "朋友", "birthday": "1970-01-01"}, 
    {"id": 2, "name": "小绿", "relation": "朋友", "birthday": "2050-01-01"}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.json
    item['id'] = len(items) + 1
    items.append(item)
    return jsonify(item), 201

@app.route('/allinfo')
def input_all_info():
    return render_template('all_info.html')

@app.route('/basicinfo')
def input_info():
    return render_template('basic_info.html')

@app.route('/setplanday')
def set_plan_day():
    return render_template('set_plan_day.html')

@app.route('/resultdisplay')
def result_display():
    return render_template('result_display.html')

@app.route('/endpage')
def endpage():
    return render_template('endpage.html')

@app.route('/closepage')
def closepage():
    return render_template('closepage.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
