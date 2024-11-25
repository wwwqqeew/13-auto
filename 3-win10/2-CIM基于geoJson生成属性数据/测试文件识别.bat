@echo off
set nginx_path=D:\13-auto\3-win10\1-cesiumlab2启动
echo nginxpath: %nginx_path%
cd %nginx_path%
echo "waterRPA.py is starting"
start python tesReadImg.py
cd %~dp0