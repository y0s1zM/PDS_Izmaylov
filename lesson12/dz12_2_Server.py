import asyncio

async def handle_client(reader, writer):
    # Отримуємо два числа від клієнта
    data = await reader.read(100)
    numbers = data.decode().strip().split(",")
    num1, num2 = int(numbers[0]), int(numbers[1])

    # Виконуємо операції та відправляємо результат клієнту
    result_add = await add(num1, num2)
    result_sub = await subtract(num1, num2)
    result_mul = await multiply(num1, num2)
    writer.write(f"{result_add},{result_sub},{result_mul}".encode())
    await writer.drain()

    # Закриваємо з'єднання
    writer.close()

async def add(num1, num2):
    return num1 + num2

async def subtract(num1, num2):
    return num1 - num2

async def multiply(num1, num2):
    return num1 * num2

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
