import psutil
from http.server import BaseHTTPRequestHandler, HTTPServer


def find_procs_by_name(proc_name):
    flag = False
    for p in psutil.process_iter(['name']):
        if p.info['name'] == proc_name:
            flag = True
            break
    return flag

        
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        proc_name = 'mymi.exe'
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        status = find_procs_by_name(proc_name)
        self.wfile.write(bytes(str(status), "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer(('', 8086), MyServer)
    print("Server started http://%s:%s" % ('localhost', 8086))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

