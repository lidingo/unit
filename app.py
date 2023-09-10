async def application(scope, receive, send):
    # See https://asgi.readthedocs.io/en/latest/specs/lifespan.html
    if scope['type'] == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                ...  # Do some startup here!
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                ...  # Do some shutdown here!
                await send({'type': 'lifespan.shutdown.complete'})
                return

    await send({
        'type': 'http.response.start',
        'status': 200
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, ASGI\n'
    })
