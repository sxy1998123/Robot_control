from flask import Blueprint, request, jsonify, send_file, current_app
from datetime import datetime
import logging
import os
robot_bp = Blueprint('robot', __name__)

# logging.basicConfig(
#     level=logging.INFO,  # 修改日志级别输出所有日志
#     format='%(asctime)s %(name)s [%(pathname)s:%(lineno)d] %(levelname)s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',  # 日期时间格式
# )



@robot_bp.route('/test', methods=['POST'])
def test():
    """
    测试接口
    """
    data = request.get_json()
    print(data)
    return jsonify({'code': 200,'msg': '测试成功', 'data': data})