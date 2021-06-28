import justpy as jp
from webapp import layout

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a= wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-4')
        jp.Div(a=div, text="This is the Home Page", classes='text-4xl m-2')
        jp.Div(a=div, text="""
        Homepage for the Instant Dictionary web app.
        """, classes='text-lg')

        return wp

