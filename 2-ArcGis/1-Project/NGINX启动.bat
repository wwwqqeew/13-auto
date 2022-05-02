@echo off
set nginx_path=D:\13-auto\2-ArcGis\1-Project
echo nginxpath: %nginx_path%
cd %nginx_path%
echo "waterRPA.py is starting"
start python waterRPA.py
cd %~dp0
pause