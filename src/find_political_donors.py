# find_political_donors.py

# find_political_donors_final_v2.py

import numpy as np
import re

# wc -l itoth.txt # 85495

input=open('../input/itoth.txt','r')

NOL=8054  #  185495 
# NOL is varying input condition for quick test

SPLINPUT=[]  # splitted input

print "\n \n", " step 01: initial split of each data line entry into parts"

for i in range(0,NOL):
    entry=input.readline()
    #print entry
    splt=entry.split()
    splt01=str(splt)
    for j in range(0, np.size(splt01)):
        splt02=re.sub("[^\w]", " ", splt01).split() 
        SPLINPUT.append(splt02)
input.close()
print "\n size of SPLINPUT ", np.size(SPLINPUT) 


print "\n \n", " step 02: chosen data set contains MM/DD/YYYYY, dollar contribution, other ID "


# collect Transactions_DT, Transaction_AMT, Other_ID

INDEX=[] # index for other id empty 
DATE=[]
DOLLAR=[]
dollarIndex=[]
for i in range(0,np.size(SPLINPUT)):
    entry=SPLINPUT[i]
    for j in range(0,np.size(entry)):
        ese=entry[j]  # each split entry
        if ( len(str(ese))==8):
            ese1=ese[6]
            ese2=ese[7]
            esedt=[ese1,ese2]
            if ( esedt[0]=="1" and (esedt[1]=="7" or esedt[1]=="6") ): # confirms taht YYYY=2017 or 2016
                otherid=entry[j+2]
                if ( str(otherid[0]) != "C" and str(otherid[0]) != "H"  ):
                    INDEX.append(i) # collect date here
                    DATE.append(ese)
                    dollarIndex.append(j)
                    DOLLAR.append(entry[j+1])
                                                    
# check  DOLLAR                               
                                                                
print "\n \n", " INDEX here to choose the entry for which OTHER_ID is empty "

print "\n size of INDEX ", np.size(INDEX)  

 # raughly for ?? % data other ID is empty

print "\n size of DATE ", np.size(DATE)  #  49,533 for NOL=185495

print "\n size of DOLLAR ", np.size(DOLLAR) #  49,533 for NOL=185495
 

print "\n \n", " step 03: An additional input data states.txt is introduced to facilitate finding zip-code  "

USSTATES=[]
inputS=open('../input/states.txt','r')
for i in range(0,55):
    line1=inputS.readline()
    line=line1[1:3]
    USSTATES.append(line)
inputS.close()


ANCN=["0","1","2","3","4","5","6","7","8","9"]

ZIP=[]
ZIP_CODE=[]
INDEXVZIP=[]   # index for valid zip
ID=[]
for i in range(0,np.size(INDEX)):
    entry=SPLINPUT[INDEX[i]]  
    for j in range(0,np.size(entry)):
        if ( len(str(entry[j]))==2 ): # since states are like NY
            statez=entry[j]
            for k in range(0,np.size(USSTATES)):
                state=USSTATES[k]
                if ( statez[0]==state[0] and statez[1]==state[1] ):
                    zip1=entry[j+1]
                    zip0=zip1[0]
                    for ii in range(0,np.size(ANCN)):
                        if ( zip0==ANCN[ii] ):
                            ZIP_CODE.append(zip1[0:5]) # only valid zip be used for mediavals_by_zip.txt
                            INDEXVZIP.append(i)
                            idz=entry[0]
                            idz=idz[0:9]
                            ID.append(idz)
                    
                              

print "\n size of ZIP_CODE ", np.size(ZIP_CODE) #  49384 for NOL=
print "\n size of INDEXVZIP ", np.size(INDEXVZIP) #  49384 for NOL=185495
print "\n size of ID ", np.size(ID) #  49384 for NOL=185495


DATERBVZ=[]   # date refined by valid zip
DOLLARRBZ=[] # dollar refined by zip
DATERBZ=[] # date refined by valid zip

for i in range(0, np.size(INDEXVZIP) ):
    dollar=DOLLAR[i]
    DOLLARRBZ.append(dollar)
    date=DATE[i]
    DATERBZ.append(date)

print "\n size of DOLLARRBZ ", np.size(DOLLARRBZ) #  49,384 for NOL=185495
print "\n size of DATERBZ ", np.size(DATERBZ) #  49,384 for NOL=185495

print "\n \n", " step 04: finalize lists are ID, ZIP_CODE, DOLLARRBZ"


print "\n \n", " step 05: get the rolling sum of dollar contribution"
    
DOLLARRBZ=list(map(int, DOLLARRBZ))
DOLLARRBZnpna=np.array(DOLLARRBZ)

ZIP_CODEint = list(map(int, ZIP_CODE)) # type(ZIP_CODEint)=> list; type(ZIP_CODEint[3])=> int
ZIP_CODEnpna=np.array(ZIP_CODEint)  

print "\n \n", " step 06: finalize lists are ID, ZIP_CODEnpna, DOLLARRBZnpna"


ZIP_RS=[]  # zip for rolling sum
IDXZ_RS=[] # zip index for rolling sum
for i in range(0,10):
    itemcs=ZIP_CODEint[i]
    itemcsindex=np.where(ZIP_CODEnpna == itemcs)[0]
    ZIP_RS.append(itemcs)
    IDXZ_RS.append(itemcsindex)
    #print "itemcs", itemcs, ",","itemcsindex", itemcsindex
    

#print "\n size of ZIP_RS ", np.size(ZIP_RS)

#print "\n size of IDXZ_RS ", np.size(IDXZ_RS)

print "\n \n", " final step: write output file"

output=open('../output/medianvals_by_zip.txt','w')
for i in range(0,np.size(ZIP_RS)):
    zprs=ZIP_RS[i]  # zip rolling sum
    idxrs=IDXZ_RS[i]  # idx rolling sum
    dcCS=[] # dolalr contribution for cum sum
    IDfrs=[] # ids for rolling sum
    for j in range(0, np.size(idxrs)):
        drsz=DOLLARRBZ[idxrs[j]] # dollar rolling sum zip
        cidfcs=ID[idxrs[j]]  # corresponding id for rolling sum
        dcCS.append(drsz)
        IDfrs.append(cidfcs)
    dcCS=list(map(int, dcCS))
    dcCSnpna=np.array(dcCS)  # numpy nd array for dolalr contribution for cum sum
    RSDC=dcCSnpna[:-1].cumsum() # rolling sum for dollar contribution
    for k in range(0,np.size(RSDC)):
        dCS=RSDC[k]  # dollar rolling sum
        dFL=dcCS[k]  # dollar from List
        idwao=IDfrs[k] # id to write as output
        output.write('%s%s%s%s%s%s%s\n' % (idwao,"|",zprs,"|",dFL,"|",dCS) )

output.close()
