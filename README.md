# 雷达控制台个人项目

前端 vue2，后端 flask python 3.8.20 主要是命令启动器

## 前端开发启动

```sh
cd Robot_control_frontend
yarn # 安装环境
yarn serve # 启动
```

## 后端开发启动

先 conda 切换环境python 3.8.20

```sh
cd Robot_control_frontend
pip install -r requirements.txt
python app.py
```

## 前端打包

```sh
cd radar_signal_display_frontend
yarn build
```

## 后端打包

```sh
cd radar_signal_display_backend
pyinstaller -F app.py
```
