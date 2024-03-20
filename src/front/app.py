# Interface graphique avec Tkinter------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color

from src.back.pricer import *
from src.front.window import WindowMain


'''
class _ChoiceScroll:
    pass

class _UnderlyingScroll(_ChoiceScroll):
    def __init__(self, name):
        self.name = name


class EquityScroll(_UnderlyingScroll):
    def __init__(self):
    
        self.name = "Equity"


def factory_choice_scroll(name):
    if name == "Equity":
        return EquityScroll()
'''    

"""

#Cette fonction modifie l'interface interactive en fonction du sous-jacent et du modèle sélectionnés pour la tab1
#cacher l'imply volatility quand c'est pas equity avec BS
def interfaceAmend(event):
        # ut2 = ut.get()
        #ut2 = factory_choice_scroll(ut.get())
        ut2 = ut.get()
        ot2 = ot.get()
        if (ut2 == "Equity" and ot2 == "Black Scholes European"):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid_forget()
            optionalEntry21.grid_forget()
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Equity" and (ot2 == "Binomial European" or ot2 == "Binomial American")):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid(column = 0,row = 9,padx = 1,pady = 1)
            optionalLabel2.set("Tree Steps:")
            optionalEntry21.grid(column = 1,row = 9,padx = 1,pady = 1)
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Equity" and ot2 == "Asian"):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid(column = 0,row = 9,padx = 1,pady = 1)
            optionalLabel2.set("Time since Inception:")
            optionalEntry21.grid(column = 1,row = 9,padx = 1,pady = 1)
            optionalLabel31.grid(column = 0,row = 10,padx = 1,pady = 1)
            optionalLabel3.set("Current Average:")
            optionalEntry31.grid(column = 1,row = 10,padx = 1,pady = 1)
        elif (ut2 == "Equity" and (ot2 == "Barrier Up And In" or ot2 == "Barrier Up And Out" or ot2 == "Barrier Down And In" or ot2 == "Barrier Down And Out")):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid(column = 0,row = 9,padx = 1,pady = 1)
            optionalLabel2.set("Barrier:")
            optionalEntry21.grid(column = 1,row = 9,padx = 1,pady = 1)
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing"):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid(column = 0,row = 9,padx = 1,pady = 1)
            optionalLabel2.set("Cash Amount:")
            optionalEntry21.grid(column = 1,row = 9,padx = 1,pady = 1)
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing"):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid_forget()
            optionalEntry21.grid_forget()
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Currency" and ot2 == "Black Scholes European"):
            optionalLabel11.grid(column = 0,row = 5,padx = 1,pady = 1)
            optionalLabel1.set("Foreign RFR (% per year):")
            optionalEntry11.grid(column = 1,row = 5,padx = 1,pady = 1)
            optionalLabel21.grid_forget()
            optionalEntry21.grid_forget()
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Index" and ot2 == "Black Scholes European"):
            optionalLabel11.grid(column = 0,row = 5,padx = 1,pady = 1)
            optionalLabel1.set("Dividend Yield (% per year):")
            optionalEntry11.grid(column = 1,row = 5,padx = 1,pady = 1)
            optionalLabel21.grid_forget()
            optionalEntry21.grid_forget()
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
        elif (ut2 == "Futures" and ot2 == "Black Scholes European"):
            optionalLabel11.grid_forget()
            optionalEntry11.grid_forget()
            optionalLabel21.grid_forget()
            optionalEntry21.grid_forget()
            optionalLabel31.grid_forget()
            optionalEntry31.grid_forget()
"""

        
#Cette fonction modifie l'interface interactive en fonction du sous-jacent et du modèle sélectionnés pour la tab2
#cacher l'imply volatility quand c'est pas equity avec BS
def interfaceAmendTab2(event):
        ut2_tab2 = ut_tab2.get()
        ot2_tab2 = ot_tab2.get()
        mt2_tab2 = mt_tab2.get()
        if (ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal"):
            optionalLabel11_tab2.grid_forget()
            optionalEntry11_tab2.grid_forget()
            optionalLabel21_tab2.grid_forget()
            optionalEntry21_tab2.grid_forget()
            optionalLabel31_tab2.grid_forget()
            optionalEntry31_tab2.grid_forget()
        elif (ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion"):
            optionalLabel11_tab2.grid(column = 2,row = 8,padx = 1,pady = 1)
            optionalLabel1_tab2.set("Jumps per Year : ")
            optionalEntry11_tab2.grid(column = 3,row = 8,padx = 1,pady = 1)
            optionalLabel21_tab2.grid(column = 2,row = 9,padx = 1,pady = 1)
            optionalLabel2_tab2.set("Average Jump Size (%): ")
            optionalEntry21_tab2.grid(column = 3,row = 9,padx = 1,pady = 1)
            optionalLabel31_tab2.grid(column = 2,row = 10,padx = 1,pady = 1)
            optionalLabel3_tab2.set("Jump Std Deviation (%): ")
            optionalEntry31_tab2.grid(column = 3,row = 10,padx = 1,pady = 1)

# N'est pas exécuté lors de l'import
if __name__ == '__main__':
    #Création de la fenêtre intéractive
    fenetre = WindowMain()

    tab1 = fenetre.get_tab(name='Options calculator')
    tab2 = fenetre.get_tab(name='Monte Carlo', title="Pricing Options by Monte Carlo Simulation")
    tab3 = fenetre.get_tab(name='Bonds calculator', title="Bond Price Calculator")
    tab4 = fenetre.get_tab(name='Swaps calculator', title="Swap Price Calculator")
    tab5 = fenetre.get_tab(name='Rates Curve', title="EUR Rates Curve")

    fenetre.notebook.pack(expand = 1, fill ="both")

    #Options calculator widgets - tab1--------------------------------------------------------------------------------------------------------------------------------------------------------
    tab1.label_titre.grid(column = 1,row = 0,padx = 20,pady = 20)


    def callback_option_calculation():
        ut2 = tab1.ut.get()
        stop2 = tab1.stop.get()
        vol2 = tab1.vol.get() / 100
        rfr2 = tab1.rfr.get() / 100
        ot2 = tab1.ot.get()
        lif2 = tab1.lif.get()
        strp2 = tab1.strp.get()
        valueRB2 = tab1.valueRB.get()
        valueCB2 = tab1.valueCB.get()
        

        p, d, g, v, t, r = option_calculation(ut2, stop2, vol2, rfr2, ot2, lif2, strp2, valueRB2,valueCB2)
        
        tab1.valuePrice.set(round(p,5))
        tab1.valueDelta.set(round(d,5))
        tab1.valueGamma.set(round(g,5))
        tab1.valueVega.set(round(v,5))
        tab1.valueTheta.set(round(t,5))
        tab1.valueRho.set(round(r,5))

    ttk.Button(tab1,text = "CALCULATE",command=callback_option_calculation).grid(column = 0,row = 11,padx = 12,pady = 12)



    #Monte Carlo widgets - tab2--------------------------------------------------------------------------------------------------------------------------------------------------------

    tab2.label_titre.grid(columnspan = 5,row = 0,padx = 20,pady = 20)  

    ttk.Label(tab2,text ="Underlying Type: ",font='Helvetica 10 bold').grid(column = 0,row = 1,padx = 12,pady = 12)  
    ttk.Label(tab2,text ="Stock Price: ").grid(column = 0,row = 2,padx = 1,pady = 1)  
    ttk.Label(tab2,text ="Risk-Free Rate (% per year): ").grid(column = 0,row = 3,padx = 1,pady = 1)
    ttk.Label(tab2,text ="Dividend Yield (% per year): ").grid(column = 0,row = 4,padx = 1,pady = 1)
    ttk.Label(tab2,text ="Simulation Data: ",font='Helvetica 10 bold').grid(column = 0,row = 6,padx = 12,pady = 12)  
    ttk.Label(tab2,text ="Number of Time Steps: ").grid(column = 0,row = 7,padx = 1,pady = 1)  
    ttk.Label(tab2,text ="Number of Simulations: ").grid(column = 0,row = 8,padx = 1,pady = 1)
    ttk.Label(tab2,text ="Random Seed: ").grid(column = 0,row = 9,padx = 1,pady = 1)
    ttk.Button(tab2,text = "CALCULATE", command=option_calculation_tab2).grid(column = 0,row = 13,padx = 1,pady = 11)

    ut_tab2 = StringVar()
    ut1_tab2 = ttk.Combobox(tab2, values=["Equity"], textvariable=ut_tab2)
    ut1_tab2.current(0)
    ut1_tab2.grid(column = 1,row = 1,padx = 12,pady = 12) 
    ut1_tab2.bind("<<ComboboxSelected>>", interfaceAmendTab2)
    stop_tab2 = DoubleVar()
    stop1_tab2 = ttk.Entry(tab2, textvariable=stop_tab2).grid(column = 1,row = 2,padx = 1,pady = 1)  
    rfr_tab2 = DoubleVar()
    rfr1_tab2 = ttk.Entry(tab2, textvariable=rfr_tab2).grid(column = 1,row = 3,padx = 1,pady = 1) 
    div_tab2 = DoubleVar()
    div1_tab2 = ttk.Entry(tab2, textvariable=div_tab2).grid(column = 1,row = 4,padx = 1,pady = 1)
    nts_tab2 = IntVar()
    nts1_tab2 = ttk.Entry(tab2, textvariable=nts_tab2).grid(column = 1,row = 7,padx = 1,pady = 1)  
    nos_tab2 = IntVar()
    nos1_tab2 = ttk.Entry(tab2, textvariable=nos_tab2).grid(column = 1,row = 8,padx = 1,pady = 1) 
    rans_tab2 = IntVar()
    rans1_tab2 = ttk.Entry(tab2, textvariable=rans_tab2).grid(column = 1,row = 9,padx = 1,pady = 1)



    ttk.Label(tab2,text ="Option Type: ",font='Helvetica 10 bold').grid(column = 2,row = 1,padx = 12,pady = 12)  
    ttk.Label(tab2,text ="Life (years): ").grid(column = 2,row = 2,padx = 1,pady = 1)  
    ttk.Label(tab2,text ="Strike Price: ").grid(column = 2,row = 3,padx = 1,pady = 1)
    ttk.Label(tab2,text ="Model Type: ").grid(column = 2,row = 6,padx = 1,pady = 1)
    ttk.Label(tab2,text ="Volatility (% per year): ").grid(column = 2,row = 7,padx = 1,pady = 1)
    optionalLabel1_tab2 = StringVar()
    optionalLabel11_tab2 = ttk.Label(tab2,textvariable=optionalLabel1_tab2)
    optionalLabel2_tab2 = StringVar()
    optionalLabel21_tab2 = ttk.Label(tab2,textvariable=optionalLabel2_tab2)
    optionalLabel3_tab2 = StringVar()
    optionalLabel31_tab2 = ttk.Label(tab2,textvariable=optionalLabel3_tab2)
    ttk.Label(tab2,text ="Price: ").grid(column = 2,row = 13,padx = 1,pady = 1)  
    ttk.Label(tab2,text ="Standard Error: ").grid(column = 2,row = 14,padx = 1,pady = 1)

    ot_tab2 = StringVar()
    ot1_tab2 = ttk.Combobox(tab2, values=["European"], textvariable=ot_tab2)
    ot1_tab2.current(0)
    ot1_tab2.grid(column = 3,row = 1,padx = 12,pady = 12)
    ot1_tab2.bind("<<ComboboxSelected>>", interfaceAmendTab2)
    lif_tab2 = DoubleVar()
    lif1_tab2 = ttk.Entry(tab2, textvariable=lif_tab2).grid(column = 3,row = 2,padx = 1,pady = 1)  
    strp_tab2 = DoubleVar()
    strp1_tab2 = ttk.Entry(tab2, textvariable=strp_tab2).grid(column = 3,row = 3,padx = 1,pady = 1)  
    mt_tab2 = StringVar()
    mt1_tab2 = ttk.Combobox(tab2, values=["Log Normal", "Merton Jump Diffusion"], textvariable=mt_tab2)
    mt1_tab2.current(0)
    mt1_tab2.grid(column = 3,row = 6,padx = 12,pady = 12)
    mt1_tab2.bind("<<ComboboxSelected>>", interfaceAmendTab2)
    vol_tab2 = DoubleVar()
    vol1_tab2 = ttk.Entry(tab2, textvariable=vol_tab2).grid(column = 3,row = 7,padx = 1,pady = 1)  
    optionalEntry1_tab2 = DoubleVar()
    optionalEntry11_tab2 = ttk.Entry(tab2, textvariable=optionalEntry1_tab2)
    optionalEntry2_tab2 = DoubleVar()
    optionalEntry21_tab2 = ttk.Entry(tab2, textvariable=optionalEntry2_tab2)
    optionalEntry3_tab2 = DoubleVar()
    optionalEntry31_tab2= ttk.Entry(tab2, textvariable=optionalEntry3_tab2)
    pri_tab2 = DoubleVar()
    pro1_tab2 = ttk.Entry(tab2, textvariable=pri_tab2).grid(column = 3,row = 13,padx = 1,pady = 1)  
    stae_tab2 = DoubleVar()
    stae1_tab2 = ttk.Entry(tab2, textvariable=stae_tab2).grid(column = 3,row = 14,padx = 1,pady = 1)  

    valueRB_tab2 = IntVar()
    cal_tab2 = Radiobutton(tab2, text="Call", variable = valueRB_tab2, value=0).grid(column = 4,row = 2,padx = 1,pady = 1)
    put_tab2 = Radiobutton(tab2, text="Put", variable = valueRB_tab2, value=1).grid(column = 4,row = 3,padx = 1,pady = 1)




    #Bonds calculator widgets - tab3--------------------------------------------------------------------------------------------------------------------------------------------------------

    tab3.label_titre.grid(columnspan = 4,row = 0,padx = 20,pady = 20) 

    ttk.Label(tab3,text ="Principal:").grid(column = 0,row = 1,padx = 12,pady = 12)  
    ttk.Label(tab3,text ="Bond Life (Years):").grid(column = 0,row = 2,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Coupon Rate (%):").grid(column = 0,row = 3,padx = 1,pady = 1)
    ttk.Label(tab3,text ="Settlement Frequency:").grid(column = 0,row = 4,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Results ",font='Helvetica 10 bold').grid(column = 0,row = 12,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Price:").grid(column = 0,row = 13,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Yield to Maturity:").grid(column = 0,row = 14,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Duration:").grid(column = 0,row = 15,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Modified Duration:").grid(column = 0,row = 16,padx = 1,pady = 1)  
    ttk.Label(tab3,text ="Convexity:").grid(column = 0,row = 17,padx = 1,pady = 1)  

    pri_tab3 = DoubleVar()
    pri1_tab3 = ttk.Entry(tab3, textvariable=pri_tab3).grid(column = 1,row = 1,padx = 1,pady = 1) 
    bonl_tab3 = DoubleVar()
    bonl1_tab3 = ttk.Entry(tab3, textvariable=bonl_tab3).grid(column = 1,row = 2,padx = 1,pady = 1) 
    cour_tab3 = DoubleVar()
    cour1_tab3 = ttk.Entry(tab3, textvariable=cour_tab3).grid(column = 1,row = 3,padx = 1,pady = 1) 
    setf = StringVar()
    setf1 = ttk.Combobox(tab3, values=["Monthly", "Quarterly", "Semi-Annual", "Annual"], textvariable=setf)
    setf1.current(0)
    setf1.grid(column = 1,row = 4,padx = 12,pady = 12)

    pri_tab3 = DoubleVar()
    pri1_tab3 = ttk.Entry(tab3, textvariable=pri_tab3).grid(column = 1,row = 13,padx = 1,pady = 1) 
    ytm_tab3 = DoubleVar()
    ytm1_tab3 = ttk.Entry(tab3, textvariable=ytm_tab3).grid(column = 1,row = 14,padx = 1,pady = 1) 
    dur_tab3 = DoubleVar()
    dur1_tab3 = ttk.Entry(tab3, textvariable=dur_tab3).grid(column = 1,row = 15,padx = 1,pady = 1) 
    mdur_tab3 = DoubleVar()
    mdur1_tab3 = ttk.Entry(tab3, textvariable=mdur_tab3).grid(column = 1,row = 16,padx = 1,pady = 1) 
    con_tab3 = DoubleVar()
    con1_tab3 = ttk.Entry(tab3, textvariable=con_tab3).grid(column = 1,row = 17,padx = 1,pady = 1) 


    ttk.Label(tab3,text ="Zeros:",font='Helvetica 10 bold').grid(column = 3,row = 1,padx = 1,pady = 1)  

    rates1_tab3 = DoubleVar()
    rates1_1_tab3 = ttk.Entry(tab3, textvariable=rates1_tab3).grid(column = 3,row = 2,padx = 1,pady = 1) 
    rates2_tab3 = DoubleVar()
    rates21_tab3 = ttk.Entry(tab3, textvariable=rates2_tab3).grid(column = 3,row = 3,padx = 1,pady = 1) 
    rates3_tab3 = DoubleVar()
    rates31_tab3 = ttk.Entry(tab3, textvariable=rates3_tab3).grid(column = 3,row = 4,padx = 1,pady = 1) 
    rates4_tab3 = DoubleVar()
    rates41_tab3 = ttk.Entry(tab3, textvariable=rates4_tab3).grid(column = 3,row = 5,padx = 1,pady = 1) 
    rates5_tab3 = DoubleVar()
    rates51_tab3 = ttk.Entry(tab3, textvariable=rates5_tab3).grid(column = 3,row = 6,padx = 1,pady = 1) 
    rates6_tab3 = DoubleVar()
    rates61_tab3 = ttk.Entry(tab3, textvariable=rates6_tab3).grid(column = 3,row = 7,padx = 1,pady = 1) 
    rates7_tab3 = DoubleVar()
    rates71_tab3 = ttk.Entry(tab3, textvariable=rates7_tab3).grid(column = 3,row = 8,padx = 1,pady = 1) 
    rates8_tab3 = DoubleVar()
    rates81_tab3 = ttk.Entry(tab3, textvariable=rates8_tab3).grid(column = 3,row = 9,padx = 1,pady = 1) 
    rates9_tab3 = DoubleVar()
    rates91_tab3 = ttk.Entry(tab3, textvariable=rates9_tab3).grid(column = 3,row = 10,padx = 1,pady = 1) 
    rates10_tab3 = DoubleVar()
    rates101_tab3 = ttk.Entry(tab3, textvariable=rates10_tab3).grid(column = 3,row =11,padx = 1,pady = 1) 
    rates11_tab3 = DoubleVar()
    rates111_tab3 = ttk.Entry(tab3, textvariable=rates11_tab3).grid(column = 3,row = 12,padx = 1,pady = 1) 
    rates12_tab3 = DoubleVar()
    rates121_tab3 = ttk.Entry(tab3, textvariable=rates12_tab3).grid(column = 3,row = 13,padx = 1,pady = 1) 

    ttk.Button(tab3,text = "CALCULATE").grid(column = 3,row = 15,padx = 1,pady = 11)


    #Swaps calculator widgets - tab4--------------------------------------------------------------------------------------------------------------------------------------------------------

    tab4.label_titre.grid(columnspan = 4,row = 0,padx = 20,pady = 20) 

    from tkcalendar import DateEntry

    ttk.Label(tab4,text ="Start Date:").grid(column = 0,row = 1,padx = 1,pady = 1) 
    startDate=StringVar() # declaring string variable
    cal1=DateEntry(tab4,selectmode='day',textvariable=startDate)
    cal1.grid(column = 1,row = 1,padx = 1,pady = 1)
    ttk.Label(tab4,text ="End date:").grid(column = 2,row = 1,padx = 1,pady = 1) 
    endDate=StringVar() # declaring string variable 
    cal2=DateEntry(tab4,selectmode='day',textvariable=endDate)
    cal2.grid(column = 3,row = 1,padx = 1,pady = 1)

    valueRB_tab4 = IntVar()
    rec_tab4 = Radiobutton(tab4, text="Rec Fixed", variable = valueRB_tab4, value=0).grid(column = 0,row = 2,padx = 1,pady = 1)
    pay_tab4 = Radiobutton(tab4, text="Pay Fixed", variable = valueRB_tab4 , value=1).grid(column = 2,row = 2,padx = 1,pady = 1)


    #Fixed leg:
    ttk.Label(tab4,text ="Notional fixed leg:").grid(column = 0,row =3,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Fixed Rate (%):").grid(column = 0,row = 4,padx = 1,pady = 1)
    ttk.Label(tab4,text ="Settlement Frequency:").grid(column = 0,row = 5,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Basis:").grid(column = 0,row = 6,padx = 1,pady = 1) 
    not1_tab4 = DoubleVar()
    not11_tab4 = ttk.Entry(tab4, textvariable=not1_tab4).grid(column = 1,row = 3,padx = 1,pady = 1) 
    rat1_tab4 = DoubleVar()
    rat11_tab4 = ttk.Entry(tab4, textvariable=rat1_tab4).grid(column = 1,row = 4,padx = 1,pady = 1) 
    setf1 = StringVar()
    setf11 = ttk.Combobox(tab4, values=["Daily", "Monthly", "Quarterly", "Semi-Annual", "Annual", "ZC"], textvariable=setf1)
    setf11.current(0)
    setf11.grid(column = 1,row = 5,padx = 1,pady = 1)
    bas1 = StringVar()
    bas11 = ttk.Combobox(tab4, values=["A360", "A365", "30/360"], textvariable=bas1)
    bas11.current(0)
    bas11.grid(column = 1,row = 6,padx = 1,pady = 1) 

    #Float leg
    ttk.Label(tab4,text ="Notional float leg:").grid(column = 2,row = 3,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Float Rate:").grid(column = 2,row = 4,padx = 1,pady = 1)
    ttk.Label(tab4,text ="Settlement Frequency:").grid(column = 2,row = 5,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Basis:").grid(column = 2,row = 6,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Last Euribor (%):").grid(column = 2,row = 7,padx = 1,pady = 1)  
    not2_tab4 = DoubleVar()
    not21_tab4 = ttk.Entry(tab4, textvariable=not2_tab4).grid(column = 3,row = 3,padx = 1,pady = 1) 
    setf2 = StringVar()
    setf21 = ttk.Combobox(tab4, values=["ESTER","EURIB1","EURIB3","EURIB6","EURIB12"], textvariable=setf2)
    setf21.current(0)
    setf21.grid(column = 3,row = 4,padx = 1,pady = 1)
    setf3 = StringVar()
    setf31 = ttk.Combobox(tab4, values=["Daily", "Monthly", "Quarterly", "Semi-Annual", "Annual", "ZC"], textvariable=setf3)
    setf31.current(0)
    setf31.grid(column = 3,row = 5,padx = 1,pady = 1)
    bas2 = StringVar()
    bas21 = ttk.Combobox(tab4, values=["A360", "A365", "30/360"], textvariable=bas2)
    bas21.current(0)
    bas21.grid(column = 3,row = 6,padx = 1,pady = 1) 
    lase_tab4 = DoubleVar()
    lase1_tab4 = ttk.Entry(tab4, textvariable=lase_tab4).grid(column = 3,row = 7,padx = 1,pady = 1) 

    #Result
    ttk.Label(tab4,text ="Results ",font='Helvetica 10 bold').grid(column = 0,row = 8,padx = 1,pady = 1)  
    ttk.Label(tab4,text ="Price (%):").grid(column = 0,row =9,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="Price (€):").grid(column = 0,row =10,padx = 1,pady = 1) 
    ttk.Label(tab4,text ="DV01 (Per basis point):").grid(column = 0,row =11,padx = 1,pady = 1) 
    pri1_tab4 = DoubleVar()
    pri11_tab4 = ttk.Entry(tab4, textvariable=pri1_tab4).grid(column = 1,row = 9,padx = 1,pady = 1) 
    pri2_tab4 = DoubleVar()
    pri21_tab4 = ttk.Entry(tab4, textvariable=pri2_tab4).grid(column = 1,row = 10,padx = 1,pady = 1) 
    sen_tab4 = DoubleVar()
    sen1_tab4 = ttk.Entry(tab4, textvariable=sen_tab4).grid(column = 1,row = 11,padx = 1,pady = 1) 
    ttk.Button(tab4,text = "Refresh Curve",command=refreshCurve).grid(column = 2,row = 9,padx = 1,pady = 1)
    ttk.Button(tab4,text = "CALCULATE",command=swapComputation).grid(column = 2,row = 11,padx = 1,pady = 1)


    #Swaps Rates Curve - tab5--------------------------------------------------------------------------------------------------------------------------------------------------------

    tab5.label_titre.grid(columnspan = 6,row = 0,padx = 20,pady = 20) 


    #Affichage de la fenêtre intéractive
    fenetre.mainloop()
