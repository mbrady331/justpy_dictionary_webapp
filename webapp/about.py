import justpy as jp
from webapp import layout

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a= wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-4')
        jp.Div(a=div, text="This is the About Page", classes='text-4xl m-2')
        jp.Div(a=div, text="""
        This webapp instantly returns the definition(s) of a word that is typed in.
        """, classes='text-lg')

        return wp


