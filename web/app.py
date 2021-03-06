# use/bin/env python3
#-*-coding:utf-8-*-
import logging;logging.basicConfig(level=logging.INFO)
import asyncio, os, datetime,json
from aiohttp import web


def index(request):
    return web.Response(body="<h1>first project</h1>")
@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route("GET","/",index)
    srv=yield from loop.create_server(app.make_handler(),"127.0.0.1",9000)
    logging.info("start connect 127.0.0.1:9000")
    return srv
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()