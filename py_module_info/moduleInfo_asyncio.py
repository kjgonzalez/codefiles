'''
similar to multithreading, but *NOT* actually multithreading, at least to the user.
more info: https://realpython.com/async-io-python/

note that coroutines and asyncio also have their own queues & producers+consumers

'''

import time
import asyncio

### normal (synchronous) version ###
def count_normal():
    print("one")
    time.sleep(1)
    print("two")
    time.sleep(1)

def main_normal():
    t0 = time.perf_counter()
    for i in range(3):
        count_normal()
    dt = time.perf_counter() - t0
    print(f"normal ran in {dt:0.4} s")

### async version ###
async def count_async():
    print("one")
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)

async def main_async():
    t0=time.perf_counter()
    await asyncio.gather(count_async(),count_async(),count_async()) # baseline version
    dt = time.perf_counter() - t0
    print(f'async ran in {dt:0.4} s')

# how can we "gather" an unknown /



if(__name__ == '__main__'):
    print('skipping synchronous version for now, too slow')
    #main_normal()
    asyncio.run(main_async())










# eof
