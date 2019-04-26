"""
    web启动类
"""
import logging; logging.basicConfig(level=logging.INFO)


import asyncio, os, json, time
from datetime import datetime


from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    # return web.Response(text="<h1>Awesome</h1>")
    return web.Response(body=b"<h1>Awesome</h1>", content_type='text/html')


def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port='8001')
    logging.info("server started at http://127.0.0.1:8001...")


init()
