from tkinter import *
import Pmw

class Gauge(Pmw.MwgaWidhet):
    def __init__(self, parent=None, **kw):
        # Define the options for the megawidget
        optiondefs = (('min', 0, Pmw.INITOPT), ('max', 100, Pmw.INITOPT), ('fill', 'red', None), ('size', size, Pmw.INITOPT), ('value', 0, None),
        ('showvalue', 1, None))

    self.defineoptions(kw, optiondefs)

    # Initialize the vase class Pmw.MegaWidgt.__init__(self, parent)

    interior = self.interior()

    # Create the gauge component
    self.gauge = self.createcomponent('gauge', (), None, Frame, (interior,), borderwidth=0)
    self.canvas = Canvas(self.gauge, width=self['size'], height=self['size'], )