from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '服务已部署，等待开始录制'

@app.route('/start')
def start():
    # 运行 main.py，执行录制逻辑
    subprocess.Popen(["python", "main.py", "--room_id", "123456"])
    return '录制任务已启动'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
