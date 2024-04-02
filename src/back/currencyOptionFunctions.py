from math import *
from scipy import stats

#Cette fonction calcule le prix et les greeks pour une call européenne avec le modèle de Black et Scholes (sj currency)
def call_currency_price_greeks_BS_model(stop, vol, rfr, lif, strp, rfrf):
    d1 = ((log(stop / strp)) + ((rfr - rfrf + ((vol**2) / 2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf11 = stats.norm.cdf(d1, loc = 0, scale = 1)
    cdf12 = stats.norm.cdf(d2, loc = 0, scale = 1)
    pdf11 = stats.norm.pdf(d1, loc = 0, scale = 1)
    price = (stop * exp(-rfrf*lif) * cdf11) - (strp * exp(-(rfr * lif)) * cdf12)
    delta = cdf11*exp(-rfrf*lif)
    gamma = (pdf11 *exp(-rfrf*lif)) / (stop * vol * sqrt(lif))
    vega = stop * sqrt(lif) * pdf11 * exp(-rfrf*lif)/ 100
    theta = ((-(stop * pdf11 * vol * exp(-rfrf * lif)) / (2 * sqrt(lif))) + (rfrf * stop * cdf11 * exp(-rfrf * lif)) - (rfr * strp * exp(-rfr * lif) * cdf12)) / 365
    rho = (strp * lif * exp(-rfr * lif) * cdf12) / 100
    return price, delta, gamma, vega, theta, rho

 #Cette fonction calcule le prix et les greeks pour un put européenne avec le modèle de Black et Scholes (sj currency)
def put_currency_price_greeks_BS_model(stop, vol, rfr, lif, strp, rfrf):
    d1 = ((log(stop / strp)) + ((rfr - rfrf + ((vol**2) / 2)) * lif)) / (vol * sqrt(lif))
    d2 = d1 - (vol*sqrt(lif))
    cdf21 = stats.norm.cdf(-d1, loc = 0, scale = 1)
    cdf22 = stats.norm.cdf(-d2, loc = 0, scale = 1)
    pdf11 = stats.norm.pdf(d1, loc = 0, scale = 1)
    price = (strp * exp(-(rfr * lif)) * cdf22) - (stop * exp(-(rfrf * lif)) * cdf21)
    delta = -cdf21 * exp(-rfrf * lif)
    gamma = (pdf11 * exp(-rfrf * lif)) / (stop * vol * sqrt(lif))
    vega = stop * sqrt(lif) * pdf11 * exp(-rfrf * lif) /100
    theta = ((-(stop * pdf11 * vol * exp(-rfrf * lif)) / (2 * sqrt(lif))) - (rfrf * stop * cdf21 * exp(-rfrf * lif)) + (rfr * strp * exp(-rfr * lif) * cdf22)) / 365
    rho = (-(strp * lif * exp(-rfr * lif) * cdf22)) / 100
    return price, delta, gamma, vega, theta, rho

