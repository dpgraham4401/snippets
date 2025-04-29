# aiohttpdemo_polls/main.py
import aiohttp_jinja2
import jinja2
from aiohttp import web
from middleware import setup_middlewares
from routes import setup_routes
from settings import BASE_DIR, config

app = web.Application()
setup_routes(app)
setup_middlewares(app)
app["config"] = config  # Don't need this but still good to know.
aiohttp_jinja2.setup(
    app, loader=jinja2.FileSystemLoader(str(BASE_DIR / "aiohttpdemo_polls" / "templates"))
)
web.run_app(app)
