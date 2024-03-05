from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return render_template('index.html')

items = [
    # {"id": 1, "name": "小红", "relation": "朋友", "birthday": "1970-01-01", "planday": ""}, 
    # {"id": 2, "name": "小绿", "relation": "朋友", "birthday": "2050-01-01", "planday": ""}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # 在items列表中搜索具有指定ID的项目
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({'message': 'Item not found'}), 404
    
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # 查找指定的项目
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        # 如果项目不存在，返回404
        return jsonify({'message': 'Item not found'}), 404
    
    # 获取请求中的更新数据
    update_data = request.json
    # 这里假设update_data是一个字典，包含要更新的字段
    # 遍历更新数据，更新项目
    for key, value in update_data.items():
        if key in item:
            item[key] = value
    
    # 返回更新后的项目
    return jsonify(item)

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
    app.run(debug=True)
