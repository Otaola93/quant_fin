# se installa con pip desde github con:
# python -m pip install --trusted-host pypi.org git+https://github.com/Otaola93/quant_fin.git#egg=quant_fin


import numpy as np
import datetime
from scipy.stats import norm

def opcion_bs(S0,K,ini,fin,sigma,r,d,tipo='call',baseT=365):
    '''
    S0      subyacente a fecha valor
    K       strike
    ini     fecha valor en formato aaaa-mm-dd
    fin     fecha fin   en formato aaaa-mm-dd
    sigma   volatilidad
    r       tipo continuo libre de riesgo
    d       dividendo
    tipo    call o put
    baseT   base temporal
    '''

    ini = datetime.date(int(ini[:4]),int(ini[5:7]),int(ini[8:]))
    fin = datetime.date(int(fin[:4]),int(fin[5:7]),int(fin[8:]))
    
    T = (fin-ini).days / baseT

    d1 = 1 / (np.sqrt(T) * sigma) * (np.log(S0 / K) + (r - d + (sigma ** 2) / 2) * T)
    d2 = d1 - sigma * np.sqrt(T)

    p_fwd = S0 * np.exp((r - d) * T)

    if tipo == 'call':
        return np.exp(-r * T) * (   norm.cdf(d1) * p_fwd - norm.cdf( d2) * K)
    elif tipo=='put':
        return np.exp(-r * T) * (- norm.cdf(-d1) * p_fwd + norm.cdf(-d2) * K)
    else:
        print('tipo de opcion no permitido (call/put)')
        return 'tipo de opcion no permitido (call/put)'