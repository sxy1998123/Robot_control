import logging

logger = logging.getLogger(__name__)

logger.info("handler.py is running")


def handle_start_arm():
    logger.info("Button start_arm pressed")


def handle_btn():
    logger.info("Button btn pressed")


# def logger_test():
#     # 调试信息：检查记录器配置
#     print(f"模块记录器 '{logger.name}' 配置:")
#     print(f"  有效级别: {logging.getLevelName(logger.getEffectiveLevel())}")
#     print(f"  处理器数量: {len(logger.handlers)}")
#     print(f"  是否传播: {logger.propagate}")

#     # 测试日志输出
#     logger.debug("调试信息 - 不应显示")
#     logger.info("模块1信息 - 应显示")
#     logger.warning("模块1警告 - 应显示")

#     # 测试根记录器
#     root_logger = logging.getLogger()
#     root_logger.info("来自模块1的根记录器信息 - 应显示")


# logger_test()
