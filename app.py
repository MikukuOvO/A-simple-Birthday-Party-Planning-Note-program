from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/basicinfo')
def input_info():
    return render_template('basic_info.html')

@app.route('/setplanday')
def set_plan_day():
    return render_template('set_plan_day.html')

if __name__ == '__main__':
    app.run()
