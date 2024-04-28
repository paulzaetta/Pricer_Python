"""
from math import *

def bond_pricing(principal, bondLife, cpnRate, settFreq, r1=0, r2=0, r3=0, r4=0, r5=0, r6=0, r7=0, r8=0, r9=0, r10=0, r11=0, r12=0):

    frequence = settFreq

    compteur_periodes = 0
    price = 0

    prin = principal
    bond_life = bondLife
    coupon = cpnRate

    if (frequence=="Monthly"):
        multiplicateur_periodes = 12
    elif (frequence=="Quarterly"):
        multiplicateur_periodes = 4
    elif (frequence=="Semi-Annual"):
        multiplicateur_periodes = 2
    elif (frequence=="Annual"):
        multiplicateur_periodes = 1
    

    nb_periodes = bond_life * multiplicateur_periodes

    #Calcul prix
    for i in range(1, nb_periodes):
        compteur_periodes = compteur_periodes + (1 / multiplicateur_periodes)
        taux_zc = Cells(i + 2, 7).Value
        if (compteur_periodes != bond_life):
            price = price + (coupon / multiplicateur_periodes) * exp(-taux_zc * compteur_periodes)
        else:
            price = price + ((principal / 100) + coupon / multiplicateur_periodes) * exp(-taux_zc * compteur_periodes)
    
    price = price * 100
    

    #Calcul Yield To Maturity
    Dim tableau_flux() As Double
    ReDim tableau_flux(0 To nb_periodes)
    tableau_flux(0) = -price
    For k = 1 To nb_periodes - 1
        tableau_flux(k) = coupon / multiplicateur_periodes
    Next k

    tableau_flux(nb_periodes) = coupon / multiplicateur_periodes + principal / 100
    TRA = Application.WorksheetFunction.IRR(tableau_flux)
    TRA = TRA * multiplicateur_periodes
    Range("D22").Value = TRA

    #Calcul Duration
    For j = 1 To nb_periodes
        compteur_periodes_2 = compteur_periodes_2 + (1 / multiplicateur_periodes)
        taux_zc = Cells(j + 2, 7).Value
        If compteur_periodes_2 <> bond_life Then
            num_duration = num_duration + (compteur_periodes_2 * coupon / multiplicateur_periodes) * Exp(-taux_zc * compteur_periodes_2)
        Else
            num_duration = num_duration + compteur_periodes_2 * ((principal / 100) + coupon / multiplicateur_periodes) * Exp(-taux_zc * compteur_periodes_2)
        End If
    Next j
    duration = num_duration / price
    Range("D23").Value = duration

    #Calcul sensibilite
    mod_duration = duration / (1 + TRA)
    Range("D24").Value = mod_duration

    #Calcul convexite
    For l = 1 To nb_periodes
        compteur_periodes_3 = compteur_periodes_3 + (1 / multiplicateur_periodes)
        taux_zc = Cells(j + 2, 7).Value
        If compteur_periodes_3 <> bond_life Then
            num_conv = num_conv + (compteur_periodes_3 ^ 2 * coupon / multiplicateur_periodes) * Exp(-taux_zc * compteur_periodes_3)
        Else
            num_conv = num_conv + compteur_periodes_3 ^ 2 * ((principal / 100) + coupon / multiplicateur_periodes) * Exp(-taux_zc * compteur_periodes_3)
        End If
    Next l
    convexite = (1 / (1 + TRA) ^ 2) * (duration + num_conv / price)
    Range("D25").Value = convexite
    End If


    return price, ytm, dur, mdur, con
"""
