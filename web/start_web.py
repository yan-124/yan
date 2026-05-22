"""
Web应用启动脚本
启动后端API服务
"""
import subprocess
import sys
import os

def start_server():
    """启动后端服务"""
    print("🚀 正在启动IT面试助手 Web服务...")
    print("📍 服务地址: http://localhost:9000")
    print("📱 前端地址: 打开 web/index.html")
    print()
    
    # 启动后端服务
    os.system("cd /workspace/projects && python src/main.py -p 9000 &")
    
    print("✅ 后端服务已启动!")
    print()
    print("📋 使用说明:")
    print("1. 后端API服务: http://localhost:9000")
    print("2. 前端页面: 打开 web/index.html")
    print("3. 如需公网访问，需要配置nginx反向代理")
    print()
    print("按 Ctrl+C 停止服务")

if __name__ == "__main__":
    start_server()
