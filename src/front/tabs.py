""" Tabs objects. """

from tkinter import StringVar
from tkinter import ttk

from src.front.widgets import (Label, Entry, Radiobutton, Checkbutton)


class _BaseTab(ttk.Frame):
    def __init__(self, notebook, name, title):
        super(_BaseTab, self).__init__(notebook)
        notebook.add(self, text=name)

        self.label_titre = ttk.Label(self, text=title, font='Helvetica 18 bold')


class OptionsCalculatorTab(_BaseTab):
    def __init__(self, notebook):
        _BaseTab.__init__(
            self,
            notebook,
            name="Options calculator",
            title="Options Pricer and Greeks Calculator",
        )

        self.static_settings()
        self.set_input()
        self.set_optional_settings()
        self.set_combobox()
        self.set_output()

    def static_settings(self):
        ttk.Label(self, text="Underlying Type: ",font='Helvetica 10 bold').grid(column = 0,row = 1,padx = 12,pady = 12)
        ttk.Label(self, text="Stock Price: ").grid(column = 0,row = 2,padx = 1,pady = 1)
        ttk.Label(self, text="Volatility (% per year): ").grid(column = 0,row = 3,padx = 1,pady = 1)
        ttk.Label(self, text="Risk-Free Rate (% per year): ").grid(column = 0,row = 4,padx = 1,pady = 1)
        
        ttk.Label(self,text ="Option Type: ",font='Helvetica 10 bold').grid(column = 0,row = 6,padx = 12,pady = 12)  
        ttk.Label(self,text ="Life (Years): ").grid(column = 0,row = 7,padx = 1,pady = 1)  
        ttk.Label(self,text ="Strike Price: ").grid(column = 0,row = 8,padx = 1,pady = 1)  

        ttk.Label(self, text="Results ",font='Helvetica 10 bold').grid(column = 0,row = 12,padx = 1,pady = 1)  
        ttk.Label(self, text="Price: ").grid(column = 0,row = 13,padx = 1,pady = 1)  
        ttk.Label(self, text="Delta (per €): ").grid(column = 0,row = 14,padx = 1,pady = 1)  
        ttk.Label(self, text="Gamma (per € per €): ").grid(column = 0,row = 15,padx = 1,pady = 1)  
        ttk.Label(self, text="Vega (per %): ").grid(column = 0,row = 16,padx = 1,pady = 1)  
        ttk.Label(self, text="Theta (per day): ").grid(column = 0,row = 17,padx = 1,pady = 1)  
        ttk.Label(self, text="Rho (per %): ").grid(column = 0,row = 18,padx = 1,pady = 1)

    def set_input(self):
        self.lif = Entry(self).grid(column = 1,row = 7,padx = 1,pady = 1)
        self.strp = Entry(self).grid(column = 1,row = 8,padx = 1,pady = 1)

        self.stop = Entry(self).grid(column = 1,row = 2,padx = 1,pady = 1)  
        self.vol = Entry(self).grid(column = 1,row = 3,padx = 1,pady = 1)
        self.rfr = Entry(self).grid(column = 1,row = 4,padx = 1,pady = 1) 
        
        self.valueRB = Radiobutton(self, call=0, put=1)
        self.valueRB.store['call'].grid(column = 2,row = 2,padx = 1,pady = 1)
        self.valueRB.store['put'].grid(column = 2,row = 4,padx = 1,pady = 1)

        self.valueCB = Checkbutton(self, text="Imply Volatility").grid(column = 2,row = 7,padx = 1,pady = 1)

    def set_output(self):
        self.valuePrice = Entry(self).grid(column = 1,row = 13,padx = 1,pady = 1)
        self.valueDelta = Entry(self).grid(column = 1,row = 14,padx = 1,pady = 1)
        self.valueGamma = Entry(self).grid(column = 1,row = 15,padx = 1,pady = 1) 
        self.valueVega = Entry(self).grid(column = 1,row = 16,padx = 1,pady = 1) 
        self.valueTheta = Entry(self).grid(column = 1,row = 17,padx = 1,pady = 1) 
        self.valueRho = Entry(self).grid(column = 1,row = 18,padx = 1,pady = 1) 

    def set_optional_settings(self):
        self.optionalLabel1 = Label(self)
        self.optionalLabel2 = Label(self)
        self.optionalLabel3 = Label(self)
        self.optionalEntry1 = Entry(self)
        self.optionalEntry2 = Entry(self)
        self.optionalEntry3 = Entry(self)
        

    def set_combobox(self):
        self.ut = StringVar()
        ut1 = ttk.Combobox(
            self,
            values=["Equity", "Currency", "Index", "Futures"],
            textvariable=self.ut,
        )
        ut1.current(0)
        ut1.grid(column = 1,row = 1,padx = 12,pady = 12) 
        ut1.bind("<<ComboboxSelected>>", self.get_interface_amend())
        
        self.ot = StringVar()
        ot1 = ttk.Combobox(
            self,
            values=["Black Scholes European", "Binomial European", 
                    "Binomial American", "Asian", "Barrier Up And In",
                    "Barrier Up And Out", "Barrier Down And In",
                    "Barrier Down And Out", "Binary Cash Or Nothing", 
                    "Binary Asset Or Nothing"],
            textvariable=self.ot
        )
        ot1.current(0)
        ot1.grid(column = 1,row = 6,padx = 12,pady = 12)
        ot1.bind("<<ComboboxSelected>>", self.get_interface_amend())



    def get_interface_amend(self):

        def interface_amend(event):
            ut2 = self.ut.get()
            ot2 = self.ot.get()

            if (ut2 == "Equity" and ot2 == "Black Scholes European") or (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing") or (ut2 == "Futures" and ot2 == "Black Scholes European"):
                self.optionalLabel1.grid_forget()
                self.optionalEntry1.grid_forget()
                self.optionalLabel2.grid_forget()
                self.optionalEntry2.grid_forget()
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()
            elif (ut2 == "Equity" and (ot2 == "Binomial European" or ot2 == "Binomial American")):
                self.optionalLabel1.grid_forget()
                self.optionalEntry1.grid_forget()
                self.optionalLabel2.grid(column = 0,row = 9,padx = 1,pady = 1)
                self.optionalLabel2.set("Tree Steps:")
                self.optionalEntry2.grid(column = 1,row = 9,padx = 1,pady = 1)
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()
            elif (ut2 == "Equity" and ot2 == "Asian"):
                self.optionalLabel1.grid_forget()
                self.optionalEntry1.grid_forget()
                self.optionalLabel2.grid(column = 0,row = 9,padx = 1,pady = 1)
                self.optionalLabel2.set("Time since Inception:")
                self.optionalEntry2.grid(column = 1,row = 9,padx = 1,pady = 1)
                self.optionalLabel3.grid(column = 0,row = 10,padx = 1,pady = 1)
                self.optionalLabel3.set("Current Average:")
                self.optionalEntry3.grid(column = 1,row = 10,padx = 1,pady = 1)
            elif (ut2 == "Equity" and (ot2 == "Barrier Up And In" or ot2 == "Barrier Up And Out" or ot2 == "Barrier Down And In" or ot2 == "Barrier Down And Out")):
                self.optionalLabel1.grid_forget()
                self.optionalEntry1.grid_forget()
                self.optionalLabel2.grid(column = 0,row = 9,padx = 1,pady = 1)
                self.optionalLabel2.set("Barrier:")
                self.optionalEntry2.grid(column = 1,row = 9,padx = 1,pady = 1)
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()
            elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing"):
                self.optionalLabel1.grid_forget()
                self.optionalEntry1.grid_forget()
                self.optionalLabel2.grid(column = 0,row = 9,padx = 1,pady = 1)
                self.optionalLabel2.set("Cash Amount:")
                self.optionalEntry2.grid(column = 1,row = 9,padx = 1,pady = 1)
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()
            elif (ut2 == "Currency" and ot2 == "Black Scholes European"):
                self.optionalLabel1.grid(column = 0,row = 5,padx = 1,pady = 1)
                self.optionalLabel1.set("Foreign RFR (% per year):")
                self.optionalEntry1.grid(column = 1,row = 5,padx = 1,pady = 1)
                self.optionalLabel2.grid_forget()
                self.optionalEntry2.grid_forget()
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()
            elif (ut2 == "Index" and ot2 == "Black Scholes European"):
                self.optionalLabel1.grid(column = 0,row = 5,padx = 1,pady = 1)
                self.optionalLabel1.set("Dividend Yield (% per year):")
                self.optionalEntry1.grid(column = 1,row = 5,padx = 1,pady = 1)
                self.optionalLabel2.grid_forget()
                self.optionalEntry2.grid_forget()
                self.optionalLabel3.grid_forget()
                self.optionalEntry3.grid_forget()

        return interface_amend
    

class MonteCarloTab(_BaseTab):
    def __init__(self, notebook):
        _BaseTab.__init__(
            self,
            notebook,
            name="Monte Carlo",
            title="Pricing Options by Monte Carlo Simulation",
        )

        self.static_settings()
        self.set_input()
        self.set_optional_settings()
        self.set_combobox()
        self.set_output()
    
    def static_settings(self):
        ttk.Label(self, text="Underlying Type: ",font='Helvetica 10 bold').grid(column = 0,row = 1,padx = 12,pady = 12)  
        ttk.Label(self, text="Stock Price: ").grid(column = 0,row = 2,padx = 1,pady = 1)  
        ttk.Label(self, text="Risk-Free Rate (% per year): ").grid(column = 0,row = 3,padx = 1,pady = 1)
        ttk.Label(self, text="Dividend Yield (% per year): ").grid(column = 0,row = 4,padx = 1,pady = 1)
        ttk.Label(self, text="Simulation Data: ",font='Helvetica 10 bold').grid(column = 0,row = 6,padx = 12,pady = 12)  
        ttk.Label(self, text="Number of Time Steps: ").grid(column = 0,row = 7,padx = 1,pady = 1)  
        ttk.Label(self, text="Number of Simulations: ").grid(column = 0,row = 8,padx = 1,pady = 1)
        ttk.Label(self, text="Random Seed: ").grid(column = 0,row = 9,padx = 1,pady = 1)
        ttk.Label(self, text="Option Type: ",font='Helvetica 10 bold').grid(column = 2,row = 1,padx = 12,pady = 12)  
        ttk.Label(self, text="Life (years): ").grid(column = 2,row = 2,padx = 1,pady = 1)  
        ttk.Label(self, text="Strike Price: ").grid(column = 2,row = 3,padx = 1,pady = 1)
        ttk.Label(self, text="Model Type: ").grid(column = 2,row = 6,padx = 1,pady = 1)
        ttk.Label(self, text="Volatility (% per year): ").grid(column = 2,row = 7,padx = 1,pady = 1)
        ttk.Label(self, text="Price: ").grid(column = 2,row = 13,padx = 1,pady = 1)  
        ttk.Label(self, text="Standard Error: ").grid(column = 2,row = 14,padx = 1,pady = 1)

    def set_input(self):
        self.stop_tab2 = Entry(self).grid(column = 1,row = 2,padx = 1,pady = 1)
        self.rfr_tab2 = Entry(self).grid(column = 1,row = 3,padx = 1,pady = 1)
        self.divy_tab2 = Entry(self).grid(column = 1,row = 4,padx = 1,pady = 1)
        self.nts_tab2 = Entry(self).grid(column = 1,row = 7,padx = 1,pady = 1)
        self.nos_tab2 = Entry(self).grid(column = 1,row = 8,padx = 1,pady = 1)
        self.rans_tab2 = Entry(self).grid(column = 1,row = 9,padx = 1,pady = 1)
        self.lif_tab2 = Entry(self).grid(column = 3,row = 2,padx = 1,pady = 1)
        self.strp_tab2 = Entry(self).grid(column = 3,row = 3,padx = 1,pady = 1)  
        self.vol_tab2 = Entry(self).grid(column = 3,row = 7,padx = 1,pady = 1)

        self.valueRB_tab2 = Radiobutton(self, call=0, put=1)
        self.valueRB_tab2.store['call'].grid(column = 4,row = 2,padx = 1,pady = 1)
        self.valueRB_tab2.store['put'].grid(column = 4,row = 3,padx = 1,pady = 1)

    def set_output(self):
        self.valuePrice_tab2 = Entry(self).grid(column = 3,row = 13,padx = 1,pady = 1)  
        self.valueSD_tab2 = Entry(self).grid(column = 3,row = 14,padx = 1,pady = 1)  

    def set_optional_settings(self):
        self.optionalLabel1_tab2 = Label(self)
        self.optionalLabel2_tab2 = Label(self)
        self.optionalLabel3_tab2 = Label(self)
        self.optionalEntry1_tab2 = Entry(self)
        self.optionalEntry2_tab2 = Entry(self)
        self.optionalEntry3_tab2 = Entry(self)

    def set_combobox(self):
        self.ut_tab2 = StringVar()
        ut1_tab2 = ttk.Combobox(
            self,
            values=["Equity"],
            textvariable=self.ut_tab2,
        )
        ut1_tab2.current(0)
        ut1_tab2.grid(column = 1,row = 1,padx = 12,pady = 12) 
        ut1_tab2.bind("<<ComboboxSelected>>", self.get_interface_amend_tab2())
        
        self.ot_tab2 = StringVar()
        ot1_tab2 = ttk.Combobox(
            self,
            values=["European"],
            textvariable=self.ot_tab2
        )
        ot1_tab2.current(0)
        ot1_tab2.grid(column = 3,row = 1,padx = 12,pady = 12)
        ot1_tab2.bind("<<ComboboxSelected>>", self.get_interface_amend_tab2())

        self.mt_tab2 = StringVar()
        mt1_tab2 = ttk.Combobox(
            self,
            values=["Log Normal", "Merton Jump Diffusion"],
            textvariable=self.mt_tab2,
        )
        mt1_tab2.current(0)
        mt1_tab2.grid(column = 3,row = 6,padx = 12,pady = 12)
        mt1_tab2.bind("<<ComboboxSelected>>", self.get_interface_amend_tab2())

    def get_interface_amend_tab2(self):

        def interface_amend_tab2(event):
            ut2_tab2 = self.ut_tab2.get()
            ot2_tab2 = self.ot_tab2.get()
            mt2_tab2 = self.mt_tab2.get()
            
            if (ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal"):
                self.optionalLabel1_tab2.grid_forget()
                self.optionalEntry1_tab2.grid_forget()
                self.optionalLabel2_tab2.grid_forget()
                self.optionalEntry2_tab2.grid_forget()
                self.optionalLabel3_tab2.grid_forget()
                self.optionalEntry3_tab2.grid_forget()
            elif (ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion"):
                self.optionalLabel1_tab2.grid(column = 2,row = 8,padx = 1,pady = 1)
                self.optionalLabel1_tab2.set("Jumps per Year : ")
                self.optionalEntry1_tab2.grid(column = 3,row = 8,padx = 1,pady = 1)
                self.optionalLabel2_tab2.grid(column = 2,row = 9,padx = 1,pady = 1)
                self.optionalLabel2_tab2.set("Average Jump Size (%): ")
                self.optionalEntry2_tab2.grid(column = 3,row = 9,padx = 1,pady = 1)
                self.optionalLabel3_tab2.grid(column = 2,row = 10,padx = 1,pady = 1)
                self.optionalLabel3_tab2.set("Jump Std Deviation (%): ")
                self.optionalEntry3_tab2.grid(column = 3,row = 10,padx = 1,pady = 1)

        return interface_amend_tab2
        



