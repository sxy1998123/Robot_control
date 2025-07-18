from flask import Flask, jsonify, send_from_directory, Blueprint
from flask_cors import CORS
import logging
from routes import robot_bp
from flasgger import Swagger

logging.basicConfig(
    level=logging.INFO,  # 修改日志级别输出所有日志
    format='%(asctime)s %(name)s [%(pathname)s:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # 日期时间格式
)


app = Flask(__name__, static_folder='frontend_dist', static_url_path='')
CORS(app)  # 开发环境下允许跨域请求


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.route('/')
def index():
    return "Hello World"

@app.route('/api/test')
def test():
    return "test"


app.register_blueprint(robot_bp, url_prefix="/api/robot")
Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
