import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    # Відправляємо два числа на сервер
    num1, num2 = 10, 5
    writer.write(f"{num1},{num2}".encode())
    await writer.drain()

    # Отримуємо результати операцій від сервера
    data = await reader.read(100)
    results = data.decode().strip().split(",")
    result_add, result_sub, result_mul = int(results[0]), int(results[1]), int(results[2])

    # Друк результатів
    print(f"Додавання: {result_add}")
    print(f"Віднімання: {result_sub}")
    print(f"Множення: {result_mul}")

    # Закриваємо з'єднання
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_client())