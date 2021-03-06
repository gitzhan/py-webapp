import logging; logging.basicConfig(level=logging.INFO)


import asyncio

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', charset='UTF-8', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    serv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8001)
    logging.info("server started at http://127.0.0.1:8001...")
    return serv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
