import numpy as np
import pylab as pl

e_max = 100
ec_50 = 1
conc = np.arange(0,101,0.5)
conc = [0.001,0.01,0.1,1,10,100,1000,10000]
conc = np.asarray(conc)
#log_conc = np.logspace(0.001,100)
#print log_conc
#print conc

gamma = 0.5

#Hill equation
effect = (e_max*(conc**gamma))/((ec_50**gamma)+(conc**gamma))
#print effect

pl.figure(1)
pl.plot(conc,effect)
pl.semilogx()

'''
gamma = 1
effect = (e_max*(conc**gamma))/((ec_50**gamma)+(conc**gamma))
pl.plot(conc,effect)
gamma = 2
effect = (e_max*(conc**gamma))/((ec_50**gamma)+(conc**gamma))
pl.plot(conc,effect)
'''

'''
f2 = pl.figure(2)
gamma = 0.5
effect = (e_max*(log_conc**gamma))/((ec_50**gamma)+(log_conc**gamma))
pl.plot(log_conc,effect)
gamma = 1
effect = (e_max*(conc**gamma))/((ec_50**gamma)+(conc**gamma))
pl.plot(conc,effect)
pl.semilogx()
gamma = 2
effect = (e_max*(conc**gamma))/((ec_50**gamma)+(conc**gamma))
pl.plot(conc,effect)
pl.semilogx()
'''

pl.show()
