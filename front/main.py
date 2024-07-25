from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/infer')
def index():
    infer_ip = os.environ.get('INFERENCE_IP', '127.0.0.1')
    infer_port = os.environ.get('INFERENCE_PORT', '5000')
    api_url = "http://" + infer_ip + ":" + infer_port + "/infer"  # 或者根据环境动态设置
    return render_template('index.html', api_url=api_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
