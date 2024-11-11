import socket  # noqa: F401


def main():
    with socket.create_server(("localhost", 6379), reuse_port=True, ) as server:
        while True:
            conn, addr = server.accept()
            print(f"addr: {addr}")
            request = b""
            with conn:
                while True:
                    request = conn.recv(100)
                    if request.decode('utf-8').endswith("exit\n"):
                        break
                    print(request)
                    conn.send(b"+PONG\r\n")
            print("Client exited!\r\nConnection Closed.")

if __name__ == "__main__":
    main()
