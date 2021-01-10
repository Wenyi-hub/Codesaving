from tkinter import *
import Pmw
root = Tk()
Pmw.initialize()
Pmw.aboutversion('1.5')
Pmw.aboutcopyright('Copyright company name\nAll rights reserved')
Pmw.aboutcontact('For information about this application contact:\n'+'sales at company Name\n'+'Phone:\n'+'E-mail:')
about = Pmw.Aboutdialog(root, applicationname = 'About dialog')
root.mainloop()