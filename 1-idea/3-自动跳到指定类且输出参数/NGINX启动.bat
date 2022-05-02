@echo off
set nginx_path=D:\13-auto\1-idea\3-自动跳到指定类且输出参数
echo nginxpath: %nginx_path%
cd %nginx_path%
echo "waterRPA.py is starting"
start python waterRPA.py
cd %~dp0
pause