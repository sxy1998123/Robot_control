from flask_cors import CORS
from flask import Flask, jsonify, send_from_directory, Blueprint, request
from flasgger import Swagger
import logging
import json


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # 修改日志级别输出所有日志
        # format='%(asctime)s %(name)s [%(pathname)s:%(lineno)d] %(levelname)s %(message)s',
        format='%(asctime)s %(name)s [%(filename)s:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',  # 日期时间格式
    )
    # werkzeug_logger = logging.getLogger('werkzeug') # 禁用werkzeug日志
    # werkzeug_logger.setLevel(logging.CRITICAL)


app = Flask(__name__, static_folder='frontend_dist', static_url_path='')
CORS(app)  # 开发环境下允许跨域请求


@app.errorhandler(404)
def page_not_found(error):
    # 返回index.html页面
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/btn_click', methods=['POST'])
def btn_click():
    required_fields = ['btn_name', 'form']
    if not all(field in request.json for field in required_fields):
        return jsonify({'error': 'Missing required fields btn_name or form'}), 400

    btn_name = request.json.get('btn_name')
    logging.info(f"点击的按钮是：{btn_name}")

    form = request.json.get('form')
    logging.info(f"接收到的表单数据：{form}")
    # 表单数据处理start
    arm1_ip = form.get('arm1_ip')
    arm2_ip = form.get('arm2_ip')
    is_end_device = form.get('is_end_device')
    end_device_name = form.get('end_device_name')
    arm_file_path = form.get('arm_file_path')
    vision_pro_file_path = form.get('vision_pro_file_path')
    init_pose_file_name = form.get('init_pose_file_name')
    waypoints_file_name = form.get('waypoints_file_name')
    # 表单数据处理end

    # 按钮名与对应处理函数的映射字典
    btn_name_dicts = {
        "start_arm": handler.handle_start_arm,
        "btn": handler.handle_btn,
    }
    # 调用对应处理函数
    btn_name_dicts[btn_name]()

    # 构造回传给前端的响应
    response = {
        'code': 200,
        'msg': 'Success',
    }

    return jsonify(response), 200


Swagger(app)

if __name__ == '__main__':
    setup_logging()
    import handler
    app.run(debug=True, host='0.0.0.0', port=5000)
