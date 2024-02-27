from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/continue', methods=['POST'])
def input_info():
    
    return '用户按下了任意键，继续游戏'

if __name__ == '__main__':
    app.run()
