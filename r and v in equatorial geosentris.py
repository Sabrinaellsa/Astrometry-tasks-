import numpy as np
print('='*100)

GMB = 398600.4405 #GMB
r=6378

semimayor = float(input("Masukkan nilai semimayor: ", ))

eksentrisitas = float(input("Masukkan nilai eksentrisitas: ", ))

inc = float(input("Masukkan nilai inklinasi: ", ))
i = inc/180*np.pi  #inklinasi

omg = float(input("Masukkan nilai RAAN: "))
RAAN = omg/180*np.pi  #RAAN

arg_peri = float(input("Masukkan nilai w: "))
w= arg_peri/180*np.pi #argument of perigee

te = float(input("Masukkan nilai v: "))
v= te/180*np.pi#true anomaly

RE = 637 #Jari-jari Bumi(km)

#a=16725
#e= 1.4
#inc= 30
#omega= 40
#w= 60
#v = 30
#mencari nilai u
u=v+w
print(u)
print("="*100)

#mencari semi0-lactus-rectum
p=semimayor*(eksentrisitas**2-1)
print(p)
print("="*100)

#mencari h
h=np.sqrt(p*GMB)
print(h)
print("="*100)

#mencari [r]_xbar
r1_xbar=p*(1/(eksentrisitas*(np.cos(v)+1)))
print(r1_xbar)
print("="*100)
r2_xbar=([np.cos(v)],[np.sin(v)],[0])
r_xbar=np.dot(r1_xbar,r2_xbar)
print(r_xbar)
print("="*100)
            
#mencari [v]_xbar
v_xbar=GMB/h
v1_xbar=([-np.sin(v)],
         [eksentrisitas+np.cos(v)],
         [0])
v_xbar=np.dot(v_xbar,v1_xbar)
print(v_xbar)
print("="*100)

#mencari [Q]xxbar
Q_xxbar1=([np.cos(w),np.sin(w),0],
         [-np.sin(w),np.cos(w),0],
         [0,0,1])
I=([1,0,0],
   [0,np.cos(i),np.sin(i)],
   [0,-np.sin(i),np.cos(i)])
I2=([np.cos(RAAN),np.sin(RAAN),0],
    [-np.sin(RAAN),np.cos(RAAN),0],
    [0,0,1])
Q_xxbar2=np.dot(Q_xxbar1,I)
Q_xxbar=np.dot(Q_xxbar2,I2)
print(Q_xxbar)

Q_xxbar=Q_xxbar.transpose()
print(Q_xxbar)
print("="*100)
r=np.dot(Q_xxbar,r_xbar)
V=np.dot(Q_xxbar,v_xbar)

print("vektor posisi dalam xyz:",r)
print("vektor kecepatan dalam xyz",V)

print ()

print (" Nama : Sabrina Ellsa Mastura")
print (" Nim : 118290070 ")
print (" Matakuliah : linsat " )
print (" nomor 3")
