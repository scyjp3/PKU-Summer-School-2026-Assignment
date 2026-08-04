@echo off
chcp 65001 >nul
echo ==============================================
echo     北京大学暑期学校 - 作业管理系统
echo ==============================================
echo.
echo 正在启动本地服务器...
echo.
cd /d "%~dp0"
python -m http.server 8000
pause