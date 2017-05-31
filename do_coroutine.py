# -*- coding: utf-8 -*-
#协程实现

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def goodbye():
    print('Googbye! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Goodbye again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), goodbye()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()