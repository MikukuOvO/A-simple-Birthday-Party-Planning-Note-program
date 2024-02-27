from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/basicinfo')
def input_info():
    return render_template('basic_info.html')

if __name__ == '__main__':
    app.run()
