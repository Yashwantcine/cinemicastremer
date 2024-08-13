import ssl
from aiohttp import web
from .stream_routes import routes

async def web_server():
    # Initialize the web application
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)

    # Set up SSL context
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(
        certfile='biisal/server/ssl_cert/certificate.crt', 
        keyfile='biisal/server/ssl_cert/private.key'
    )

    # Load CA Bundle
    ssl_context.load_verify_locations(cafile='biisal/server/ssl_cert/ca_bundle.crt')

    # Return the application and SSL context
    return web_app, ssl_context

if __name__ == "__main__":
    app, ssl_context = web_server()
    web.run_app(app, port=9010, ssl_context=ssl_context)
