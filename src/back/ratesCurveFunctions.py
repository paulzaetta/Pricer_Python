import numpy as np
import pandas as pd
from datetime import date
from scipy import interpolate

from pandas.tseries.offsets import DateOffset
from datetime import datetime
from datetime import timedelta
from datetime import date
  

def refreshCurve(data):
# Cette fonction renvoie les taux euros de 1d à 50y
#
# INPUTS
#------------------------------------------------------------------------------
# Les taux euros ester, eurib1, eurib3, eurib6, eurib12 de 1d à 50y en tenor
#------------------------------------------------------------------------------
# OUTPUT
#------------------------------------------------------------------------------
# Les taux euros daily ester, eurib1, eurib3, eurib6, eurib12 de 1d à 50y
#------------------------------------------------------------------------------

#rajouter les jours en index dans mon tableau -> faire avec pandes ??????
#enlever les weekends et les jours fériés -> utiliser le calendar TARGET?
#faire un dictionnaire clé = date et index et valeur = taux


    dataRatesCurve = data.to_numpy()
    ester = dataRatesCurve[:,1]
    eurib1 = dataRatesCurve[:,2]
    eurib3 = dataRatesCurve[:,3]
    eurib6 = dataRatesCurve[:,4]
    eurib12 = dataRatesCurve[:,5]

    time = np.array(list(range(1, 21)))
    startDate = date.today()
    year = int(startDate.strftime("%Y"))
    endDate = startDate.replace(year=year+50)
    delta = endDate - startDate
    deltaDays = delta.days
    timeNew = np.linspace(1, 20, deltaDays)


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



def refreshCurve2(data):
# Cette fonction renvoie les taux euros de 1d à 50y
#
# INPUTS
#------------------------------------------------------------------------------
# Les taux euros ester, eurib1, eurib3, eurib6, eurib12 de 1d à 50y en tenor
#------------------------------------------------------------------------------
# OUTPUT
#------------------------------------------------------------------------------
# Les taux euros daily ester, eurib1, eurib3, eurib6, eurib12 de 1d à 50y
#------------------------------------------------------------------------------

#j'ai sélectionné les business days -> vaudrait mieux avoir le calendrier target ? 

    dataRatesCurve = data.to_numpy()
    ester = dataRatesCurve[:,1]
    eurib1 = dataRatesCurve[:,2]
    eurib3 = dataRatesCurve[:,3]
    eurib6 = dataRatesCurve[:,4]
    eurib12 = dataRatesCurve[:,5]

    time = np.array(list(range(1, 21)))
    startDate = date.today()
    year = int(startDate.strftime("%Y"))
    endDate = startDate.replace(year=year+50)
    indexDate = pd.date_range(start=startDate, end=endDate, freq='B')
    deltaDays = len(indexDate)
    timeNew = np.linspace(1, 20, deltaDays)


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

    indexDate = indexDate.to_numpy()
                                    
    dataRatesCurve = {
        'DATE': indexDate,
        'ESTER' : interpoEster(timeNew),
        'EURIB1' : interpoEurib1(timeNew),
        'EURIB3' : interpoEurib3(timeNew),
        'EURIB6' : interpoEurib6(timeNew),
        'EURIB12' : interpoEurib12(timeNew)
    }

    dataRatesCurve = pd.DataFrame(dataRatesCurve)

    dataRatesCurve.set_index("DATE", inplace=True)
     
    return dataRatesCurve



def swapComputation(startDate,endDate,payOrRec,notFixed,notFloat,rateFixed,floatIndex,setfFixed,setfFloat,basFixed,basFloat,lastE,dataRatesCurve):
# Cette fonction calcule le prix et la DV01 du swap
#
# INPUTS
#------------------------------------------------------------------------------
# startDate      : la start date du swap
# endDate        : la end date du swap
# payOrRec       : sens du swap
# notFixed       : notional de la fixed leg
# notFloat       : notional de la float leg
# rateFixed      : taux fixe
# floatIndex     : indice
# setfFixed      : roll frequency de la leg fixed
# setfFloat      : roll frequency de la leg float
# basFixed       :
# basFloat       :
# lastE          :
# dataRatesCurve : matrice de taux
#------------------------------------------------------------------------------
# OUTPUTS
#------------------------------------------------------------------------------
# prix           : prix du swap 
# sensi          : DV01 du swap
# fixedLeg       : tableau des flux de la fixed leg
# floatLeg       : tableau des flux de la float leg
#------------------------------------------------------------------------------
    
    #startDate = datetime.strptime(startDate, '%Y-%m-%d')
    #endDate = datetime.strptime(endDate, '%Y-%m-%d')

    startDate = datetime.strptime(startDate, '%m/%d/%y')
    endDate = datetime.strptime(endDate, '%m/%d/%y')

    #Ajustement en fonction des fréquences de roll:
    if (setfFixed == "Annual" and setfFloat == "Annual"):
        i = 1
        months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
        period = 12
        indexTEST = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)
    elif (setfFixed == "Semi-Annual" and setfFloat == "Semi-Annual"):
        i = 1/2
        months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
        period = 6
        indexTEST = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)
    elif (setfFixed == "Quarterly" and setfFloat == "Quarterly"):
        i = 1/4
        months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
        period = 3
        indexTEST = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)
    elif (setfFixed == "Monthly" and setfFloat == "Monthly"):
        i = 1/12
        months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
        period = 1
        indexTEST = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)
    elif (setfFixed == "Daily" and setfFloat == "Daily"):
        i = 1 / 365 #366 


    #Rec ou pay le fixed rate: 
    if payOrRec == 0:
        payrec = 1 #on recoit
    else: 
        payrec = -1 #on paye
    

    #Fixed Leg:
    #ne marche pas pour le daily et le continu..... que periode = 1, 3, 6 ou 12
    months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
    datesRoll = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)
    
    #on décale les start/end dates au prochain jour ouvré si close day
    for i, date in enumerate(datesRoll):
        if date.weekday() >= 5:  # Saturday or Sunday
            datesRoll = datesRoll.delete(i)
            datesRoll = datesRoll.insert(i, date + pd.offsets.BDay())
    
    nbrDays = datesRoll[1:] - datesRoll[:-1]
    nbrDays = pd.DataFrame(data=nbrDays.days, columns=["Days"])

    startDates = pd.DataFrame(data=datesRoll[:-1], columns=["Start"])
    endDates = pd.DataFrame(data=datesRoll[1:], columns=["End"])
    
    #on décale les dates de paiement au prochain jour ouvré si close day
    paymentDates = datesRoll[1:] + timedelta(days=2)
    for i, date in enumerate(paymentDates):
        if date.weekday() >= 5: # Saturday or Sunday
            paymentDates = paymentDates.delete(i)
            paymentDates = paymentDates.insert(i, date + pd.offsets.BDay())

    nbrDaysPay=paymentDates-pd.Timestamp(date.today())        
    nbrDaysPay=pd.DataFrame(data=nbrDaysPay.days, columns=["CumDays"])
    paymentDates=pd.DataFrame(data=paymentDates, columns=["Date"])
    
    
    finalResultsFixed=pd.concat([startDates, endDates], axis=1) #start et end dates
    finalResultsFixed=pd.concat([finalResultsFixed, nbrDays], axis=1) #nbr de jours par période
    finalResultsFixed['Rate'] = rateFixed #fixed rate
    finalResultsFixed['Notional'] = notFixed #notional on the fixed leg
    finalResultsFixed=pd.concat([finalResultsFixed, paymentDates], axis=1) # payment dates
    finalResultsFixed['Flows'] = round(payrec * finalResultsFixed['Days'] * finalResultsFixed['Rate'] * finalResultsFixed['Notional'] / 100 / 360,5) #flows
    finalResultsFixed=pd.concat([finalResultsFixed, nbrDaysPay], axis=1) #nbr de jours pour l'actualisation

    
    #faire l'actualisation des flux -> récupérer le taux sans risque de la date de paiment et divisé le flux par ce taux (1+r)^per
    tableauDiscount = [[0] * (2) for _ in range(len(finalResultsFixed))]
    for i in range(len(finalResultsFixed)):
        a = finalResultsFixed.iloc[i]['Date'].date() 
        a = a.strftime('%Y-%m-%d')
        tableauDiscount[i][0] = a
        tableauDiscount[i][1] = dataRatesCurve.iloc[dataRatesCurve.index.get_loc(a), dataRatesCurve.columns.get_loc('ESTER')]

    # Convert list to DataFrame
    tableauDiscount_df = pd.DataFrame(tableauDiscount, columns=['Date', 'Zeros'])
    tableauDiscount_df.drop(columns=['Date'], inplace=True)

    finalResultsFixed= pd.concat([finalResultsFixed, round(tableauDiscount_df,5)], axis=1) #taux ZC
    finalResultsFixed['Discount'] = round(1 / ((1+(finalResultsFixed['Zeros']/100))**(finalResultsFixed['CumDays']/180)),5)

    finalResultsFixed['PV'] = round(finalResultsFixed['Flows'] * finalResultsFixed['Discount'],2)

    fixedLegPV = sum(finalResultsFixed['PV'])



    #Float Leg:
    # faire une deuxième variable period si roll différent entre la fixed et la float leg - pour le moment on assume meme roll
    months = (endDate.year - startDate.year)*12 + endDate.month - startDate.month
    datesRoll = pd.DatetimeIndex([endDate - DateOffset(months=e) for e in range(0, months, period)][::-1]).insert(0, startDate)

    #on décale les start/end dates au prochain jour ouvré si close day
    for i, date in enumerate(datesRoll):
        if date.weekday() >= 5:  # Saturday or Sunday
            datesRoll = datesRoll.delete(i)
            datesRoll = datesRoll.insert(i, date + pd.offsets.BDay())

    nbrDays = datesRoll[1:] - datesRoll[:-1]
    nbrDays = pd.DataFrame(data=nbrDays.days, columns=["Days"])

    startDates = pd.DataFrame(data=datesRoll[:-1], columns=["Start"])
    endDates = pd.DataFrame(data=datesRoll[1:], columns=["End"])

    #on décale les dates de paiement au prochain jour ouvré si close day
    paymentDates = datesRoll[1:] + timedelta(days=2)
    for i, date in enumerate(paymentDates):
        if date.weekday() >= 5: # Saturday or Sunday
            paymentDates = paymentDates.delete(i)
            paymentDates = paymentDates.insert(i, date + pd.offsets.BDay())
    

    fixingDates = datesRoll[:-1] - timedelta(days=2)
    for i, date in enumerate(fixingDates):
                if date.weekday() >= 5: # Saturday or Sunday
                    fixingDates = fixingDates.delete(i)
                    fixingDates = fixingDates.insert(i, date + pd.offsets.BDay())
    fixingDates = pd.DataFrame(data=fixingDates, columns=["Fixing"])

    #date de fixing à modifier si ester (backard looking)
    #fixingDates = pd.DataFrame(datesRoll[:-1] - timedelta(days=2), columns=["Fixing"])
    finalResultsFloat = pd.concat([startDates, endDates], axis=1) #start et end dates
    finalResultsFloat = pd.concat([finalResultsFloat, fixingDates], axis=1) # dates de fixing
    finalResultsFloat = pd.concat([finalResultsFloat, nbrDays], axis=1) #nbr de jours par période

    #Récupération de taux forward
    tableauFlowardFloat = [[0] * (2) for _ in range(len(finalResultsFloat))]
    for i in range(len(finalResultsFloat)):
        a = finalResultsFloat.iloc[i]['Fixing'].date() 
        a = a.strftime('%Y-%m-%d')
        tableauFlowardFloat[i][0] = a
        tableauFlowardFloat[i][1] = dataRatesCurve.iloc[dataRatesCurve.index.get_loc(a), dataRatesCurve.columns.get_loc(floatIndex)]

    tableauFlowardFloat_df = pd.DataFrame(tableauFlowardFloat, columns=['Date', 'Forward'])
    tableauFlowardFloat_df.drop(columns=['Date'], inplace=True)
    finalResultsFloat = pd.concat([finalResultsFloat, round(tableauFlowardFloat_df,5)], axis=1) #taux forward

    nbrDaysPay=paymentDates-pd.Timestamp(date.today())        
    nbrDaysPay=pd.DataFrame(data=nbrDaysPay.days, columns=["CumDays"])
    paymentDates=pd.DataFrame(data=paymentDates, columns=["Date"])


    finalResultsFloat['Spread'] = 0
    finalResultsFloat['All Rate'] = round(finalResultsFloat['Forward'] + finalResultsFloat['Spread'],5) # taux forward plus le spread
    finalResultsFloat['Notional'] = notFloat #notional de la float leg
    finalResultsFloat = pd.concat([finalResultsFloat, paymentDates], axis=1) # payment dates
    finalResultsFloat['Flows'] = round(-1 * payrec * finalResultsFloat['Days'] * finalResultsFloat['All Rate'] * finalResultsFloat['Notional'] / 100 / 360,5) #flows
    finalResultsFloat = pd.concat([finalResultsFloat, nbrDaysPay], axis=1) #nbr de jours pour l'actualisation

    #faire l'actualisation des flux -> récupérer le taux sans risque de la date de paiment et divisé le flux par ce taux (1+r)^per
    tableauDiscount = [[0] * (2) for _ in range(len(finalResultsFloat))]
    for i in range(len(finalResultsFloat)):
        a = finalResultsFloat.iloc[i]['Date'].date() 
        a = a.strftime('%Y-%m-%d')
        tableauDiscount[i][0] = a
        tableauDiscount[i][1] = dataRatesCurve.iloc[dataRatesCurve.index.get_loc(a), dataRatesCurve.columns.get_loc('ESTER')]

    #convert list to DataFrame
    tableauDiscount_df = pd.DataFrame(tableauDiscount, columns=['Date', 'Zeros'])
    tableauDiscount_df.drop(columns=['Date'], inplace=True)

    finalResultsFloat= pd.concat([finalResultsFloat, round(tableauDiscount_df,5)], axis=1) #taux ZC
    finalResultsFloat['Discount'] = round(1 / ((1+(finalResultsFloat['Zeros']/100))**(finalResultsFloat['CumDays']/180)),5)
    
    finalResultsFloat['PV'] = round(finalResultsFloat['Flows'] * finalResultsFloat['Discount'],2)

    floatLegPV = sum(finalResultsFloat['PV'])


    #prix du swap:
    priceSwap = fixedLegPV + floatLegPV 
    

    #dv01 du swap: 
    finalResultsFloat2 = finalResultsFloat
    finalResultsFloat2['Forward'] = finalResultsFloat['Forward'] + 0.01
    finalResultsFloat2['All Rate'] = finalResultsFloat2['Forward'] + finalResultsFloat2['Spread']
    finalResultsFloat2['Flows'] = -1 * payrec * finalResultsFloat2['Days'] * finalResultsFloat2['All Rate'] * finalResultsFloat2['Notional'] / 100 / 360
    finalResultsFloat2['PV'] = round(finalResultsFloat2['Flows'] * finalResultsFloat2['Discount'],2)
    floatLegShift = sum(finalResultsFloat2['PV'])

    dv01 = (fixedLegPV + floatLegShift) - priceSwap

    print(finalResultsFixed)
    print(finalResultsFloat)


    return priceSwap, dv01, fixedLegPV, floatLegPV, finalResultsFixed, finalResultsFloat, finalResultsFloat2
