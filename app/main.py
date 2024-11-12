import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    try:
        while True:
            data = await reader.read(1024)            
            if not data: # If no data is received, the client has closed the connection
                break
            print(f"Received {data.decode()} from {addr}")
            writer.write(b"+PONG\r\n")
            await writer.drain()  # Ensure data is sent before proceeding
    except asyncio.CancelledError:
        print("Connection was cancelled")

    # Close the connection
    print("Closing connection")
    writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, 'localhost', 6379
    )
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
