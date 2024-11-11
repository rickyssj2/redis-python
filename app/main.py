import socket  # noqa: F401


def main():
    with socket.create_server(("localhost", 6379), reuse_port=True, ) as server:
        while True:
            conn, addr = server.accept()
            print(f"addr: {addr}")
            request = conn.recv(100)
            print(request)
            conn.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
