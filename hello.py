#!/usr/bin/env python3
#import cpuinfo
import platform
#import pandas as pd
import numpy as np
import subprocess
#%%
'''
    Get architecture 
    --> CPU 
    --> GPU
    What can be build??
'''
#Get cpu information


#cpu_brand=cpu_info['arch']
cpu_processor = platform.processor()
print('Found '+str(cpu_processor+' as CPU'))


# #Get cpu information
# #Use Terminal to get GPU information
# output_gpu_terminal = subprocess.run(['lshw', '-C', 'display'], capture_output=True)
# #Seperate the output in lists and save in variable
# gpu_list=str(output_gpu_terminal.stdout).split('\\n')
# #store vender value of gpu_list in gpu_brand and remove first 15 charackter which
# #is '        vendor:'
# gpu_brand = gpu_list[3][15:]
#%%

gpu_hw_list=['NVIDIA','AMD','Asus','Intel','EVGA','Inno','Gigabyte','Zotac']
#os.system('date')

#Get installed display(s)
r = subprocess.run(['lshw', '-C', 'display'], capture_output=True)
#Store it in a list
f=str(r.stdout).split('\\n')

found = False            
for gpu in gpu_hw_list:
    
    vendor = [desc_item for desc_item in f if gpu in desc_item]
    if(len(vendor) == 0):
        print(f'Not found: {gpu}')
    else:
        print(f'Found: {gpu} as GPU')

#%%
#print('This system runs with '+ str(cpu_brand) + ' '+str(cpu_processor) +' processor and\nthe following GPU:' +str(gpu_list[3]))
#print('Here is the required HW information.\nPlease check string format for comperation\n ')
#print('\nCPU: '+str(cpu_processor)+'\nGPU: '+str(gpu_brand))

#--> Compare with existing CPU and GPU brand names?
#--> How to run my script on server?


#%%

'''
Mail from 09.03.2021
1001  . gpu/setup-madgraph.sh 
 1004  git clone https://github.com/madgraph5/madgraph4gpu.git
 1006  cd madgraph4gpu/
 1008  cd (poch2/cuda/ee_mumu)<--als Variablen /SubProcesses/P1_Sigma_sm_epem_mupmum/
 1011  make
 1013  ./gcheck.exe -p 1024 32 32
 1014  ./check.exe 1024 32 32


roiser@itscrd02:~$ cat gpu/setup-madgraph.sh 

—> von  hier
#/bin/bash

CUDAVERSION=11.1

export PATH=`echo $PATH | sed s/\\\\/cvmfs[a-zA-Z0-9./_-]\\\\+\://g`
export PATH=`echo $PATH | sed s/cuda-[0-9]*.[0-9]/cuda-${CUDAVERSION}/g`
cd /afs/cern.ch/work/a/areepsch/sw/madgraph4gpu

<— bis hier


file erzeugen
chmod u+x <file>


'''

'''
    Download Sourcode 
    Most likely from github
'''

'''
    check.exe for CPU
    gcheck.exe for GPU
'''

'''
    Get values to be evaluated
'''
#%%
