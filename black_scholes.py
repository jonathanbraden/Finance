#!/usr/bin/env python

# To Do:
#  - Add dividends (discrete + continuous)
#  - Add some checks and corner cases to calculation (t=0, vol=0,s=k)
#  - Add Greeks

from scipy.stats import norm
import numpy as np

class OptionBS():
    def __init__(self,s,k,r,vol,t):
        self.s = s
        self.k = k
        self.r = r
        self.vol = vol
        self.t = t
        return

class CallBS(OptionBS):
    def __init__(self,s,k,r,vol,t):
        # Add call to super
        return

class PutBS(OptionBS):
    def __init__(self,s,k,r,vol,t):
        # Add call to super
        return
    
class BlackScholes():
    def __init__(self,s,k,r,vol,t):
        self.s = s
        self.k = k
        self.r = r
        self.vol = vol
        self.t = t
        return

    def call_european(self):
        d1 = self.delta_z()
        d2 = self.exercise_z()
        return self.s*norm.cdf(d1) - self.k*np.exp(-self.r*self.t)*norm.cdf(d2)

    def put_european(self):
        d1 = self.delta_z()
        d2 = self.exercise_z()
        return self.k*np.exp(-self.r*self.t)*norm.cdf(-d2) - self.s*norm.cdf(-d1)
    
    def exercise_z(self):
        return (np.log(self.s/self.k) + (self.r-0.5*self.vol**2)*self.t)/(self.vol*np.sqrt(self.t))

    def delta_z(self):
        return (np.log(self.s/self.k) + (self.r+0.5*self.vol**2)*self.t)/(self.vol*np.sqrt(self.t))

    def delta_call(self):
        return norm.cdf(self.delta_z)

    def gamma_call(self):
        d1 = self.delta_z()
        return np.exp(-0.5*d1**2)/np.sqrt(2.*np.pi)/self.s

    def rho_call(self):
        return

    def vega_call(self):
        return

    def tau_call(self):
        return
    
    def delta_put(self):
        return 

    def gamma_put(self):
        return
    
    def rho_put(self):
        return
    
    def vega_put(self):
        return

    def tau_put(self):
        return

    def implied_vol(self):
        return
    
    
# Add special cases for at the money (where I can take t to 0)
# Add special case for t=0 (get step function)
# Add special case of vol=0

def exercise_z(s,k,r,vol,t):
    return (np.log(s/k) + (r-0.5*vol**2)*t)/(vol*np.sqrt(t))

def delta_z(s,k,r,vol,t):
    return (np.log(s/k) + (r+0.5*vol**2)*t)/(vol*np.sqrt(t))

def put_call_parity_european():
    return

def call_european(s,k,r,vol,t):
    d1 = delta_z(s,k,r,vol,t)
    d2 = exercise_z(s,k,r,vol,t)
    return s*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)

def put_european(s, k, r, vol, t, q, d=0.):
    """
    Compute the Black-Scholes price of a European put option

      :param s:   - Current stock price
      :param k:   - Strike price
      :param r:   - continuously compounded risk free rate
      :param vol: - volatility
      :param t:   - time to maturity
      :param q:   - dividend yield rate
      :param d:   - present value of dividends

    Note: The risk free rate, time, dividend yield and volatility should all be computed in the same units (e.g. per annun)
    
    """
    d1 = delta_z(s*np.exp(-q*t),k,r,vol,t)
    d2 = exercise_z(s*np.exp(-q*t),k,r,vol,t)
    return k*np.exp(-r*t)*norm.cdf(-d2) - s*np.exp(-q*t)*norm.cdf(-d1)

if __name__=="__main__":
    c = call_european(100,100,0.05,0.2,0.5)
    #p = put_european(100,100,0.05,0.2,0.5)
    p = put_european(83,95,0.05,0.3,1.,0.03)

    aVals = np.linspace(1.,100.,100)
    pVals = [ put_european(a_,95,0.05,0.3,1.,0.03) for a_ in aVals ]

    pVals = np.array(pVals)
