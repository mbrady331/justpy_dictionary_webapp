import justpy as jp

class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a= wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="leftDrawerOpen",
                            side='left', bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)

        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'

        jp.A(a=qlist, text='Home', href='/', classes=a_classes)
        jp.Br(a=qlist)

        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.Br(a=qlist)

        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a= toolbar, dense=True, flat=True, round=True, icon='menu',
                click= cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-4')
        jp.Div(a=div, text="This is the Home Page", classes='text-4xl m-2')
        jp.Div(a=div, text="""
        I'm baby disrupt occaecat migas stumptown truffaut meditation scenester deserunt gluten-free shaman
         fingerstache humblebrag tumeric ullamco. Poutine prism succulents meditation nisi gluten-free chia
          incididunt officia est. Sunt laborum veniam stumptown master cleanse austin af ea shabby chic offal
           affogato everyday carry. Organic hella lorem, seitan put a bird on it tattooed in readymade.
        """, classes='text-lg')

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value == True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
