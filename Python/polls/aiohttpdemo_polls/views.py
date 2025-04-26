# aiohttpdemo_polls/views.py
import aiohttp.web_request
import aiohttp_jinja2

questions_data = [
    {"title": "foo", "text": "this is a question?"},
    {"title": "bar", "text": "this is a jazzy fizzle?"},
]


@aiohttp_jinja2.template("index.html")
async def index(request: aiohttp.web_request.Request):
    print(request.url)
    questions = questions_data
    return {"questions": questions}
