#Functions------------------------------------------------------------------------------------------------------------------------------------------

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

import pricer.front.app
from pricer.front.app import *


#Cette fonction lance la fonction qui calculera le prix de l'option et ses grecques selon le sous-jacent et le modèle:
def option_calculation():
    #tentative de mettre un msg d'alerte si pas bon type de valeur.......    
    #if (ut.get() == "" and stop.get()!= DoubleVar()):
        #   return "faux"
        ut2 = ut.get()
        stop2 = stop.get()
        vol2 = vol.get() / 100
        rfr2 = rfr.get() / 100
        ot2 = ot.get()
        lif2 = lif.get()
        strp2 = strp.get()
        valueRB2 = valueRB.get()
        valueCB2 = valueCB.get()
        #rajouter un contrôle des données/types rentrés par l'utilisateur
        #changer le if en switch -> beaucoup mieux !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 1): #implied vol pour un call
            stav = 0.2 #on assume une volatilité égale à 20% sur le marché action  
            prio2 = valuePrice.get()          
            #faire un msg d'alerte si le prix de l'option est trop faible >= 0 et -> voir le code VBA
            res_iv = round(call_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav) * 100, 5)
            vol.set(res_iv)
            return
        elif (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 1): #implied vol pour un put
            stav = 0.2 
            prio2 = valuePrice.get()
            res_iv = round(put_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav) * 100, 5)
            vol.set(res_iv)
            return
        elif (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 0 and valueCB2 == 0):
            res2 = call_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)
            
        elif (ut2 == "Equity" and ot2 == "Black Scholes European" and valueRB2 == 1 and valueCB2 == 0):
            res2 = put_price_greeks_BS_model(stop2,vol2,rfr2,lif2,strp2)
            
        elif (ut2 == "Equity" and ot2 == "Binomial European" and valueRB2 == 0 and valueCB2 == 0):
            niter2 = int(optionalEntry2.get())
            res2 = list([call_price_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, niter2)]) + call_greeks_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, niter2)
            
        elif (ut2 == "Equity" and ot2 == "Binomial European" and valueRB2 == 1 and valueCB2 == 0):
            niter2 = int(optionalEntry2.get())
            res2 = list([put_price_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, niter2)]) + put_greeks_binomial_european_model(stop2, vol2, rfr2, lif2, strp2, niter2)
            
        elif (ut2 == "Equity" and ot2 == "Binomial American" and valueRB2 == 0 and valueCB2 == 0):
            niter2 = int(optionalEntry2.get())
            res2 = list([call_price_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, niter2)]) + call_greeks_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, niter2)
            
        elif (ut2 == "Equity" and ot2 == "Binomial American" and valueRB2 == 1 and valueCB2 == 0):
            niter2 = int(optionalEntry2.get())
            res2 = list([put_price_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, niter2)]) + put_greeks_binomial_american_model(stop2, vol2, rfr2, lif2, strp2, niter2)  
            
        elif (ut2 == "Equity" and ot2 == "Asian" and valueRB2 == 0 and valueCB2 == 0):
            tsi2 = float(optionalEntry2.get())
            ca2 = float(optionalEntry3.get())
     
            res2 = call_price_greeks_asian(stop2, vol2, rfr2, lif2, strp2, tsi2, ca2)
            
        elif (ut2 == "Equity" and ot2 == "Asian" and valueRB2 == 1 and valueCB2 == 0):
            tsi2 = float(optionalEntry2.get())
            ca2 = float(optionalEntry3.get())
            res2 = put_price_greeks_asian(stop2, vol2, rfr2, lif2, strp2, tsi2, ca2)
            
        elif (ut2 == "Equity" and ot2 == "Barrier Up And Out" and valueRB2 == 0 and valueCB2 == 0):
            bar2 = int(optionalEntry2.get())
            res2 = call_price_greeks_barrier_up_and_out()
            
        elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing" and valueRB2 == 0 and valueCB2 == 0):
            cash = int(optionalEntry2.get())
            res2 = call_Binary_Cash_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2, cash)
            
        elif (ut2 == "Equity" and ot2 == "Binary Cash Or Nothing" and valueRB2 == 1 and valueCB2 == 0):
            cash = int(optionalEntry2.get())
            res2 = put_Binary_Cash_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2, cash)
            
        elif (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing" and valueRB2 == 0 and valueCB2 == 0):
            res2 = call_Binary_Asset_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2)
            
        elif (ut2 == "Equity" and ot2 == "Binary Asset Or Nothing" and valueRB2 == 1 and valueCB2 == 0):
            res2 = put_Binary_Asset_Or_Nothing_model(stop2, vol2, rfr2, lif2, strp2)
                

        valuePrice.set(round(res2[0],5))
        valueDelta.set(round(res2[1],5))
        valueGamma.set(round(res2[2],5))
        valueVega.set(round(res2[3],5))
        valueTheta.set(round(res2[4],5))
        valueRho.set(round(res2[5],5))


#Cette fonction lance la fonction qui calculera le prix de l'option via Monte Carlo:
def option_calculation_tab2():
        ut2_tab2 = ut_tab2 .get()
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



#Cette fonction calcule la volatilité implicite pour un call avec le modèle Black et Scholes----------------------------------------------------------------------------------------------
def call_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav):
    dVol = 0.0000001
    epsilon = 0.0000001
    maxIter = 1000
    vol_1 = stav
    i = 1
    while True:
        Value_1 = call_price_greeks_BS_model(stop2, vol_1, rfr2, lif2, strp2)[0]
        vol_2 = vol_1 - dVol
        Value_2 = call_price_greeks_BS_model(stop2, vol_2, rfr2, lif2, strp2)[0]
        dx = (Value_2 - Value_1) / dVol
        if abs(dx) < epsilon or i == maxIter: break
        vol_1 = vol_1 - (prio2 - Value_1) / dx
        i = i + 1   
    return vol_1
   
#Cette fonction calcule la volatilité implicite pour un put avec le modèle Black et Scholes (sj equity)----------------------------------------------------------------------------------------
def put_implied_volatility_BS(stop2, strp2, rfr2, lif2, prio2, stav):
    dVol = 0.0000001
    epsilon = 0.0000001
    maxIter = 1000
    vol_1 = stav
    i = 1
    while True:
        Value_1 = put_price_greeks_BS_model(stop2, strp2, vol_1, rfr2, lif2)
        vol_2 = vol_1 - dVol
        Value_2 = put_price_greeks_BS_model(stop2, strp2, vol_2, rfr2, lif2)
        dx = (Value_2 - Value_1) / dVol
        if abs(dx) < epsilon or i == maxIter: break
        vol_1 = vol_1 - (prio2 - Value_1) / dx
        i = i + 1    
    return vol_1


#Cette fonction calcule le prix pour une call européenne avec le modèle de Black et Scholes (sj equity)--------------------------------------------------------------------------
def call_price_BS_model(stop, vol, rfr, lif, strp):
    d1 = ((log(stop/strp)) + ((rfr + ((vol**2)/2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf11 = stats.norm.cdf(d1, loc = 0, scale = 1)
    cdf12 = stats.norm.cdf(d2, loc = 0, scale = 1)
    res = []
    res.append((stop * cdf11) - (strp * exp(-(rfr * lif)) * cdf12)) #prix
    return res

 #Cette fonction calcule le prix pour un put européenne avec le modèle de Black et Scholes (sj equity)---------------------------------------------------------------------------
def put_price_BS_model(stop, vol, rfr, lif, strp):
    d1 = ((log(stop/strp)) + ((rfr + ((vol**2)/2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf22 = stats.norm.cdf(-d2, loc = 0, scale = 1)
    cdf1 = stats.norm.cdf(-d1, loc = 0, scale = 1)
    res = []
    res.append(strp * exp(-(rfr * lif)) * cdf22 - (stop * cdf1)) #prix
    return res

#Cette fonction calcule le prix et les greeks pour une call européenne avec le modèle de Black et Scholes (sj equity)--------------------------------------------------------------------------
def call_price_greeks_BS_model(stop, vol, rfr, lif, strp):
    d1 = ((log(stop/strp)) + ((rfr + ((vol**2)/2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    phi1 = exp(-(d1**2 / 2)) / sqrt(2*pi)
    cdf11 = stats.norm.cdf(d1, loc = 0, scale = 1)
    cdf12 = stats.norm.cdf(d2, loc = 0, scale = 1)
    res = []
    res.append((stop * cdf11) - (strp * exp(-(rfr * lif)) * cdf12)) #prix
    res.append((cdf11)) #delta
    res.append(phi1 / (stop * vol * sqrt(lif))) #gamma
    res.append(stop * phi1 * sqrt(lif) / 100) #vega
    res.append((-((stop * phi1 * vol) / (2 * sqrt(lif))) - (rfr * strp * exp(-rfr * lif) * cdf12)) / 365) #theta
    res.append((strp * lif * exp(-rfr * lif) * cdf12) / 100) #rho
    return res

 #Cette fonction calcule le prix et les greeks pour un put européenne avec le modèle de Black et Scholes (sj equity)---------------------------------------------------------------------------
def put_price_greeks_BS_model(stop, vol, rfr, lif, strp):
    d1 = ((log(stop/strp)) + ((rfr + ((vol**2)/2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    phi1 = exp(-(d1**2 / 2)) / sqrt(2*pi)
    cdf11 = stats.norm.cdf(d1, loc = 0, scale = 1)
    cdf22 = stats.norm.cdf(-d2, loc = 0, scale = 1)
    cdf1 = stats.norm.cdf(-d1, loc = 0, scale = 1)
    res = []
    res.append(strp * exp(-(rfr * lif)) * cdf22 - (stop * cdf1)) #prix
    res.append(cdf11-1) #delta
    res.append(phi1 / (stop * vol * sqrt(lif))) #gamma
    res.append(stop * phi1 * sqrt(lif) / 100) #vega
    res.append((-((stop * phi1 * vol) / (2 * sqrt(lif))) + (rfr * strp * exp(-rfr * lif) * cdf22)) / 365) #theta #à revoir ca bloque.............
    res.append((-strp * lif * exp(-rfr * lif) * cdf22) / 100) #rho
    return res

#Cette fonction calcule le prix d'un call européenne avec le modèle Binomial (sj equity)-------------------------------------------------------------------------------------------------------
def call_price_binomial_european_model(stop, vol, rfr, lif, strp, niter):
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] < strp:
            res[i] = 0
        else:
            res[i] = res[i] - strp
    timeStep = lif/niter
    for i in range(1,(niter+1)):
        for j in range((niter+1)-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
    return(res[0])
    
#Cette fonction calcule le prix d'un put européenne avec le modèle Binomial (sj equity)--------------------------------------------------------------------------------------------------------
def put_price_binomial_european_model(stop, vol, rfr, lif, strp, niter):
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] > strp:
            res[i] = 0
        else:
            res[i] = strp - res[i]
    timeStep = lif/niter
    for i in range(1,(niter+1)):
        for j in range((niter+1)-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
    return(res[0])

#Cette fonction calcule les greeks d'un call européenne avec le modèle Binomial (sj equity)----------------------------------------------------------------------------------------------------
def call_greeks_binomial_european_model(stop, vol, rfr, lif, strp, niter):
    vol2 = vol + 0.01
    rfr2 = rfr + 0.01
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] < strp:
            res[i] = 0
        else:
            res[i] = res[i] - strp
    #Lorsque la volatilité varie de +1% (pour le calcul de vega)
    up2 = exp(vol2*sqrt(lif/niter))
    down2 = 1/up2
    prob2 = (exp(rfr*lif/niter)-down2)/(up2-down2) #probabilité d'un mouvement de hausse
    prob_2 = 1-prob2 #probabilité d'un mouvement de baisse
    res2 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res2'
        res2.append(stop*(down2**i)*(up2**(niter-i)))
        if res2[i] < strp:
            res2[i] = 0
        else:
            res2[i] = res2[i] - strp
    #Lorsque le taux sans risque varie de +1% (pour le calcul de rho):
    prob3 = (exp(rfr2*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_3 = 1-prob3 #probabilité d'un mouvement de baisse
    timeStep = lif/niter #le pas d'itération
    res3 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau3' lorsque le taux sans risque varie de 1%
        res3.append(res[i])
    
    for i in range(1,niter+1): #Boucle qui détermine le prix initial de l'option d'achat (backward-looking)
        for j in range(niter+1-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
            if i == niter - 1 and j == 0:
                fu = res[0]
            elif i == niter - 1 and j == 1: 
                fd = res[1]
            elif i == niter - 2 and j == 0:
                fuu = res[0]
            elif i == niter - 2 and j == 1:
                fud = res[1]
            elif i == niter - 2 and j == 2:
                fdd = res[2]
            res2[j]=exp((-rfr) * timeStep) * (prob2 * res2[j] + prob_2 * res2[j + 1])
            res3[j]=exp((-rfr2) * timeStep) * (prob3 * res3[j] + prob_3 * res3[j + 1])
    delta = (fu - fd) / ((stop*up)-(stop*down))
    gamma = (((fuu - fud) / (stop * up * up - stop * up * down)) - ((fud - fdd) / (stop * up * down - stop * down * down))) / ((stop * up * up - stop * down * down) / 2)
    vega = res2[0] - res[0]
    theta = (fud - res[0]) / (2 * lif * 365 / niter)
    rho = res3[0] - res[0]
    res_B_greeks = [delta, gamma, vega, theta, rho]
    return res_B_greeks

#Cette fonction calcule les greeks d'un put européenne avec le modèle Binomial (sj equity)-----------------------------------------------------------------------------------------------------
def put_greeks_binomial_european_model(stop, vol, rfr, lif, strp, niter):
    vol2 = vol + 0.01
    rfr2 = rfr + 0.01
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] > strp:
            res[i] = 0
        else:
            res[i] = strp - res[i]
    #Lorsque la volatilité varie de +1% (pour le calcul de vega)
    up2 = exp(vol2*sqrt(lif/niter))
    down2 = 1/up2
    prob2 = (exp(rfr*lif/niter)-down2)/(up2-down2) #probabilité d'un mouvement de hausse
    prob_2 = 1-prob2 #probabilité d'un mouvement de baisse
    res2 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res2'
        res2.append(stop*(down2**i)*(up2**(niter-i)))
        if res2[i] > strp:
            res2[i] = 0
        else:
            res2[i] = strp - res2[i]
    #Lorsque le taux sans risque varie de +1% (pour le calcul de rho):
    prob3 = (exp(rfr2*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_3 = 1-prob3 #probabilité d'un mouvement de baisse
    timeStep = lif/niter #le pas d'itération
    res3 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau3' lorsque le taux sans risque varie de 1%
        res3.append(res[i])
    
    for i in range(1,niter+1): #Boucle qui détermine le prix initial de l'option d'achat (backward-looking)
        for j in range(niter+1-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
            if i == niter - 1 and j == 0:
                fu = res[0]
            elif i == niter - 1 and j == 1: 
                fd = res[1]
            elif i == niter - 2 and j == 0:
                fuu = res[0]
            elif i == niter - 2 and j == 1:
                fud = res[1]
            elif i == niter - 2 and j == 2:
                fdd = res[2]
            res2[j]=exp((-rfr) * timeStep) * (prob2 * res2[j] + prob_2 * res2[j + 1])
            res3[j]=exp((-rfr2) * timeStep) * (prob3 * res3[j] + prob_3 * res3[j + 1])
    delta = (fu - fd) / ((stop*up)-(stop*down))
    gamma = (((fuu - fud) / (stop * up * up - stop * up * down)) - ((fud - fdd) / (stop * up * down - stop * down * down))) / ((stop * up * up - stop * down * down) / 2)
    vega = res2[0] - res[0]
    theta = (fud - res[0]) / (2 * lif * 365 / niter)
    rho = res3[0] - res[0]
    res_B_greeks = [delta, gamma, vega, theta, rho]
    return res_B_greeks

#Cette fonction calcule le prix d'un call american avec le modèle Binomial (sj equity)-------------------------------------------------------------------------------------------------------
def call_price_binomial_american_model(stop, vol, rfr, lif, strp, niter):
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] < strp:
            res[i] = 0
        else:
            res[i] = res[i] - strp
    timeStep = lif/niter
    for i in range(1,niter+1):
        for j in range(niter+1-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
            if res[j] < (stop * (up**(niter - i - j)) * (down**j)) - strp:
                 res[j] = (stop * (up**(niter - i - j)) * (down**j)) - strp
    return(res[0])

#Cette fonction calcule le prix d'un put american avec le modèle Binomial (sj equity)-------------------------------------------------------------------------------------------------------
def put_price_binomial_american_model(stop, vol, rfr, lif, strp, niter):
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] > strp:
            res[i] = 0
        else:
            res[i] = strp - res[i]
    timeStep = lif/niter
    for i in range(1,(niter+1)):
        for j in range((niter+1)-i):
            res[j] = exp((-rfr) * timeStep) * (prob * res[j] + prob_ * res[j+1])
            if res[j] < strp - (stop * (up**(niter - i - j)) * (down ** j)):
                 res[j] = strp - (stop * (up**(niter - i - j)) * (down ** j))
    return(res[0])

#Cette fonction calcule les greeks d'un call american avec le modèle Binomial (sj equity)----------------------------------------------------------------------------------------------------
def call_greeks_binomial_american_model(stop, vol, rfr, lif, strp, niter):
    vol2 = vol + 0.01
    rfr2 = rfr + 0.01
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] < strp:
            res[i] = 0
        else:
            res[i] = res[i] - strp
    #Lorsque la volatilité varie de +1% (pour le calcul de vega)
    up2 = exp(vol2*sqrt(lif/niter))
    down2 = 1/up2
    prob2 = (exp(rfr*lif/niter)-down2)/(up2-down2) #probabilité d'un mouvement de hausse
    prob_2 = 1-prob2 #probabilité d'un mouvement de baisse
    res2 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res2'
        res2.append(stop*(down2**i)*(up2**(niter-i)))
        if res2[i] < strp:
            res2[i] = 0
        else:
            res2[i] = res2[i] - strp
    #Lorsque le taux sans risque varie de +1% (pour le calcul de rho):
    prob3 = (exp(rfr2*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_3 = 1-prob3 #probabilité d'un mouvement de baisse
    timeStep = lif/niter #le pas d'itération
    res3 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau3' lorsque le taux sans risque varie de 1%
        res3.append(res[i])
    
    for i in range(1,niter+1): #Boucle qui détermine le prix initial de l'option d'achat (backward-looking)
        for j in range(niter+1-i):
            res[j] = exp((-rfr)*timeStep)*(prob*res[j]+prob_*res[j+1])
            if res[j] < (stop * (up ** (niter - i - j)) * (down ** j)) - strp:
                 res[j] = (stop * (up ** (niter - i - j)) * (down ** j)) - strp
            if i == niter - 1 and j == 0:
                fu = res[0]
            elif i == niter - 1 and j == 1: 
                fd = res[1]
            elif i == niter - 2 and j == 0:
                fuu = res[0]
            elif i == niter - 2 and j == 1:
                fud = res[1]
            elif i == niter - 2 and j == 2:
                fdd = res[2]
            res2[j]=exp((-rfr) * timeStep) * (prob2 * res2[j] + prob_2 * res2[j + 1])
            if res2[j] < (stop * (up ** (niter - i - j)) * (down ** j)) - strp:
                 res2[j] = (stop * (up ** (niter - i - j)) * (down ** j)) - strp
            res3[j]=exp((-rfr2) * timeStep) * (prob3 * res3[j] + prob_3 * res3[j + 1])
            if res3[j] < (stop * (up ** (niter - i - j)) * (down ** j)) - strp:
                 res3[j] = (stop * (up ** (niter - i - j)) * (down ** j)) - strp
    delta = (fu - fd) / ((stop*up)-(stop*down))
    gamma = (((fuu - fud) / (stop * up * up - stop * up * down)) - ((fud - fdd) / (stop * up * down - stop * down * down))) / ((stop * up * up - stop * down * down) / 2)
    vega = res2[0] - res[0]
    theta = (fud - res[0]) / (2 * lif * 365 / niter)
    rho = res3[0] - res[0]
    res_B_greeks = [delta, gamma, vega, theta, rho]
    return res_B_greeks

#Cette fonction calcule les greeks d'un put american avec le modèle Binomial (sj equity)-----------------------------------------------------------------------------------------------------
def put_greeks_binomial_american_model(stop, vol, rfr, lif, strp, niter):
    vol2 = vol + 0.01
    rfr2 = rfr + 0.01
    up = exp(vol*sqrt(lif/niter))
    down = 1/up
    prob = (exp(rfr*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_ = 1-prob #probabilité d'un mouvement de baisse
    res = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res'
        res.append(stop*(down**i)*(up**(niter-i)))
        if res[i] > strp:
            res[i] = 0
        else:
            res[i] = strp - res[i]
    #Lorsque la volatilité varie de +1% (pour le calcul de vega)
    up2 = exp(vol2*sqrt(lif/niter))
    down2 = 1/up2
    prob2 = (exp(rfr*lif/niter)-down2)/(up2-down2) #probabilité d'un mouvement de hausse
    prob_2 = 1-prob2 #probabilité d'un mouvement de baisse
    res2 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'res2'
        res2.append(stop*(down2**i)*(up2**(niter-i)))
        if res2[i] > strp:
            res2[i] = 0
        else:
            res2[i] = strp - res2[i]
    #Lorsque le taux sans risque varie de +1% (pour le calcul de rho):
    prob3 = (exp(rfr2*lif/niter)-down)/(up-down) #probabilité d'un mouvement de hausse
    prob_3 = 1-prob3 #probabilité d'un mouvement de baisse
    timeStep = lif/niter #le pas d'itération
    res3 = []
    for i in range(niter+1): #Boucle qui stocke les valeurs finales de l'arbre binomial dans 'tableau3' lorsque le taux sans risque varie de 1%
        res3.append(res[i])
    
    for i in range(1,niter+1): #Boucle qui détermine le prix initial de l'option d'achat (backward-looking)
        for j in range(niter+1-i):
            res[j] = exp((-rfr) * timeStep) * (prob * res[j] + prob_ * res[j+1])
            if res[j] < strp - (stop * (up**(niter - i - j)) * (down**j)):
                 res[j] = strp - (stop * (up**(niter - i - j)) * (down**j))
            if i == niter - 1 and j == 0:
                fu = res[0]
            elif i == niter - 1 and j == 1: 
                fd = res[1]
            elif i == niter - 2 and j == 0:
                fuu = res[0]
            elif i == niter - 2 and j == 1:
                fud = res[1]
            elif i == niter - 2 and j == 2:
                fdd = res[2]
            res2[j]=exp((-rfr) * timeStep) * (prob2 * res2[j] + prob_2 * res2[j + 1])
            if res2[j] < strp - (stop * (up**(niter - i - j)) * (down**j)):
                 res2[j] = strp - (stop * (up**(niter - i - j)) * (down**j))
            res3[j]=exp((-rfr2) * timeStep) * (prob3 * res3[j] + prob_3 * res3[j + 1])
            if res3[j] < strp - (stop * (up**(niter - i - j)) * (down**j)):
                 res3[j] = strp - (stop * (up**(niter - i - j)) * (down**j))
    delta = (fu - fd) / ((stop*up)-(stop*down))
    gamma = (((fuu - fud) / (stop * up * up - stop * up * down)) - ((fud - fdd) / (stop * up * down - stop * down * down))) / ((stop * up * up - stop * down * down) / 2)
    vega = res2[0] - res[0]
    theta = (fud - res[0]) / (2 * lif * 365 / niter)
    rho = res3[0] - res[0]
    res_B_greeks = [delta, gamma, vega, theta, rho]
    return res_B_greeks


####################################################################### Binary Cash or Nothing #############################################################################


def callPriceBinaryCashOrNothing(v1, v2, v3, v4, v5, v6) :
# Cette fonction calcule le prix d'une option d'achat Binary Cash Or Nothing
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : prix d'exercice
# v3 : volatilité
# v4 : taux d'intérêt sans risque
# v5 : maturité
# v6 : montant de cash
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option d'achat Binary Cash Or Nothing
#
#----------------------------------------------------------------

   d1 = ((log(v1 / v2)) + ((v4 + ((v3**2) / 2)) * v5)) / (v3 * sqrt(v5))
   d2 = d1 - (v3 * sqrt(v5))
   cdf = stats.norm.cdf(d2, 0, 1)
   callPriceBinaryCashOrNothing = exp(-(v4 * v5)) * cdf * v6
   
   return callPriceBinaryCashOrNothing


def putPriceBinaryCashOrNothing(v1, v2, v3, v4, v5, v6) :
# Cette fonction calcule le prix d'une option de vente Binary Cash Or Nothing
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : prix d'exercice
# v3 : volatilité
# v4 : taux d'intérêt sans risque
# v5 : maturité
# v6 : montant de cash
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option de vente Binary Cash Or Nothing
#
#----------------------------------------------------------------

   d1 = ((log(v1 / v2)) + ((v4 + ((v3**2) / 2)) * v5)) / (v3 * sqrt(v5))
   d2 = d1 - (v3 * sqrt(v5))
   cdf = stats.norm.cdf(d2, 0, 1)
   callPriceBinaryCashOrNothing = exp(-v4 * v5) * (1 - cdf) * v6

   return callPriceBinaryCashOrNothing


def call_Binary_Cash_Or_Nothing_model(spot, vol, rfr, life, strike, cash):

   d1 = ((log(spot / strike)) + ((rfr + ((vol**2) / 2)) * life)) / (vol * sqrt(life))
   d2 = d1 - (vol * sqrt(life))

   Pi = pi #nombre Pi
   phi1 = exp(-(d1**2 / 2)) / sqrt(2 * Pi)

   cdf2 = stats.norm.cdf(d2, 0, 1) #fonction de répartition de la loi normale

   res = []
   res.append(exp(-(rfr * life)) * cdf2 * cash) #price
   res.append(((spot / strike) * (phi1 / (spot * vol * sqrt(life)))) * cash) #delta
   res.append((-((phi1 / (spot * vol * sqrt(life))) / strike) * (d1 / (vol * sqrt(life)))) * cash) #gamma
   #Vega
   vol2 = vol + 0.01 #Lorsque la volatilité augmente de 1%
   d1Vol = ((log(spot / strike)) + ((rfr + ((vol2**2) / 2)) * life)) / (vol2 * sqrt(life))
   d2Vol = d1Vol - (vol2 * sqrt(life))
   cdf2Vol = stats.norm.cdf(d2Vol, 0, 1)
   res.append((exp(-(rfr * life)) * cdf2Vol * cash) - (exp(-(rfr * life)) * cdf2 * cash))
   #Theta
   life2 = life * 0.99726027 #Maturité - 1 jour
   d1life = ((log(spot / strike)) + ((rfr + ((vol**2) / 2)) * life2)) / (vol * sqrt(life2))
   d2life = d1life - (vol * sqrt(life2))
   cdf2life = stats.norm.cdf(d2life, 0, 1)
   res.append((exp(-(rfr * life2)) * cdf2life * cash) - (exp(-(rfr * life)) * cdf2 * cash))
   #Rho
   rfr2 = rfr + 0.01 #Lorsque le taux sans risque augmente de 1%
   d1RFR = ((log(spot / strike)) + ((rfr2 + ((vol**2) / 2)) * life)) / (vol * sqrt(life))
   d2RFR = d1RFR - (vol * sqrt(life))
   cdf2RFR = stats.norm.cdf(d2RFR, 0, 1)
   res.append((exp(-(rfr2 * life)) * cdf2RFR * cash) - (exp(-(rfr * life)) * cdf2 * cash))
   
   return res

def put_Binary_Cash_Or_Nothing_model(spot, vol, rfr, life, strike, cash):

   d1 = ((log(spot / strike)) + ((rfr + ((vol**2) / 2)) * life)) / (vol * sqrt(life))
   d2 = d1 - (vol * sqrt(life))

   Pi = pi #nombre Pi
   phi1 = exp(-(d1**2 / 2)) / sqrt(2 * Pi)

   cdf2 = stats.norm.cdf(d2, 0, 1) #fonction de répartition de la loi normale

   res = []
   res.append(exp(-(rfr * life)) * (1-cdf2) * cash) #price
   res.append((-(spot / strike)) * (phi1 / (spot * vol * sqrt(life))) * cash) #delta
   res.append((((phi1 / (spot * vol * sqrt(life))) / strike) * (d1 / (vol * sqrt(life)))) * cash) #gamma
   #Vega
   vol2 = vol + 0.01 #Lorsque la volatilité augmente de 1%
   d1Vol = ((log(spot / strike)) + ((rfr + ((vol2**2) / 2)) * life)) / (vol2 * sqrt(life))
   d2Vol = d1Vol - (vol2 * sqrt(life))
   cdf2Vol = stats.norm.cdf(d2Vol, 0, 1)
   res.append((exp(-(rfr * life)) * (1-cdf2Vol) * cash) - (exp(-(rfr * life)) * (1-cdf2) * cash))
   #Theta
   life2 = life * 0.99726027 #Maturité - 1 jour
   d1life = ((log(spot / strike)) + ((rfr + ((vol**2) / 2)) * life2)) / (vol * sqrt(life2))
   d2life = d1life - (vol * sqrt(life2))
   cdf2life = stats.norm.cdf(d2life, 0, 1)
   res.append((exp(-(rfr * life2)) * (1-cdf2life) * cash) - (exp(-(rfr * life)) * (1-cdf2) * cash))
   #Rho
   rfr2 = rfr + 0.01 #Lorsque le taux sans risque augmente de 1%
   d1RFR = ((log(spot / strike)) + ((rfr2 + ((vol**2) / 2)) * life)) / (vol * sqrt(life))
   d2RFR = d1RFR - (vol * sqrt(life))
   cdf2RFR = stats.norm.cdf(d2RFR, 0, 1)
   res.append((exp(-(rfr2 * life)) * (1-cdf2RFR) * cash) - (exp(-(rfr * life)) * (1-cdf2) * cash))
   
   return res


################################################################################ Binary Asset or Nothing ####################################################################################

def call_Binary_Asset_Or_Nothing_model(spot, vol, rfr, life, strike):
    spot2 = spot+1
    spot3 = spot+2
    vol2 = vol+0.01
    rfr2 = rfr+0.01
    life2=life*(364/365)
    price = sum(call_price_BS_model(spot, vol, rfr, life, strike) + list([callPriceBinaryCashOrNothing(spot, strike, vol, rfr, life, strike)])) #prix du call au spot
    price2 =sum(call_price_BS_model(spot2, vol, rfr, life, strike) + list([callPriceBinaryCashOrNothing(spot2, strike, vol, rfr, life, strike)]))#prix du call au spot + 1
    price3 = sum(call_price_BS_model(spot3, vol, rfr, life, strike) + list([callPriceBinaryCashOrNothing(spot3, strike, vol, rfr, life, strike)])) #prix du call au spot + 2 
    delta = price2 - price #delta du call au niveau du spot
    delta2 = price3 - price2 #delta du call au niveau du spot + 1
    res = []
    res.append(price) #prix
    res.append(delta) #delta
    res.append(delta2-delta) #gamma
    res.append(sum(-price + call_price_BS_model(spot, vol2, rfr, life, strike) + list([callPriceBinaryCashOrNothing(spot, strike, vol2, rfr, life, strike)]))) #vega
    res.append(sum(-price + call_price_BS_model(spot, vol, rfr, life2, strike) + list([callPriceBinaryCashOrNothing(spot, strike, vol, rfr, life2, strike)]))) #theta
    res.append(sum(-price + call_price_BS_model(spot, vol, rfr2, life, strike) + list([callPriceBinaryCashOrNothing(spot, strike, vol, rfr2, life, strike)]))) #rho
    return res


def put_Binary_Asset_Or_Nothing_model(spot, vol, rfr, life, strike):
    spot2 = spot+1
    spot3 = spot+2
    vol2 = vol+0.01
    rfr2 = rfr+0.01
    life2=life*(364/365)
    price = sum(put_price_BS_model(spot, vol, rfr, life, strike) + list([putPriceBinaryCashOrNothing(spot, strike, vol, rfr, life, strike)])) #prix du call au spot
    price2 =sum(put_price_BS_model(spot2, vol, rfr, life, strike) + list([putPriceBinaryCashOrNothing(spot2, strike, vol, rfr, life, strike)]))#prix du call au spot + 1
    price3 = sum(put_price_BS_model(spot3, vol, rfr, life, strike) + list([putPriceBinaryCashOrNothing(spot3, strike, vol, rfr, life, strike)])) #prix du call au spot + 2 
    delta = price2 - price #delta du call au niveau du spot
    delta2 = price3 - price2 #delta du call au niveau du spot + 1
    res = []
    res.append(price) #prix
    res.append(delta) #delta
    res.append(delta2-delta) #gamma
    res.append(sum(-price + put_price_BS_model(spot, vol2, rfr, life, strike) + list([putPriceBinaryCashOrNothing(spot, strike, vol2, rfr, life, strike)]))) #vega
    res.append(sum(-price + put_price_BS_model(spot, vol, rfr, life2, strike) + list([putPriceBinaryCashOrNothing(spot, strike, vol, rfr, life2, strike)]))) #theta
    res.append(sum(-price + put_price_BS_model(spot, vol, rfr2, life, strike) + list([putPriceBinaryCashOrNothing(spot, strike, vol, rfr2, life, strike)]))) #rho
    return res


########################################################################################### Barrière Up and Out ############################################################################
def call_price_greeks_barrier_up_and_out(spot, vol, rfr, life, strike, niter, barrier):
    step = 2000 #nombre d'itérations
    spot2 = spot + 1 #spot augmentant de 1€
    spot3 = spot + 2 #spot augmentant de 2€
    vol2 = vol + 0.01 #volatilité augmentant de 1%
    rfr2 = rfr + 0.01 #taux snas risque augmentant de 1%
    life2 = life * (364/365) #maturité moins 1 jour
    #Prix du call au spot :
    price = callPriceBarrierUpAndOut(spot, strp, vol, rfr, life, barrier, step)
    #Prix du call au spot + 1 :
    price2 = callPriceBarrierUpAndOut(spot2, strike, vol, rfr, life, barrier, step)
    #Prix du call au spot + 2 :
    price3 = callPriceBarrierUpAndOut(spot3, strike, vol, rfr, life, barrier, step)
    res = []
    res.append(price) #prix
    res.append(price2-price) #delta
    res.append((price3-price2)-(price2-price)) #gamma
    res.append(callPriceBarrierUpAndOut(spot, strike, vol2, rfr, life, barrier, step) - price) #vega
    res.append(callPriceBarrierUpAndOut(spot, strike, vol, rfr, life2, barrier, step) - price) #theta
    res.append(callPriceBarrierUpAndOut(spot, strike, vol, rfr2, life, barrier, step) - price) #rho
    return res

def put_price_greeks_barrier_up_and_out(spot, vol, rfr, life, strike, niter, barrier):
    step = 2000 #nombre d'itérations
    spot2 = spot + 1 #spot augmentant de 1€
    spot3 = spot + 2 #spot augmentant de 2€
    vol2 = vol + 0.01 #volatilité augmentant de 1%
    rfr2 = rfr + 0.01 #taux snas risque augmentant de 1%
    life2 = life * (364/365) #maturité moins 1 jour
    #Prix du call au spot :
    price = putPriceBarrierUpAndOut(spot, strp, vol, rfr, life, barrier, step)
    #Prix du call au spot + 1 :
    price2 = putPriceBarrierUpAndOut(spot2, strike, vol, rfr, life, barrier, step)
    #Prix du call au spot + 2 :
    price3 = putPriceBarrierUpAndOut(spot3, strike, vol, rfr, life, barrier, step)
    res = []
    res.append(price) #prix
    #delta
    if price2 - price > 0:
        delta = price / (spot - barrier)
    else:
        delta = price2 - price    
    res.append(delta)
    res.append((price3-price2)-(price2-price)) #gamma
    res.append(putPriceBarrierUpAndOut(spot, strike, vol2, rfr, life, barrier, step) - price) #vega
    res.append(putPriceBarrierUpAndOut(spot, strike, vol, rfr, life2, barrier, step) - price) #theta
    res.append(putPriceBarrierUpAndOut(spot, strike, vol, rfr2, life, barrier, step) - price) #rho
    return res


########################################################################################### Asian ############################################################################
def callPriceAsian(v1, v2, v3, v4, v5, v6, v7):
# Cette fonction calcule le prix d'une option d'achat asiatique
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : prix d'exercice
# v3 : volatilité
# v4 : taux d'intérêt sans risque
# v5 : maturité
# v6 : temps depuis la création de l'option
# v7 : moyenne actuelle du cours du sous-jacent
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option d'achat asiatique
#
#----------------------------------------------------------------

   numberSteps = 50
   numberSimulations = 500

   timeStep = (v5 - v6) / numberSteps

# Fixe le générateur de nombre aléatoire
   randomSeed = 366
   random.seed(randomSeed)
   u = random.random()

   tableauSpots = [[0] * (numberSteps+1) for _ in range(numberSimulations)]
# Simulation de Monte Carlo sous l'hypothèse que le sous-jacent suit une distribution log-normale
   for i in range (numberSimulations):
       tableauSpots[i][0] = v1
       for j in range(1, numberSteps+1):
           u = random.random()
           z = stats.norm.ppf(u, 0, 1)
           tableauSpots[i][j] = tableauSpots[i][j-1] * exp((v4 - ((v3**2) / 2)) * timeStep + (v3 * sqrt(timeStep) * z))
           u = random.random()
         
   tableauResults = [0 * 1 for _ in range(numberSimulations)]
   result = 0
   for i in range(numberSimulations):
      for j in range (numberSteps+1):
          tableauResults[i] = tableauResults[i] + tableauSpots[i][j]
      tableauResults[i] = ((v6 / v5) * v7) + (((v5 - v6) / v5) * (tableauResults[i] / numberSteps))
      tableauResults[i] = max(0, tableauResults[i] - v2) * exp(-v4 * v5)
      result = result + (tableauResults[i] / numberSimulations)
      
   return result
  

def putPriceAsian(v1, v2, v3, v4, v5, v6, v7):
# Cette fonction calcule le prix d'une option de vente asiatique
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : prix d'exercice
# v3 : volatilité
# v4 : taux d'intérêt sans risque
# v5 : maturité
# v6 : temps depuis la création de l'option
# v7 : moyenne actuelle du cours du sous-jacent
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option de vente asiatique
#
#----------------------------------------------------------------

   numberSteps = 50
   numberSimulations = 500

   timeStep = (v5 - v6) / numberSteps

# Fixe le générateur de nombre aléatoire
   randomSeed = 366
   random.seed(randomSeed)
   u = random.random()

   tableauSpots = [[0] * (numberSteps+1) for _ in range(numberSimulations)]
# Simulation de Monte Carlo sous l'hypothèse que le sous-jacent suit une distribution log-normale
   for i in range (numberSimulations):
       tableauSpots[i][0] = v1
       for j in range(1, numberSteps+1):
           u = random.random()
           z = stats.norm.ppf(u, 0, 1)
           tableauSpots[i][j] = tableauSpots[i][j-1] * exp((v4 - ((v3**2) / 2)) * timeStep + (v3 * sqrt(timeStep) * z))
           u = random.random()
         
   tableauResults = [0 * 1 for _ in range(numberSimulations)]
   result = 0
   for i in range(numberSimulations):
      for j in range (numberSteps+1):
          tableauResults[i] = tableauResults[i] + tableauSpots[i][j]
      tableauResults[i] = ((v6 / v5) * v7) + (((v5 - v6) / v5) * (tableauResults[i] / numberSteps))
      tableauResults[i] = max(0, v2 - tableauResults[i]) * exp(-v4 * v5)
      result = result + (tableauResults[i] / numberSimulations)
      
   return result


def call_price_greeks_asian(spot, vol, rfr, life, strike, tsi, ca):
# Cette fonction renvoie le prix et les greeks d'une option d'achat asiatique
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : temps depuis la création de l'option
# v7 : moyenne actuelle du cours du sous-jacent
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option d'achat asiatique et ses grecques
#
#----------------------------------------------------------------

    spot2 = spot + 1 #spot augmentant de 1€
    spot3 = spot + 2 #spot augmentant de 2€
    vol2 = vol + 0.01 #volatilité augmentant de 1%
    rfr2 = rfr + 0.01 #taux snas risque augmentant de 1%
    life2 = life * (364/365) #maturité moins 1 jour
    tsi2 = tsi * (366/365) #temps écoulé depuis la création + 1 jour
    ca2 = ca  #moyenne actuelle du cours en jour + 1

    #Prix du call au spot :
    price = callPriceAsian(spot, strike, vol, rfr, life, tsi, ca)
    #Prix du call au spot + 1 :
    price2 = callPriceAsian(spot2, strike, vol, rfr, life, tsi, ca)
    #Prix du call au spot + 2 :
    price3 = callPriceAsian(spot3, strike, vol, rfr, life, tsi, ca)

    #Delta du call au niveau du spot :
    delta = price2 - price
    #Delta du call au niveau du spot + 1 :
    delta2 = price3 - price2

    res = []
    #Prix de l'option d'achat asiatique sur action
    res.append(price)
    #Delta
    res.append(delta)
    #Gamma
    res.append(delta2 - delta)
    #Vega
    res.append(callPriceAsian(spot, strike, vol2, rfr, life, tsi, ca) - price)
    #Theta
    res.append(callPriceAsian(spot, strike, vol, rfr, life2, tsi2, ca2) - price)
    #Rho
    res.append(callPriceAsian(spot, strike, vol, rfr2, life, tsi, ca) - price)

    return res


def put_price_greeks_asian(spot, vol, rfr, life, strike, tsi, ca):  
# Cette fonction renvoie le prix et les greeks d'une option de vente asiatique
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : temps depuis la création de l'option
# v7 : moyenne actuelle du cours du sous-jacent
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option de vente asiatique et ses grecques
#
#----------------------------------------------------------------

    spot2 = spot + 1 #spot augmentant de 1€
    spot3 = spot + 2 #spot augmentant de 2€
    vol2 = vol + 0.01 #volatilité augmentant de 1%
    rfr2 = rfr + 0.01 #taux snas risque augmentant de 1%
    life2 = life * (364/365) #maturité moins 1 jour
    tsi2 = tsi * (366/365) #temps écoulé depuis la création + 1 jour
    ca2 = ca  #moyenne actuelle du cours en jour + 1

    #Prix du call au spot :
    price = putPriceAsian(spot, strike, vol, rfr, life, tsi, ca)
    #Prix du call au spot + 1 :
    price2 = putPriceAsian(spot2, strike, vol, rfr, life, tsi, ca)
    #Prix du call au spot + 2 :
    price3 = putPriceAsian(spot3, strike, vol, rfr, life, tsi, ca)

    #Delta du call au niveau du spot :
    delta = price2 - price
    #Delta du call au niveau du spot + 1 :
    delta2 = price3 - price2

    res = []
    #Prix de l'option d'achat asiatique sur action
    res.append(price)
    #Delta
    res.append(delta)
    #Gamma
    res.append(delta2 - delta)
    #Vega
    res.append(putPriceAsian(spot, strike, vol2, rfr, life, tsi, ca) - price)
    #Theta
    res.append(putPriceAsian(spot, strike, vol, rfr, life2, tsi2, ca2) - price)
    #Rho
    res.append(putPriceAsian(spot, strike, vol, rfr2, life, tsi, ca) - price)

    return res




#continuer les modèles equity



#Fonction pour le sous jacent Currency:
#Cette fonction calcule le prix et les greeks pour une call européenne avec le modèle de Black et Scholes (sj currency)------------------------------------------------------------------------
def call_currency_price_greeks_BS_model(stop, vol, rfr, lif, strp, rfrf):
    d1 = ((log(stop / strp)) + ((rfr - rfrf + ((vol**2) / 2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf11 = stats.norm.cdf(d1, loc = 0, scale = 1)
    cdf12 = stats.norm.cdf(d2, loc = 0, scale = 1)
    pdf11 = stats.norm.pdf(d1, loc = 0, scale = 1)
    res = []
    res.append((stop * exp(-rfrf*lif) * cdf11) - (strp * exp(-(rfr * lif)) * cdf12)) #prix
    res.append(cdf11*exp(-rfrf*lif)) #delta
    res.append((pdf11 *exp(-rfrf*lif)) / (stop * vol * sqrt(lif))) #gamma
    res.append(stop * sqrt(lif) * pdf11 * exp(-rfrf*lif)/ 100) #vega
    res.append(((-(stop * pdf11 * vol * exp(-rfrf * lif)) / (2 * sqrt(lif))) + (rfrf * stop * cdf11 * exp(-rfrf * lif)) - (rfr * strp * exp(-rfr * lif) * cdf12)) / 365) #theta
    res.append((strp * lif * exp(-rfr * lif) * cdf12) / 100) #rho
    return res

 #Cette fonction calcule le prix et les greeks pour un put européenne avec le modèle de Black et Scholes (sj currency)---------------------------------------------------------------------------
def put_currency_price_greeks_BS_model(stop, vol, rfr, lif, strp, rfrf):
    d1 = ((log(stop / strp)) + ((rfr - rfrf + ((vol**2) / 2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf21 = stats.norm.cdf(-d1, loc = 0, scale = 1)
    cdf22 = stats.norm.cdf(-d2, loc = 0, scale = 1)
    pdf11 = stats.norm.pdf(d1, loc = 0, scale = 1)
    res = []
    res.append((strp * exp(-(rfr * lif)) * cdf22) - (stop * exp(-(rfrf * lif)) * cdf21)) #prix
    res.append(-cdf21 * exp(-rfrf * lif)) #delta
    res.append((pdf11 * exp(-rfrf * lif)) / (stop * vol * sqrt(lif))) #gamma
    res.append(stop * sqrt(lif) * pdf11 * exp(-rfrf * lif) /100) #vega
    res.append(((-(stop * pdf11 * vol * exp(-rfrf * lif)) / (2 * sqrt(lif))) - (rfrf * stop * cdf21 * exp(-rfrf * lif)) + (rfr * strp * exp(-rfr * lif) * cdf22)) / 365) #theta
    res.append((-(strp * lif * exp(-rfr * lif) * cdf22)) / 100) #rho
    return res


#Fonction pour le sous jacent Index:

#Fonction pour le sous jacent Futures:




def monteCarloEuropeanLogNormalCall(v1, v2, v3, v4, v5, v6, v7, v8, v9):
# Cette fonction renvoie le prix d'une option européenne d'achat via Monte Carlo avec le modèle log normal
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : dividendes
# v7 : nombre d'itérations
# v8 : nombre de simulations
# v9 : fixation de l'aléa
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option d'achat et l'écart type
#
#----------------------------------------------------------------

   timeStep = v4/v7 #Le pas d'itération

   global tableauSpots
   tableauSpots = [[0] * (v7+1) for _ in range(v8)]
   
   # Fixe le générateur de nombre aléatoire
   random.seed(v9)
   u = random.random()
   
   #Tableau contenant le passage du temps
   global tableauTime
   tableauTime = [[0] * (1) for _ in range(v7+1)]
   tableauTime[0] = 0 #Initialisation
   for i in range(1,v7+1):
       tableauTime[i] = tableauTime[i-1] + timeStep

   #Simulation de Monte Carlo sous l'hypothèse que le sous-jacent suit une distribution log-normale
   for i in range (v8):
       tableauSpots[i][0] = v1
       for j in range (1, v7+1):
            u = random.random()
            z = stats.norm.ppf(u, 0, 1)
            tableauSpots[i][j] =  tableauSpots[i][j-1] * exp((v3 - v6 - ((v2**2) / 2)) * timeStep + (v2 * sqrt(timeStep) * z))
            u = random.random()
          
   #Calcul du prix de l'option et l'écart-type de la simulation
   tableauResults = [[0] * (1) for _ in range(v8)]
   priceCum = 0
   for i in range (v8):
       tableauResults[i] = max(tableauSpots[i][v7] - v5, 0) * exp(-v3 * v4)
       priceCum = priceCum + tableauResults[i]
   
   res = []      
   res.append(priceCum / v8)
   res.append(statistics.stdev(tableauResults) / sqrt(v8))
   
   return res


def monteCarloEuropeanLogNormalPut(v1, v2, v3, v4, v5, v6, v7, v8, v9):
# Cette fonction renvoie le prix d'une option européenne de vente via Monte Carlo avec le modèle log normal
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : dividendes
# v7 : nombre d'itérations
# v8 : nombre de simulations
# v9 : fixation de l'aléa
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option de vente et l'écart type
#
#----------------------------------------------------------------

   timeStep = v4/v7 #Le pas d'itération

   global tableauSpots
   tableauSpots = [[0] * (v7+1) for _ in range(v8)]
   
   # Fixe le générateur de nombre aléatoire
   random.seed(v9)
   u = random.random()
   
   #Tableau contenant le passage du temps
   global tableauTime
   tableauTime = [[0] * (1) for _ in range(v7+1)]
   tableauTime[0] = 0 #Initialisation
   for i in range(1,v7+1):
       tableauTime[i] = tableauTime[i-1] + timeStep

   #Simulation de Monte Carlo sous l'hypothèse que le sous-jacent suit une distribution log-normale
   for i in range (v8):
       tableauSpots[i][0] = v1
       for j in range (1, v7+1):
            u = random.random()
            z = stats.norm.ppf(u, 0, 1)
            tableauSpots[i][j] =  tableauSpots[i][j-1] * exp((v3 - v6 - ((v2**2) / 2)) * timeStep + (v2 * sqrt(timeStep) * z))
            u = random.random()
          
   #Calcul du prix de l'option et l'écart-type de la simulation
   tableauResults = [[0] * (1) for _ in range(v8)]
   priceCum = 0
   for i in range (v8):
       tableauResults[i] = max(v5 - tableauSpots[i][v7], 0) * exp(-v3 * v4)
       priceCum = priceCum + tableauResults[i]
   
   res = []      
   res.append(priceCum / v8)
   res.append(statistics.stdev(tableauResults) / sqrt(v8))

   return res



def monteCarloEuropeanMertonJumpDiffusionCall(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12):
# Cette fonction renvoie le prix d'une option européenne d'achat via Monte Carlo avec le modèle Merton Jump Diffusion
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : dividendes
# v7 : nombre d'itérations
# v8 : nombre de simulations
# v9 : fixation de l'aléa
# v10: fréquence de saut par an 
# v11: moyenne des mouvements liée au saut
# v12: volatilité liée au saut
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option d'achat et l'écart type
#
#----------------------------------------------------------------

   timeStep = v4/v7 #le pas d'itération
   kappa = exp(v11) - 1
   drift = v3 - v6 - (v10*kappa) - (0.5*(v2**2)) #la tendance
 
   # Fixe le générateur de nombre aléatoire
   random.seed(v9)
   u = random.random()

   #Tableau contenant le passage du temps
   global tableauTime
   tableauTime = [[0] * (1) for _ in range(v7+1)]
   tableauTime[0] = 0 #Initialisation
   for i in range(1,v7+1):
       tableauTime[i] = tableauTime[i-1] + timeStep

   global tableauSpots
   tableauSpots = [[0] * (v7+1) for _ in range(v8)]
    
   #Simulation de Monte Carlo avec le modèle de Merton
   for i in range (v8):
      tableauSpots[i][0] = v1
      for j in range (1,v7+1):
          jj = 0
          if v10 != 0: 
             N_tt = int(stats.poisson.ppf(u, v10 * timeStep))
             if N_tt > 0:
                for S in range(1,N_tt+1):
                    u = random.random()
                    jj = jj +  stats.norm.ppf(u, v11 - ((v12**2)) / 2, v12)
          u = random.random()
          z = stats.norm.ppf(random.random(), 0, 1)
          tableauSpots[i][j] = tableauSpots[i][j-1] * exp((drift * timeStep) + (v2 * sqrt(timeStep) * z) + jj)
 

   #Calcul du prix de l'option et l'écart-type de la simulation
   tableauResults = [[0] * (1) for _ in range(v8)]
   priceCum = 0
   for i in range(v8):
       tableauResults[i] = max(tableauSpots[i][v7] - v5, 0) * exp(-v3 * v4)
       priceCum = priceCum + tableauResults[i]
    
   res = []      
   res.append(priceCum / v8)
   res.append(statistics.stdev(tableauResults) / sqrt(v8))
 
   return res



def monteCarloEuropeanMertonJumpDiffusionPut(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12):
# Cette fonction renvoie le prix d'une option européenne de vente via Monte Carlo avec le modèle Merton Jump Diffusion
#
# INPUTS
#----------------------------------------------------------------
# v1 : prix au comptant
# v2 : volatilité
# v3 : taux d'intérêt sans risque
# v4 : maturité
# v5 : prix d'exercice
# v6 : dividendes
# v7 : nombre d'itérations
# v8 : nombre de simulations
# v9 : fixation de l'aléa
# v10: fréquence de saut par an 
# v11: moyenne des mouvements liée au saut
# v12: volatilité liée au saut
#
# OUTPUT
#----------------------------------------------------------------
#
# Prix de l'option de vente et l'écart type
#
#----------------------------------------------------------------

   timeStep = v4/v7 #le pas d'itération
   kappa = exp(v11) - 1
   drift = v3 - v6 - (v10*kappa) - (0.5*(v2**2)) #la tendance
 
   # Fixe le générateur de nombre aléatoire
   random.seed(v9)
   u = random.random()

   #Tableau contenant le passage du temps
   global tableauTime
   tableauTime = [[0] * (1) for _ in range(v7+1)]
   tableauTime[0] = 0 #Initialisation
   for i in range(1,v7+1):
       tableauTime[i] = tableauTime[i-1] + timeStep

   global tableauSpots
   tableauSpots = [[0] * (v7+1) for _ in range(v8)]
    
   #Simulation de Monte Carlo avec le modèle de Merton
   for i in range (v8):
      tableauSpots[i][0] = v1
      for j in range (1,v7+1):
          jj = 0
          if v10 != 0: 
             N_tt = int(stats.poisson.ppf(u, v10 * timeStep))
             if N_tt > 0:
                for S in range(1,N_tt+1):
                    u = random.random()
                    jj = jj +  stats.norm.ppf(u, v11 - ((v12**2)) / 2, v12)
          u = random.random()
          z = stats.norm.ppf(random.random(), 0, 1)
          tableauSpots[i][j] = tableauSpots[i][j-1] * exp((drift * timeStep) + (v2 * sqrt(timeStep) * z) + jj)
 

   #Calcul du prix de l'option et l'écart-type de la simulation
   tableauResults = [[0] * (1) for _ in range(v8)]
   priceCum = 0
   for i in range(v8):
       tableauResults[i] = max(v5 - tableauSpots[i][v7], 0) * exp(-v3 * v4)
       priceCum = priceCum + tableauResults[i]
    
   res = []      
   res.append(priceCum / v8)
   res.append(statistics.stdev(tableauResults) / sqrt(v8))
 
   return res





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
