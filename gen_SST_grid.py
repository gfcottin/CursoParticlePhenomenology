import os,sys
import numpy as np
import math

mN    = np.array([10,20,30,40,50])
for mass in mN:
    f = open("SST_gen_mg5_GRID/gen_SST_GRID_mg5_"+str(mass),'w')
    f.write("import model SM_SST1_UFO\n")
    f.write("generate p p > w+, (w+ > e+ nu4)\n")
    f.write("output SST_GRID_e/SST_GRID_e-"+str(mass)+"\n")
    f.write("launch -i SST_GRID_e/SST_GRID_e-"+str(mass)+"\n")
    f.write("generate_events\n")
    f.write("/home/chubi/Desktop/MyGit/CursoParticlePhenomenology/param_card_SST_e.dat\n")
    f.write("set Vv 4 1 1e-04\n")
    f.write("set MASS 112 "+str(mass)+"\n")
    f.write("set DECAY 112 Auto\n")
    f.close()
