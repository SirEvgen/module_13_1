import asyncio


async def start_strongman(name, power):
    time_power = 1 / (power * 5)
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(time_power)
        print(f'Силач {name} поднял {i + 1}-ый шар' )
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vasya', 5))
    task2 = asyncio.create_task(start_strongman('Petya', 4))
    task3 = asyncio.create_task(start_strongman('Pasha', 3))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())