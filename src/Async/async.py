import asyncio

async def task1():
    print("Iniciando task1")
    await asyncio.sleep(1)
    print("task1 concluída")

async def task2():
    print("Iniciando task2")
    await asyncio.sleep(2)
    print("task2 concluída")

async def main():
    print("Chamando task1 e task2")
    await asyncio.gather(task1(), task2())
    print("task1 e task2 chamadas com sucesso")

asyncio.run(main())
