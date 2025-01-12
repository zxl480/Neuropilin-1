import matplotlib.pyplot as plt
import numpy as np
import pylab
import random

####################################################################################
fw = open ("select.txt","w")
repeat0,Time0,CV0A,CV0B,CV0G =[],[],[],[],[]
repeat1,Time1,CV1A,CV1B,CV1G =[],[],[],[],[]
repeat2,Time2,CV2A,CV2B,CV2G =[],[],[],[],[]

repeat=100        ##########import#########################################
f1=open('md0/CV/COLVAR_ALL')
r=-1;row=0
while True:    
      line=f1.readline()
      split=line.split()
      length=len(line.strip())
      row=row+1;
      if  length==0:
          break   
      elif  split[0]=="#!":
          r=r+1
      elif r%3==0 and row%12!=0: 
          Time0.append(float (split[0])); CV0A.append(float (split[1])); CV0B.append(float (split[2]));CV0G.append(float (split[3])); step=int(r/repeat+1);repeat0.append(step)
      elif r%3==1 and row%12!=0: 
          Time2.append(float (split[0])); CV2A.append(float (split[1])); CV2B.append(float (split[2]));CV2G.append(float (split[3])); step=int(r/repeat+1);repeat2.append(step)
      elif r%3==2 and row%12!=0: 
          Time1.append(float (split[0])); CV1A.append(float (split[1])); CV1B.append(float (split[2]));CV1G.append(float (split[3])); step=int(r/repeat+1);repeat1.append(step)

f2=open('md1/CV/COLVAR_ALL')
r=-1;row=0
while True:    
      line=f2.readline()
      split=line.split()
      length=len(line.strip())
      row=row+1;
      if  length==0:
          break   
      elif   split[0]=="#!":
          r=r+1
      elif r%3==0 and row%12!=0: 
          Time1.append(float (split[0])); CV1A.append(float (split[1])); CV1B.append(float (split[2]));CV1G.append(float (split[3]));step=int(r/repeat+1);repeat1.append(step)
      elif r%3==1 and row%12!=0: 
          Time0.append(float (split[0])); CV0A.append(float (split[1])); CV0B.append(float (split[2]));CV0G.append(float (split[3]));step=int(r/repeat+1);repeat0.append(step)
      elif r%3==2 and row%12!=0: 
          Time2.append(float (split[0])); CV2A.append(float (split[1])); CV2B.append(float (split[2]));CV2G.append(float (split[3]));step=int(r/repeat+1);repeat2.append(step)

f3=open('md2/CV/COLVAR_ALL')
r=-1;row=0
while True:    
      line=f3.readline()
      split=line.split()
      length=len(line.strip())
      row=row+1;
      if  length==0:
          break   
      elif   split[0]=="#!":
          r=r+1
      elif r%3==0 and row%12!=0: 
          Time2.append(float (split[0])); CV2A.append(float (split[1])); CV2B.append(float (split[2]));CV2G.append(float (split[3]));step=int(r/repeat+1);repeat2.append(step)
      elif r%3==1 and row%12!=0: 
          Time1.append(float (split[0])); CV1A.append(float (split[1])); CV1B.append(float (split[2]));CV1G.append(float (split[3]));step=int(r/repeat+1);repeat1.append(step)
      elif r%3==2 and row%12!=0: 
          Time0.append(float (split[0])); CV0A.append(float (split[1])); CV0B.append(float (split[2]));CV0G.append(float (split[3]));step=int(r/repeat+1);repeat0.append(step)

#print (Time0);print (CV0G);print(CV0B);print(CV0A)
N=len(Time0);#print (N)
AB= [1.0 for x in range (25)]
AG= [1.0 for x in range (25)]
BG= [1.0 for x in range (25)]

ret=random.randint(0,2)
#print (ret)
if (ret==0):
   index0,index1,index2=[],[],[]
   for i in range (5):
       mina=0.0+3.2*i
       maxa=0.0+3.2*(i+1)
       for j in range (5):
              minb=0.0+1.6*j
              maxb=0.0+1.6*(j+1)
              n=0
              for y in range (0,N) :
                 if (CV0A[y]>=mina and CV0A[y]<maxa and CV0B[y]>=minb and CV0B[y]<maxb):
                    n=n+1;
                 if (CV1A[y]>=mina and CV1A[y]<maxa and CV1B[y]>=minb and CV1B[y]<maxb):
                    n=n+1; 
                 if (CV2A[y]>=mina and CV2A[y]<maxa and CV2B[y]>=minb and CV2B[y]<maxb):
                    n=n+1;  
              if n!=0:
                 AB[5*i+j]=(n-1)*1.0/3/N;   
   ind=AB.index(min(AB)) ########################import##########################################
   nonone=AB.count(1.0);
   #print (AB); print(25-nonone);print(ind)
   w1,w2=int(ind/5),ind%5;  # print(w1,w2)  
   
   min1=0.0+3.2*w1;  max1=0.0+3.2*(w1+1); min2=0.0+1.6*w2; max2=0.0+1.6*(w2+1)        
   for y in range (0,N) :
       if (CV0A[y]>=min1 and CV0A[y]<max1 and CV0B[y]>=min2 and CV0B[y]<max2):
           index0.append(y);  
       if (CV1A[y]>=min1 and CV1A[y]<max1 and CV1B[y]>=min2 and CV1B[y]<max2):
           index1.append(y);  
       if (CV2A[y]>=min1 and CV2A[y]<max1 and CV2B[y]>=min2 and CV2B[y]<max2):
           index2.append(y);            
   total=index0+index1+index2
   traj=random.choice(total);
   frame=total.index(traj)
   if frame<len(index0): 
      print (2,repeat0[traj],Time0[traj]);fw.write(str(2)+' '+str(repeat0[traj])+' '+str(Time0[traj])+' '+str(nonone)+' '+str(ret))
   elif frame<(len(index0)+len(index1)): 
      print (0,repeat1[traj],Time1[traj]);fw.write(str(0)+' '+str(repeat1[traj])+' '+str(Time1[traj])+' '+str(nonone)+' '+str(ret))
   else:
      print (1,repeat2[traj],Time2[traj]);fw.write(str(1)+' '+str(repeat2[traj])+' '+str(Time2[traj])+' '+str(nonone)+' '+str(ret))


if (ret==1):
   index0,index1,index2=[],[],[]
   for i in range (5):
       mina=0.0+3.2*i
       maxa=0.0+3.2*(i+1)
       for j in range (5):
              minb=1.0+0.3*j
              maxb=1.0+0.3*(j+1)
              n=0
              for y in range (0,N) :
                 if (CV0A[y]>=mina and CV0A[y]<maxa and CV0G[y]>=minb and CV0G[y]<maxb):
                    n=n+1;
                 if (CV1A[y]>=mina and CV1A[y]<maxa and CV1G[y]>=minb and CV1G[y]<maxb):
                    n=n+1; 
                 if (CV2A[y]>=mina and CV2A[y]<maxa and CV2G[y]>=minb and CV2G[y]<maxb):
                    n=n+1; 
              if n!=0:
                 AG[5*i+j]=(n-1)*1.0/3/N; 
   ind=AG.index(min(AG)) ########################import##########################################
   nonone=AG.count(1.0);
  # print(AG);print(25-nonone);print(ind)
   w1,w2=int(ind/5),ind%5; # print(w1,w2)  
   min1=0.0+3.2*w1;  max1=0.0+3.2*(w1+1); min2=1.0+0.3*w2; max2=1.0+0.3*(w2+1)        
   for y in range (0,N) :
       if (CV0A[y]>=min1 and CV0A[y]<max1 and CV0G[y]>=min2 and CV0G[y]<max2):
           index0.append(y);  
       if (CV1A[y]>=min1 and CV1A[y]<max1 and CV1G[y]>=min2 and CV1G[y]<max2):
           index1.append(y);  
       if (CV2A[y]>=min1 and CV2A[y]<max1 and CV2G[y]>=min2 and CV2G[y]<max2):
           index2.append(y);            
   total=index0+index1+index2
   traj=random.choice(total);
   frame=total.index(traj)
   if frame<len(index0): 
      print (2,repeat0[traj],Time0[traj]);fw.write(str(2)+' '+str(repeat0[traj])+' '+str(Time0[traj])+' '+str(nonone)+' '+str(ret))
   elif frame<(len(index0)+len(index1)): 
      print (0,repeat1[traj],Time1[traj]);fw.write(str(0)+' '+str(repeat1[traj])+' '+str(Time1[traj])+' '+str(nonone)+' '+str(ret))
   else:
      print (1,repeat2[traj],Time2[traj]);fw.write(str(1)+' '+str(repeat2[traj])+' '+str(Time2[traj])+' '+str(nonone)+' '+str(ret))

if (ret==2):
   index0,index1,index2=[],[],[]
   for i in range (5):
       mina=0.0+1.6*i
       maxa=0.0+1.6*(i+1)
       for j in range (5):
              minb=1.0+0.3*j
              maxb=1.0+0.3*(j+1)
              n=0
              for y in range (0,N) :
                 if (CV0B[y]>=mina and CV0B[y]<maxa and CV0G[y]>=minb and CV0G[y]<maxb):
                    n=n+1;  
                 if (CV1B[y]>=mina and CV1B[y]<maxa and CV1G[y]>=minb and CV1G[y]<maxb):
                    n=n+1; 
                 if (CV2B[y]>=mina and CV2B[y]<maxa and CV2G[y]>=minb and CV2G[y]<maxb):
                    n=n+1;
              if n!=0:
                 BG[5*i+j]=(n-1)*1.0/3/N; 
   ind=BG.index(min(BG)) ########################import##########################################
   nonone=BG.count(1.0);
   #print(BG);print(25-nonone);print(ind)
   w1,w2=int(ind/5),ind%5; #print(w1,w2)
   min1=0.0+1.6*w1;  max1=0.0+1.6*(w1+1); min2=1.0+0.3*w2; max2=1.0+0.3*(w2+1)        
   for y in range (0,N) :
       if (CV0B[y]>=min1 and CV0B[y]<max1 and CV0G[y]>=min2 and CV0G[y]<max2):
           index0.append(y);  
       if (CV1B[y]>=min1 and CV1B[y]<max1 and CV1G[y]>=min2 and CV1G[y]<max2):
           index1.append(y);  
       if (CV2B[y]>=min1 and CV2B[y]<max1 and CV2G[y]>=min2 and CV2G[y]<max2):
           index2.append(y);         
  # print (index0);print(index1);print(index2)   
   total=index0+index1+index2
   traj=random.choice(total);
   frame=total.index(traj)
   if frame<len(index0): 
      print (2,repeat0[traj],Time0[traj]);fw.write(str(2)+' '+str(repeat0[traj])+' '+str(Time0[traj])+' '+str(nonone)+' '+str(ret))
   elif frame<(len(index0)+len(index1)): 
      print (0,repeat1[traj],Time1[traj]);fw.write(str(0)+' '+str(repeat1[traj])+' '+str(Time1[traj])+' '+str(nonone)+' '+str(ret))
   else:
      print (1,repeat2[traj],Time2[traj]);fw.write(str(1)+' '+str(repeat2[traj])+' '+str(Time2[traj])+' '+str(nonone)+' '+str(ret))
   
