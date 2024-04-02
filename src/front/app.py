# Interface graphique avec Tkinter------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color

from src.back.pricer import *
from src.front.window import WindowMain


# N'est pas exécuté lors de l'import
if __name__ == '__main__':
    #Création de la fenêtre intéractive
    fenetre = WindowMain()
    

    tab1 = fenetre.get_tab(name='Options calculator')
    #tab2 = fenetre.get_tab(name='Monte Carlo', title="Pricing Options by Monte Carlo Simulation")
    tab2 = fenetre.get_tab(name='Monte Carlo')
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
        
        #optional values
        ov1 = tab1.optionalEntry1.get()
        ov2 = tab1.optionalEntry2.get()
        ov3 = tab1.optionalEntry3.get()
        pri2 = tab1.valuePrice.get() 
        
        if valueCB2 == 0: 
             price, delta, gamma, vega, theta, rho = option_calculation(ut2,stop2,vol2,rfr2,ot2,lif2,strp2,valueRB2,valueCB2,ov1,ov2,ov3)
             tab1.valuePrice.set(round(price,5))
             tab1.valueDelta.set(round(delta,5))
             tab1.valueGamma.set(round(gamma,5))
             tab1.valueVega.set(round(vega,5))
             tab1.valueTheta.set(round(theta,5))
             tab1.valueRho.set(round(rho,5))

        elif valueCB2 == 1:
             vol = option_calculation_impliedVolatility(ut2,stop2,pri2,rfr2,ot2,lif2,strp2,valueRB2,valueCB2)
             tab1.vol.set(round(vol,5))

    ttk.Button(tab1,text = "CALCULATE",command=callback_option_calculation).grid(column = 0,row = 11,padx = 12,pady = 12)


    #Monte Carlo widgets - tab2--------------------------------------------------------------------------------------------------------------------------------------------------------
    tab2.label_titre.grid(columnspan = 5,row = 0,padx = 20,pady = 20)

    def callback_option_calculation_tab2():
        ut2_tab2 = tab2.ut_tab2.get()
        stop2_tab2 = tab2.stop_tab2.get()
        vol2_tab2 = tab2.vol_tab2.get() / 100
        rfr2_tab2 = tab2.rfr_tab2.get() / 100
        ot2_tab2 = tab2.ot_tab2.get()
        mt2_tab2 = tab2.mt_tab2.get()
        lif2_tab2 = tab2.lif_tab2.get()
        strp2_tab2 = tab2.strp_tab2.get()
        valueRB2_tab2 = tab2.valueRB_tab2.get()
        divy2_tab2 = tab2.divy_tab2.get() / 100
        nts2_tab2 = tab2.nts_tab2.get()
        nos2_tab2 = tab2.nos_tab2.get()
        rans2_tab2 = tab2.rans_tab2.get()

        #optional values
        ov1_tab2 = tab2.optionalEntry1_tab2.get()
        ov2_tab2 = tab2.optionalEntry2_tab2.get() / 100
        ov3_tab2 = tab2.optionalEntry3_tab2.get() / 100
     
        price, standardDeviation, tableauSpots = option_calculation_tab2(ut2_tab2,stop2_tab2,vol2_tab2,rfr2_tab2,ot2_tab2,mt2_tab2,lif2_tab2,strp2_tab2,valueRB2_tab2,divy2_tab2,nts2_tab2,nos2_tab2,rans2_tab2,ov1_tab2,ov2_tab2,ov3_tab2)
        tab2.valuePrice_tab2.set(round(price,5))
        tab2.valueSD_tab2.set(round(standardDeviation,5))
        
        #à corriger j'ai dix charts ou lieu d'un de dix !!!!!!!!!!!!!!!!!!!!!!!!!
        for i in range(min(nts2_tab2,10)):
            plt.plot(tableauSpots[i]) 
            plt.title('First Ten Simulation Trials')
            plt.xlabel('Time')
            plt.ylabel('Stock Price')
            plt.show()

    ttk.Button(tab2,text = "CALCULATE", command=callback_option_calculation_tab2).grid(column = 0,row = 13,padx = 1,pady = 11)


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
