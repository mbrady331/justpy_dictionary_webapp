import justpy as jp

class Home:
    path = '/'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="This is the Home Page", classes='text-4xl m-2')
        jp.Div(a=div, text="""
        I'm baby disrupt occaecat migas stumptown truffaut meditation scenester deserunt gluten-free shaman
         fingerstache humblebrag tumeric ullamco. Poutine prism succulents meditation nisi gluten-free chia
          incididunt officia est. Sunt laborum veniam stumptown master cleanse austin af ea shabby chic offal
           affogato everyday carry. Organic hella lorem, seitan put a bird on it tattooed in readymade.
        """, classes='text-lg')

        return wp


