#!/usr/bin/env python3
"""
应聘搭子 Web 应用启动脚本
"""

import os
import http.server
import socketserver
from pathlib import Path

PORT = 8001  # 使用8001端口，避免和面试助手冲突

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

def main():
    script_dir = Path(__file__).parent.absolute()
    os.chdir(script_dir)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"=" * 50)
        print(f"🤝 应聘搭子 Web 应用已启动！")
        print(f"=" * 50)
        print(f"")
        print(f"本地访问地址:")
        print(f"  http://localhost:{PORT}")
        print(f"")
        print(f"局域网访问地址:")
        print(f"  http://你的IP:{PORT}")
        print(f"")
        print(f"按 Ctrl+C 停止服务")
        print(f"")
        print(f"=" * 50)
        httpd.serve_forever()

if __name__ == "__main__":
    main()
