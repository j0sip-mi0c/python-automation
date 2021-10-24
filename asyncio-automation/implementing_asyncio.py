import asyncio
import time

#SYNCHRONOUS
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')

#ASYNCHRONOUS
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)
    print('two ', end='')

async def main():
    #tasks = [async_f(), async_f(), asyncio] #same as below code
    tasks = [async_f() for _ in range(3)]

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f'Execution time: {end - start}')
print('\n')

start = time.time()
for _ in range(3):
    sync_f()
end = time.time()
print(f'Execution time: {end - start}')

'''   
async def f():
    pass

async def g():
    await f()  #pause here and come back to g() when f() is ready

'''


