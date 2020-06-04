#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 14, 2019 11:51:14 PM +0530  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox,OptionMenu,StringVar
import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def buySubmit(self):
        # bnifty = self.
        Risk = self.RiskBuy.get()
        Spotlow = self.SpotlowBuy.get()
        Optionlow = self.OptionlowBuy.get()


        # print(Risk,Spotlow,Optionlow)

    def sellSubmit(self):
        Risk = self.RiskSell.get()
        Spothigh = self.SpothighSell.get()
        Optionlow = self.OptionlowSell.get()
        


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI Semibold} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+278+154")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.033, rely=0.022, relheight=0.947
                , relwidth=0.94)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="BUY",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#008000")
        self.TNotebook1_t0.configure(highlightbackground="#008000")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="SELL",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#ff0000")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(self.TNotebook1_t0)
        self.Frame2.place(relx=0.018, rely=0.025, relheight=0.938
                , relwidth=0.955)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.var_banknifty = StringVar(self.Frame2)
        self.var_banknifty.set("Banknifty") # initial value

        self.banknifty = OptionMenu(self.Frame2, self.var_banknifty, "Banknifty", "Nifty")
        self.banknifty.place(relx=0.10, rely=0.192, height=24, width=200)

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.187, rely=0.16, height=27, width=60)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Risk''')

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.168, rely=0.347, height=27, width=100)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Spot Low''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.131, rely=0.587, height=27, width=100)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Option Low''')
       

        self.RiskBuy = tk.Entry(self.Frame2)
        self.RiskBuy.place(relx=0.467, rely=0.16,height=30, relwidth=0.4)
        self.RiskBuy.configure(background="white")
        self.RiskBuy.configure(disabledforeground="#a3a3a3")
        self.RiskBuy.configure(font="TkFixedFont")
        self.RiskBuy.configure(foreground="#000000")
        self.RiskBuy.configure(insertbackground="black")


        self.SpotlowBuy = tk.Entry(self.Frame2)
        self.SpotlowBuy.place(relx=0.467, rely=0.373,height=30, relwidth=0.4)
        self.SpotlowBuy.configure(background="white")
        self.SpotlowBuy.configure(disabledforeground="#a3a3a3")
        self.SpotlowBuy.configure(font="TkFixedFont")
        self.SpotlowBuy.configure(foreground="#000000")
        self.SpotlowBuy.configure(insertbackground="black")


        self.OptionlowBuy = tk.Entry(self.Frame2)
        self.OptionlowBuy.place(relx=0.467, rely=0.587,height=30, relwidth=0.4)
        self.OptionlowBuy.configure(background="white")
        self.OptionlowBuy.configure(disabledforeground="#a3a3a3")
        self.OptionlowBuy.configure(font="TkFixedFont")
        self.OptionlowBuy.configure(foreground="#000000")
        self.OptionlowBuy.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.486, rely=0.8, height=44, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#008000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''START''')
        self.Button1.configure(command = self.buySubmit)
        

        self.Frame1 = tk.Frame(self.TNotebook1_t1)
        self.Frame1.place(relx=0.018, rely=0.025, relheight=0.938
                , relwidth=0.955)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.187, rely=0.16, height=27, width=60)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Risk''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.168, rely=0.347, height=27, width=100)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Spot High''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.131, rely=0.587, height=27, width=100)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Option Low''')

        self.RiskSell = tk.Entry(self.Frame1)
        self.RiskSell.place(relx=0.505, rely=0.133,height=30, relwidth=0.344)
        self.RiskSell.configure(background="white")
        self.RiskSell.configure(disabledforeground="#a3a3a3")
        self.RiskSell.configure(font="TkFixedFont")
        self.RiskSell.configure(foreground="#000000")
        self.RiskSell.configure(insertbackground="black")

        self.SpothighSell = tk.Entry(self.Frame1)
        self.SpothighSell.place(relx=0.505, rely=0.32,height=30, relwidth=0.344)
        self.SpothighSell.configure(background="white")
        self.SpothighSell.configure(disabledforeground="#a3a3a3")
        self.SpothighSell.configure(font="TkFixedFont")
        self.SpothighSell.configure(foreground="#000000")
        self.SpothighSell.configure(insertbackground="black")

        self.OptionlowSell = tk.Entry(self.Frame1)
        self.OptionlowSell.place(relx=0.505, rely=0.507,height=30, relwidth=0.344)
        self.OptionlowSell.configure(background="white")
        self.OptionlowSell.configure(disabledforeground="#a3a3a3")
        self.OptionlowSell.configure(font="TkFixedFont")
        self.OptionlowSell.configure(foreground="#000000")
        self.OptionlowSell.configure(insertbackground="black")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.523, rely=0.747, height=35, width=122)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#f5010a")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''START''')

if __name__ == '__main__':
    vp_start_gui()




