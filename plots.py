#################################################
# Written by Giovanna Cottin (gfcottin@gmail.com)
#################################################
import os,sys
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.random import normal
import matplotlib.font_manager as font_manager
from matplotlib.colors import LogNorm
from matplotlib.ticker import ScalarFormatter 
from pylab import *
import matplotlib.gridspec as gridspec
from numpy import linspace, meshgrid
# from matplotlib.mlab import griddata
from scipy.interpolate import griddata
from matplotlib import ticker, cm
import operator
#################
## Plotting Style
#################
rcParams['legend.loc'] = 'best'
#Direct input 
plt.rcParams['text.latex.preamble']=[r"\usepackage{lmodern}"]
#Options
params = {'text.usetex' : True,
          'font.size' : 15,
          'font.family' : 'lmodern',
          'text.latex.unicode': True,
          'legend.fontsize': 10
          }
plt.rcParams.update(params) 

electrons_file=np.loadtxt('electrons.dat')
neutrinos_file=np.loadtxt('neutrinos.dat')

#To separate the columns one can do
electrons_pt=electrons_file[:]

neutrinos_mass=neutrinos_file[:,0]
neutrinos_boost=neutrinos_file[:,1]
neutrinos_pt=neutrinos_file[:,2]


fig1=plt.figure(1)
plt.hist(electrons_pt,bins=50,color="black",alpha=0.5,histtype="step",lw=2)
plt.xlabel('$ p_{T}$ [GeV]',fontsize=15)
plt.savefig('SST_electrons_plots.pdf', bbox_inches='tight')

fig2=plt.figure(2)
plt.subplot(131)
ax2 = fig1.add_subplot(121)
ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)
plt.gca().set_rasterization_zorder(0)
plt.subplot(131)
#plt.xlim(0,2000)
plt.hist(neutrinos_mass,bins=50,color="red",alpha=0.5,histtype="step",lw=2)
plt.xlabel('$N$ mass [GeV]',fontsize=15)
# plt.legend()
plt.subplot(132)
plt.xlim(0,10)
plt.hist(neutrinos_boost,bins=50,color="blue",alpha=0.5,histtype="step",lw=2)
plt.xlabel('$  \\gamma$',fontsize=15)
# plt.legend()
plt.subplot(133)
plt.hist(neutrinos_pt,bins=50,color="red",alpha=0.5,histtype="step",lw=2)
plt.xlabel('$ p_{T}$ [GeV]',fontsize=15)
plt.savefig('SST_neutrinos_plots.pdf', bbox_inches='tight')
####################################
