# serve.py — letakkan di folder yang sama dengan Sumberdownload.html
import http.server
import socketserver
import socket

PORT = 8000

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    ip = get_local_ip()
    print(f"Server jalan di:")
    print(f"  → http://localhost:{PORT}")
    print(f"  → http://{ip}:{PORT}   (buka dari HP, satu Wi-Fi)")
    print("Tekan Ctrl+C untuk stop.")
    httpd.serve_forever()