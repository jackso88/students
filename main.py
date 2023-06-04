import asyncio
import tornado.web
from tornado.web import url
from view import SearchView, CreateView, DeleteView, UpdateView
import json
from jinja2 import Template

html = open('HTML/index.html').read()
template = Template(html)


class CreateHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><meta charset="utf-8">'
                   '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
                   '<body><form action="/create" method="POST">'
                   '<input type="text" name="text">'
                   '<input type="date" name="date">'
                   '<input type="text" name="rubrics">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    async def post(self):
        request = {
            "text": self.get_body_argument("text"),
            "created_date": self.get_argument("date"),
            "rubrics": self.get_argument("rubrics")
        }
        view = CreateView(request)
        response = await view.create()
        self.write(template.render(items=response))


class SearchHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><meta charset="utf-8">'
                   '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
                   '<body><form action="/" method="POST">'
                   '<input type="text" name="search">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    async def post(self):
        request = self.get_body_argument("search")
        view = SearchView(request)
        response = await view.search()
        if response == []:
            self.write('Такого не существует')
        else:
            self.write(template.render(items=response))


class DeleteHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><meta charset="utf-8">'
                   '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
                   '<body><form action="/delete" method="POST">'
                   '<input type="text" name="delete">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    async def post(self):
        request = self.get_body_argument("delete")
        view = DeleteView(request)
        response = await view.delete()
        self.write(template.render(items=response))


class UpdateHandle(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><meta charset="utf-8">'
                   '<meta http-equiv="X-UA-Compatible" content="IE=edge">'
                   '<body><form action="/create" method="POST">'
                   '<input type="id" name="id">'
                   '<input type="text" name="text">'
                   '<input type="date" name="date">'
                   '<input type="text" name="rubrics">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    async def post(self):
        request = {
            "id": self.get_argument('id'),
            "val": {
                "text": self.get_body_argument("text"),
                "created_date": self.get_argument("date"),
                "rubrics": self.get_argument("rubrics")
            }
        }
        view = UpdateView(request)
        response = await view.update()
        self.write(template.render(items=response))


urls = [
    url(r"/", SearchHandle),
    url(r"/create", CreateHandle),
    url(r"/delete", DeleteHandle),
    url(r"/update", UpdateHandle),
]


def make_app():
    return tornado.web.Application(urls)


async def main():
    app = make_app()
    app.listen(8010)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
