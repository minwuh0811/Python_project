# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import sqrt,cos,sin
def center_of_mass(lists):
        coms=[]
        for c in range(len(lists)):
            n=lists[c]
            com=[]
            for element in range(1,len(n[0])):
                a=0
                b=0
                for i in n:
                    if i[0][0]=='C':
                        a=a+12.0107*i[element]
                        b=b+12.0107
                    elif i[0][0]=='N':
                        a=a+14.0067*i[element]
                        b=b+14.0067
                    elif i[0][0]=='S':
                        a=a+32.065*i[element]
                        b=b+32.065
                    elif i[0][0]=='O':
                        a=a+15.9994*i[element]
                        b=b+15.9994
                    else:
                        print i[0][0]
                        print 'not match'
                com.append(a/b)           
            print' center of mass of monomer %d is x:%0.3f  y:%0.3f  z:%0.3f' %(c+1,com[0],com[1],com[2])
            coms.append(com)
        return coms
            
def fileload(filename):
    my_file=open(filename,'r+')
    files=my_file.readlines()
    my_file.close()
    number=len(files)    
    a=0
    numbers=[]
    for i in range(number):
        word=files[i].split()
        if word[0]=='TER':
            a=a+1
            numbers.append(a)
        else:
            a=a+1
    
    dimer=[]
    b=0
    for i in numbers:
        words=[]
        for j in range(b,i-1,2):
            word=files[j].split()
            words.append([word[2],eval(word[6]),eval(word[7]),eval(word[8])])
        dimer.append(words)
        b=i
    coms=center_of_mass(dimer)
    a=(coms[1][0]+coms[0][0])/2
    b=(coms[1][1]+coms[0][1])/2
    c=(coms[1][2]+coms[0][2])/2
    com=[a,b,c]
    print coms
    return coms
    
def traslate(filename,lists,filename1):
    my_file=open(filename,'r+')
    files=my_file.readlines()
    my_file.close()
    number=len(files)   
    new_file=open(filename1,'w')
    for i in range(number):
        words=files[i].split()
#        print files[i]
        if words[0]=='ATOM':
#            print words[6],words[7],words[8]
#            print lists
            words[6]=eval(words[6])-lists[0]
            words[7]=eval(words[7])-lists[1]
            words[8]=eval(words[8])-lists[2]
#            print words[6],words[7],words[8]
#            print words
            new_file.write('%-6s %4s  %-3s %s %s %3s %11.3f %7.3f %7.3f %5s    %-5s %11s\n' %(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11])) 
        else:
            new_file.write(files[i])

def rotate(filename,filename1,filename2,axies,number):
    lists=fileload(filename2)[number]
    my_file=open(filename,'r+')
    files=my_file.readlines()
    my_file.close()
    number=len(files)   
#    print R
    new_file=open(filename1,'w')
    for i in range(number):
        words=files[i].split()
        if words[0]=='ATOM':
            if axies=='z':
                R=sqrt(lists[1]**2+lists[0]**2)
                a=eval(words[6])*lists[0]/R+eval(words[7])*lists[1]/R
                b=eval(words[6])*lists[1]/R-eval(words[7])*lists[0]/R
                c=eval(words[8])
                words[6]=a
                words[7]=b
                words[8]=c
                new_file.write('%-6s %4s  %-3s %s %s %3s %11.3f %7.3f %7.3f %5s    %-5s %11s\n' %(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]))
            elif axies=='y':
                R=sqrt(lists[0]**2+lists[2]**2)
                a=eval(words[6])*lists[0]/R+eval(words[8])*lists[2]/R
                b=eval(words[7])
                c=eval(words[6])*lists[2]/R-eval(words[8])*lists[0]/R
                words[6]=a
                words[7]=b
                words[8]=c
                new_file.write('%-6s %4s  %-3s %s %s %3s %11.3f %7.3f %7.3f %5s    %-5s %11s\n' %(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11])) 
            elif axies == 'x':
                R=sqrt(lists[1]**2+lists[2]**2)
                a=eval(words[6])
                b=eval(words[7])*lists[1]/R+eval(words[8])*lists[2]/R
                c=eval(words[7])*lists[2]/R-eval(words[8])*lists[1]/R
                words[6]=a
                words[7]=b
                words[8]=c
                new_file.write('%-6s %4s  %-3s %s %s %3s %11.3f %7.3f %7.3f %5s    %-5s %11s\n' %(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11])) 
        else:
            print 'no ATOM'
            new_file.write(files[i])
def dimer_rotate(filename,filename1,filename2,times):
    my_file=open(filename,'r+')
    files=my_file.readlines()
    my_file.close()
    number=len(files) 
    dimer=[]
    Monomer=[]
    new_file=open(filename1,'w')
    R=fileload(filename2)[0][0]
    for i in range(number):
        words=files[i].split()
        if words[0]=='TER':
            Monomer.append(files[i])
            dimer.append(Monomer)
            Monomer=[]
        else:
            Monomer.append(files[i])
    
    for i in range(1,times+1):
        degree=360.0*i/times
        print degree
        new_file.write('rotate degree %0.2f\n' %(degree))
        for monomer in range(len(dimer[0])):
            words=dimer[0][monomer].split()
            if words[0]=='ATOM':
                a=eval(words[6])*cos(degree)+eval(words[8])*sin(degree)
                b=eval(words[7])
                c=-eval(words[6])*sin(degree)+eval(words[8])*cos(degree)
                words[6]=a
                words[7]=b
                words[8]=c
                new_file.write('%-6s %4s  %-3s %s %s %3s %11.3f %7.3f %7.3f %5s    %-5s %11s\n' %(words[0],words[1],words[2],words[3],words[4],words[5],words[6],words[7],words[8],words[9],words[10],words[11]))
            else:
                new_file.write(dimer[0][monomer])
        for monomer in dimer[1]:
            new_file.write(monomer)
        new_file.write('END\n')
        new_file.write('\n')
    new_file.close()
        

#fileload('4dnw.pdb')

#traslate('4dnw.pdb',[14.587, -12.116, 26.190],'4dnw_test.pdb')
#traslate('4dnw_reference.pdb',[14.587, -12.116, 26.190],'4dnw_reference_test.pdb')
#traslate('4dnw_reference_2.pdb',[14.587, -12.116, 26.190],'4dnw_reference_2_t.pdb')
#fileload('4dnw_test.pdb') 
#fileload('4dnw_reference_test.pdb')      
#fileload('4dnw_reference_2_t.pdb')  
#rotate('4dnw_test.pdb','4dnw_test_rotate.pdb','4dnw_reference_test.pdb','z',0)
#rotate('4dnw_reference_test.pdb','4dnw_reference_test_rotate.pdb','4dnw_reference_test.pdb','z',0)
#rotate('4dnw_reference_2_t.pdb','4dnw_reference_2_t_rotate.pdb','4dnw_reference_test.pdb','z',0)   
#fileload('4dnw_test_rotate.pdb')  
#fileload('4dnw_reference_test_rotate.pdb') 
#fileload('4dnw_reference_2_t_rotate.pdb')       
#rotate('4dnw_reference_test_rotate.pdb','4dnw_reference_test_rotate_y.pdb','4dnw_reference_test_rotate.pdb','y',0) 
#rotate('4dnw_test_rotate.pdb','4dnw_test_rotate_y.pdb','4dnw_reference_test_rotate.pdb','y',0)
#rotate('4dnw_reference_2_t_rotate.pdb','4dnw_reference_2_t_rotate_y.pdb','4dnw_reference_test_rotate.pdb','y',0)
#fileload('4dnw_test_rotate_y.pdb')  
#fileload('4dnw_reference_test_rotate_y.pdb')  
#fileload('4dnw_reference_2_t_rotate_y.pdb') 
###traslate('4dnw_test_rotate_y.pdb',[4.425/2, 0, 4.091/2],'4dnw_test_t.pdb')
###traslate('4dnw_reference_test_rotate_y.pdb',[4.425/2, 0, 4.091/2],'4dnw_reference_test_t.pdb')
###traslate('4dnw_reference_2_t_rotate_y.pdb',[4.425/2, 0, 4.091/2],'4dnw_reference_2_t_t.pdb')
###fileload('4dnw_test_t.pdb') 
###fileload('4dnw_reference_test_t.pdb')      
###fileload('4dnw_reference_2_t_t.pdb')
#rotate('4dnw_test_rotate_y.pdb','4dnw_test_rotate_x.pdb','4dnw_reference_2_t_rotate_y.pdb','x',1)
#rotate('4dnw_reference_test_rotate_y.pdb','4dnw_reference_test_rotate_x.pdb','4dnw_reference_2_t_rotate_y.pdb','x',1)
#rotate('4dnw_reference_2_t_rotate_y.pdb','4dnw_reference_2_t_rotate_x.pdb','4dnw_reference_2_t_rotate_y.pdb','x',1) 
#fileload('4dnw_test_rotate_x.pdb')  
#fileload('4dnw_reference_test_rotate_x.pdb')  
#fileload('4dnw_reference_2_t_rotate_x.pdb') 
#fileload('4dnw_reference_test_rotate_x.pdb')  
#fileload('4dnw_test_rotate_x.pdb')  
dimer_rotate('4dnw_test_rotate_x.pdb','4dnw_test_rotate_360.pdb','4dnw_reference_test_rotate_x.pdb',10)

