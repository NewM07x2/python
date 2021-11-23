"""
サーバ通信

"""

import requests
import http.server
import socket
import socketserver
with socketserver.TCPServer(('127.0.0.1', 8000), http.server.SimpleHTTPRequestHandler) as httpd:
    # 実行
    httpd.serve_forever()
