import socket

sock = socket.socket(socket.AF_INET)
sock.bind(("0.0.0.0", 8080))
sock.listen()

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print(data.decode("UTF-8"))
    conn.sendall(b"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 17
Connection: Close

<h1>Hello API</h>""")
    conn.close()