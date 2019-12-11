import sys
import os
import gzip
import numpy as np
import matplotlib.pyplot as plt


outfile = "SST_sigma.txt" 
path    = "/home/chubi/Desktop/MyGit/CursoParticlePhenomenology/MG5_aMC_v2_4_3/SST_GRID_e/"

subfolders=[x for x in os.listdir(path) if os.path.isdir(path+x)]
print(subfolders)

out     = {'sig':[],'mass':[]}

for ss in subfolders:
    sss=ss.split('-')
    run=sss[1]
    fp=path+ss
    print(fp)
    with gzip.open(fp+'/Events/run_01/unweighted_events.lhe.gz') as ff:
        # print(ff)
        for l in ff:
            if '#  Integrated weight (pb)  :' in l:
                sig=l.split()[-1]
                print(sig)
            if '# fv_4' in l:
                mass=l.split()[1]
                print(mass)
    out['sig'].append(sig)
    out['mass'].append(mass)


plt.figure()
plt.title("$\\sigma (pp\\to W^{+}\\to e^{+} N)$ [pb]",fontsize=15)
plt.plot(out['mass'],out['sig'],alpha=0.7,lw=2,color='red')
#plt.xlim([20,1000])
#plt.ylim([1e-5,1e-3])
plt.yscale('log')
plt.xlabel('$m_{N}$ [GeV]',fontsize=15)
plt.tight_layout()
plt.savefig("sigma_mN.pdf")
plt.show()
#with open(outfile,'w') as ff:
#    for i in range(len(out['sig'])):
#        ff.write('{0} {1}\n'.format(out['sig'][i], out['mass'][i]))
