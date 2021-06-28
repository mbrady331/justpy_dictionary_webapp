import justpy as jp
import definition
from webapp import layout

class Dictionary:
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a= wp, view="hHh lpR fFf")
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-4')
        jp.Div(a=div, text="Instant English Dictionary", classes='text-4xl m-2')
        jp.Div(a=div, text="Get the definition of any English word instantly.", classes='text-2xl')

        input_div = jp.Div(a=div, classes=' grid grid-cols-2')

        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 border-gray-400 h-40')
        input_box = jp.Input(a=input_div, placeholder='Type in a word here...', outputdiv = output_div,
                             classes='m-2, bg-white border-2 border-gray-200 rounded w-64 '
                                     'focus:bg-white focus:outline-none focus:border-blue-500 py-2 px-4')
        input_box.on('input', cls.get_definition)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(term=widget.value.lower()).get()
        widget.outputdiv.text = " ".join(defined)
