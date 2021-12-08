with open('C:\\Users\\Пользователь\\Desktop\\lista.txt','r',encoding='utf-8') as f:
   l=list(f)
   f.close()
print('  Nume','Prenume','Nota','Grupa',sep='\t')
for i,linie  in enumerate(l):
    print(i+1,':\t',linie,end='')
n=media=0   
for linie in l:
    campuri=linie.split()
    nota=int(campuri[2])
    n+=1
    media+=nota
s1=s2=0
print(nota,sep='\t')
print('Media celor',n,'elevi este',media/float(n))
n1=n2=0
grupa1=[]
grupa2=[]
for linie in l:
    campuri=linie.split()
    if campuri[3]=="engl1":
        s1+=int(campuri[2])
        n1+=1
        grupa1.extend([linie])
    if campuri[3]=="engl2":
        n2+=1
        s2+=int(campuri[2])
        grupa2.extend([linie])
print('Media celor',n,'elevi din grupa 1 este',round(s1/n1,2))
print('Media celor',n,'elevi din grupa 2 este',round(s2/n2,2))
with open('C:\Users\Пользователь\Desktop\grupa1.txt',"w",) as f:
     for i in grupa1:
        f.write(i)
with open('C:\Users\Пользователь\Desktop\grupa2.txt','w') as f:
    for i in grupa2:    
        f.write(i)