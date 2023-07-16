import os
import shutil
import math


with open('OUTPUT.cfg') as f:
    lines = f.readlines()
    cfgcnt = 0
    for line in lines:
        if line == ' Size\n':
            cfgcnt += 1

    cntr=1
    for i in range(len(lines)):
        if lines[i] != 'BEGIN_CFG\n':
            continue
#        else:
#            print("reading cfg#"+str(cntr+1))
        size = int(lines[i+2].split()[0])
    
        nruter = []
        for j in range(size):
            tmp = []
            words = lines[i+8+j].split()
            tmp.append(float(words[5]))
            tmp.append(float(words[6]))
            tmp.append(float(words[7]))
            nruter.append(tmp)

        base = math.ceil(math.log10(cfgcnt))
        dirname = ('job-{:0'+str(base)+'d}').format(cntr)
        os.system('mkdir '+dirname)
        with open(dirname+'/vasprun.xml','w') as ff:
            ff.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
            ff.write('<modeling>\n')
            ff.write(' <calculation>\n')
            ff.write('  <varray name="forces" >\n')
            for k in range (size):
                ff.write('  <v>  {: 12.6f} {: 12.6f} {: 12.6f} </v>\n'.format(nruter[k][0], nruter[k][1], nruter[k][2]))
            ff.write('  </varray>\n')
            ff.write(' </calculation>\n')
            ff.write('</modeling>\n')
 
        print(cntr)
        cntr += 1