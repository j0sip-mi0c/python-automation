import asyncio
import asyncssh

async def connect_and_run(host, username, password, commands):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        #result = await connection.run(command)
        #return result
        #run multiple commands
        results = []
        for cmd in commands:
            result = await connection.run(cmd)
            results.append(result)

        return results

commands = ('ifconfig', )  #run multiple commands
results = asyncio.run(connect_and_run('192.168.1.110', 'x', 'x', commands))
for result in results:
    print(f'STDOUT:\n {result.stdout}')
    print(f'STDERR:\n {result.stderr}')
    print('#'*50)