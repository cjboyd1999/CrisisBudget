from ausIndividual import *
from ausBusiness import *
from ukIndividual import *
from ukBusiness import *
from usIndividual import *
from usBusiness import *

def RunQ3(window, canvas, country, personType):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)

    if country == 0:
        if personType == 0:
            AusBusiness(window, canvas)
        elif personType == 1:
            AusIndividual(window, canvas)

    elif country == 1:
        if personType == 0:
            UkBusiness(window, canvas)
        elif personType == 1:
            UkIndividual(window, canvas)

    elif country == 2:
        if personType == 0:
            UsBusiness(window, canvas)
        elif personType == 1:
            UsIndividual(window, canvas)