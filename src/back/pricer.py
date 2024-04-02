#Tab1
from src.back.equityOptionFunctions import *
from src.back.currencyOptionFunctions import *
from src.back.indexOptionFunctions import *
from src.back.futuresOptionFunctions import *

#Tab2
from src.back.monteCarloFunctions import *
import matplotlib.pyplot as plt
from tkinter import messagebox

#Tab3


#Tab4
from scipy import interpolate


"""
from imaplib import Time2Internaldate
from math import *
from pickle import STOP
from numpy.random import normal
from scipy import stats
import pandas as pd
import numpy as np
import random
import statistics
import matplotlib.pyplot as plt
from tkinter import messagebox
#from datetime import datetime, timedelta
from scipy import interpolate

print(__file__)
from pathlib import Path
print(Path("."))
"""


#####################################Tab 1#####################################

#Cette fonction lance la fonction selon le modèle et le sj sélectionnés par l'utilisateur en Tab1:
def option_calculation(ut2, stop2, vol2, rfr2, ot2, lif2, strp2, valueRB2,valueCB2, ov1=0, ov2=0, ov3=0, pri2=0):
        
        #equity
        if (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 0): 
            price, delta, gamma, vega, theta, rho = call_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)
            
        elif (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 0):
            price, delta, gamma, vega, theta, rho = put_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)
            
        elif (ut2 == "Equity" and ot2 == "Binomial European" and valueRB2 == 0 and valueCB2 == 0):
            ov2 = int(ov2)
            price = call_price_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, ov2)
            delta, gamma, vega, theta, rho = call_greeks_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, ov2)

        elif (ut2 == "Equity" and ot2 == "Binomial European" and valueRB2 == 1 and valueCB2 == 0):
            ov2 = int(ov2)
            price = put_price_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, ov2)
            delta, gamma, vega, theta, rho = put_greeks_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, ov2)

        elif (ut2 == "Equity" and ot2 == "Binomial American" and valueRB2 == 0 and valueCB2 == 0):
            ov2 = int(ov2)
            price = call_price_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, ov2)
            delta, gamma, vega, theta, rho = call_greeks_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, ov2)
      
        elif (ut2 == "Equity" and ot2 == "Binomial American" and valueRB2 == 1 and valueCB2 == 0):
            ov2 = int(ov2)
            price = put_price_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, ov2)
            delta, gamma, vega, theta, rho = put_greeks_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, ov2)

        elif (ut2 == "Equity" and ot2 == "Asian" and valueRB2 == 0 and valueCB2 == 0):
            tsi2 = float(ov2)
            ca2 = float(ov3)
            price, delta, gamma, vega, theta, rho = call_price_greeks_asian(stop2, vol2, rfr2, lif2, strp2, tsi2, ca2)
            
        elif (ut2 == "Equity" and ot2 == "Asian" and valueRB2 == 1 and valueCB2 == 0):
            tsi2 = float(ov2)
            ca2 = float(ov3)
            price, delta, gamma, vega, theta, rho = put_price_greeks_asian(stop2, vol2, rfr2, lif2, strp2, tsi2, ca2)
        
       # elif (ut2 == "Equity" and ot2 == "Barrier Up And In" and valueRB2 == 0 and valueCB2 == 0):
       #     bar2 = int(ov2)
       #     price, delta, gamma, vega, theta, rho = call_price_greeks_barrier_up_and_in(stop2, vol2, rfr2, lif2, strp2, 2000, bar2)

       # elif (ut2 == "Equity" and ot2 == "Barrier Up And In" and valueRB2 == 1 and valueCB2 == 0):
       #     bar2 = int(ov2)
       #     price, delta, gamma, vega, theta, rho = put_price_greeks_barrier_up_and_in(stop2, vol2, rfr2, lif2, strp2, 2000, bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Up And Out" and valueRB2 == 0 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = call_price_greeks_barrier_up_and_out(stop2, vol2, rfr2, lif2, strp2, 2000,bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Up And Out" and valueRB2 == 1 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = put_price_greeks_barrier_up_and_out(stop2, vol2, rfr2, lif2, strp2, 2000, bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Down And In" and valueRB2 == 0 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = call_price_greeks_barrier_down_and_in(stop2, vol2, rfr2, lif2, strp2, bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Down And In" and valueRB2 == 1 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = put_price_greeks_barrier_down_and_in(stop2, vol2, rfr2, lif2, strp2, bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Down And Out" and valueRB2 == 0 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = call_price_greeks_barrier_down_and_out(stop2, vol2, rfr2, lif2, strp2, 2000, bar2)

        elif (ut2 == "Equity" and ot2 == "Barrier Down And Out" and valueRB2 == 1 and valueCB2 == 0):
            bar2 = int(ov2)
            price, delta, gamma, vega, theta, rho = put_price_greeks_barrier_down_and_out(stop2, vol2, rfr2, lif2, strp2, 2000, bar2)
  
        elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing" and valueRB2 == 0 and valueCB2 == 0):
            cash = int(ov2)
            price, delta, gamma, vega, theta, rho =  call_Binary_Cash_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2, cash)

        elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing" and valueRB2 == 1 and valueCB2 == 0):
            cash = int(ov2)
            price, delta, gamma, vega, theta, rho =  put_Binary_Cash_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2, cash)

        elif (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing" and valueRB2 == 0 and valueCB2 == 0):
            price, delta, gamma, vega, theta, rho = call_Binary_Asset_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2)
            
        elif (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing" and valueRB2 == 1 and valueCB2 == 0):
            price, delta, gamma, vega, theta, rho = put_Binary_Asset_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2)
        

        #currency 
        elif (ut2 == "Currency" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 0):
            frfr2 = float(ov1) / 100
            price, delta, gamma, vega, theta, rho = call_currency_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2, frfr2)  

        elif (ut2 == "Currency" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 0):
            frfr2 = float(ov1) / 100
            price, delta, gamma, vega, theta, rho = put_currency_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2, frfr2)


        #index 
        elif (ut2 == "Index" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 0):
            divy2 = float(ov1) / 100
            price, delta, gamma, vega, theta, rho = call_index_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2, divy2)  

        elif (ut2 == "Index" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 0):
            divy2 = float(ov1) / 100
            price, delta, gamma, vega, theta, rho = put_index_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2, divy2)


        #futures
        elif (ut2 == "Futures" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 0):
            price, delta, gamma, vega, theta, rho = call_futures_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)  

        elif (ut2 == "Futures" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 0):
            price, delta, gamma, vega, theta, rho = put_futures_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)


        return price, delta, gamma, vega, theta, rho


#Cette fonction lance la fonction qui calcule la volatilité implicite en Tab1:     
def option_calculation_impliedVolatility(ut2, stop2, prio2, rfr2, ot2, lif2, strp2, valueRB2,valueCB2):
        
        if (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 1): #implied vol pour un call
            stav = 0.2 #on assume une volatilité égale à 20% sur le marché action  
            impliedVolatility = round(call_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav) * 100, 5)
        
        elif (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 1): #implied vol pour un put
            stav = 0.2 #on assume une volatilité égale à 20% sur le marché action  
            impliedVolatility = round(put_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav) * 100, 5)

        return impliedVolatility


#####################################Tab 2#####################################

#Cette fonction lance la fonction qui calcule le prix de l'option via Monte Carlo:
def option_calculation_tab2(ut2_tab2, stop2_tab2, vol2_tab2, rfr2_tab2, ot2_tab2, mt2_tab2, lif2_tab2, strp2_tab2, valueRB2_tab2, divy2_tab2, nts2_tab2, nos2_tab2, rans2_tab2, ov1_tab2=0,ov2_tab2=0,ov3_tab2=0):
        
        if nts2_tab2 < 2 or  nts2_tab2 > 200 :
            messagebox.showinfo("Alert", "Number of time steps must be between 2 and 200")
            return
        elif nos2_tab2 < 4 or  nos2_tab2 > 10000 :
             messagebox.showinfo("Alert", "Number of simulations must be between 4 and 10000")
             return
        
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal" and valueRB2_tab2 == 0: #Lancement de la simulation Monte-Carlo (modèle : Log-Normal) pour un Call
            price, standardError, tableauSpots = monteCarloEuropeanLogNormalCall(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, divy2_tab2, int(nts2_tab2), int(nos2_tab2), rans2_tab2)
        
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal" and valueRB2_tab2 == 1: #Lancement de la simulation Monte-Carlo (modèle : Log-Normal) pour un Put
            price, standardError, tableauSpots = monteCarloEuropeanLogNormalPut(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, divy2_tab2, int(nts2_tab2), int(nos2_tab2), rans2_tab2)
        
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion" and valueRB2_tab2 == 0: #Lancement de la simulation Monte-Carlo (modèle : Merton Jump Diffusion) pour un Call
            jpy = int(ov1_tab2)
            ajs = float(ov2_tab2)
            jsd = float(ov3_tab2)
            price, standardError, tableauSpots = monteCarloEuropeanMertonJumpDiffusionCall(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, divy2_tab2, int(nts2_tab2), int(nos2_tab2), rans2_tab2,jpy, ajs, jsd)
        
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion" and valueRB2_tab2 == 1: #Lancement de la simulation Monte-Carlo (modèle : Merton Jump Diffusion) pour un Put
            jpy = int(ov1_tab2)
            ajs = float(ov2_tab2)
            jsd = float(ov3_tab2) 
            price, standardError, tableauSpots = monteCarloEuropeanMertonJumpDiffusionPut(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, divy2_tab2, int(nts2_tab2), int(nos2_tab2), rans2_tab2,jpy, ajs, jsd)

        return price, standardError, tableauSpots


"""

def option_calculation_tab2():
        ut2_tab2 = ut_tab2.get()
        stop2_tab2 = stop_tab2.get()
        vol2_tab2 = vol_tab2.get() / 100
        rfr2_tab2 = rfr_tab2.get() / 100
        ot2_tab2 = ot_tab2.get()
        mt2_tab2 = mt_tab2.get()
        lif2_tab2 = lif_tab2.get()
        strp2_tab2 = strp_tab2.get()
        valueRB2_tab2 = valueRB_tab2.get()
        div2_tab2 = div_tab2.get() / 100
        nts2_tab2 =nts_tab2.get()
        nos2_tab2 = nos_tab2.get()
        rans2_tab2 = rans_tab2.get()

        if nts2_tab2 < 2 or  nts2_tab2 > 200 :
            messagebox.showinfo("Alert", "Number of time steps must be between 2 and 200")
            return
        elif nos2_tab2 < 4 or  nos2_tab2 > 10000 :
             messagebox.showinfo("Alert", "Number of simulations must be between 4 and 10000")
             return
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal" and valueRB2_tab2 == 0: #Lancement de la simulation Monte-Carlo (modèle : Log-Normal) pour un Call
            res = monteCarloEuropeanLogNormalCall(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, div2_tab2, nts2_tab2, nos2_tab2, rans2_tab2)
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Log Normal" and valueRB2_tab2 == 1: #Lancement de la simulation Monte-Carlo (modèle : Log-Normal) pour un Put
            res = monteCarloEuropeanLogNormalPut(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, div2_tab2, nts2_tab2, nos2_tab2, rans2_tab2)
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion" and valueRB2_tab2 == 0: #Lancement de la simulation Monte-Carlo (modèle : Merton Jump Diffusion) pour un Call
            optionalEntry12_tab2 = optionalEntry1_tab2.get()
            optionalEntry22_tab2 = optionalEntry2_tab2.get() / 100
            optionalEntry32_tab2 = optionalEntry3_tab2.get() / 100
            res = monteCarloEuropeanMertonJumpDiffusionCall(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, div2_tab2, nts2_tab2, nos2_tab2, rans2_tab2,optionalEntry12_tab2, optionalEntry22_tab2, optionalEntry32_tab2)
        elif ut2_tab2 == "Equity" and ot2_tab2 == "European" and mt2_tab2 == "Merton Jump Diffusion" and valueRB2_tab2 == 1: #Lancement de la simulation Monte-Carlo (modèle : Merton Jump Diffusion) pour un Put
            optionalEntry12_tab2 = optionalEntry1_tab2.get()
            optionalEntry22_tab2 = optionalEntry2_tab2.get() / 100
            optionalEntry32_tab2 = optionalEntry3_tab2.get() / 100
            res = monteCarloEuropeanMertonJumpDiffusionPut(stop2_tab2, vol2_tab2 , rfr2_tab2, lif2_tab2, strp2_tab2, div2_tab2, nts2_tab2, nos2_tab2, rans2_tab2,optionalEntry12_tab2, optionalEntry22_tab2, optionalEntry32_tab2)


        #le plot sort avant les résultats..........................?????????????????????????????????????????????????
        pri_tab2.set(round(res[0],5))
        stae_tab2.set(round(res[1],5))
    
        for i in range(min(nts2_tab2,10)):
            plt.plot(tableauSpots[i]) 
        plt.title('First Ten Simulation Trials')
        plt.xlabel('Time')
        plt.ylabel('Stock Price')
        plt.show()
"""



#####################################Tab 3#####################################



#####################################Tab 4#####################################

def refreshCurve():
# Cette fonction renvoie les taux euros et les met à jour dans la tab5
#
# INPUTS
#----------------------------------------------------------------
# no input

#----------------------------------------------------------------
# OUTPUT
#----------------------------------------------------------------
# Les taux euros ester, eurib1, eurib3, eurib6, eurib12 de 1d à 50y
#----------------------------------------------------------------
    global dataRatesCurve
    data = pd.read_excel('C:/Users/paul/OneDrive/Bureau/python/Pricer Python/ratesCurve.xlsx')
    ttk.Label(tab5,text = data.iloc[:,0:6]).grid(column = 0,row = 2,padx = 1,pady = 1) #update tab5
    dataRatesCurve = data.to_numpy()
    ester = dataRatesCurve[:,1]
    eurib1 = dataRatesCurve[:,2]
    eurib3 = dataRatesCurve[:,3]
    eurib6 = dataRatesCurve[:,4]
    eurib12 = dataRatesCurve[:,5]
    time = np.array(list(range(1, 21)))
    timeNew = np.linspace(1, 20, 18250)
    
    interpoEster = interpolate.interp1d(time, ester)
    resultInterpoEster = interpoEster(timeNew)
    
    interpoEurib1 = interpolate.interp1d(time, eurib1)
    resultInterpoEurib1 = interpoEurib1(timeNew)

    interpoEurib3 = interpolate.interp1d(time, eurib3)
    resultInterpoEurib3 = interpoEurib3(timeNew)

    interpoEurib6 = interpolate.interp1d(time, eurib6)
    resultInterpoEurib6 = interpoEurib6(timeNew)

    interpoEurib12 = interpolate.interp1d(time, eurib12)
    resultInterpoEurib12 = interpoEurib12(timeNew)

    dataRatesCurve = [resultInterpoEster, resultInterpoEurib1, resultInterpoEurib3, resultInterpoEurib6, resultInterpoEurib12]
     
    return dataRatesCurve


def swapComputation():
# Cette fonction calcule le prix et la DV01 du swap
#
# INPUTS
#----------------------------------------------------------------
# no input

#----------------------------------------------------------------
# OUTPUT
#----------------------------------------------------------------
# Le prix et la DV01 du swap
#----------------------------------------------------------------    


   startDate2 = startDate.get() #'3/12/24'
   endDate2 = endDate.get() #'3/12/24'

   #essayer de savoir combien on a de jours entre les deux dates !!!!!!!!!!!!!!!!!!!!!!!!!!!
   
   valueRB2_tab4 = valueRB_tab4.get() #vaut 0 actuellement

   print(startDate2)
   print(endDate2)
   

   return
