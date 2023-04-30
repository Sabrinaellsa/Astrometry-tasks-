#2.3 Solve Kepler's equation 


import numpy as np
import math as mt

# diketahui 
v = np.array([-1.5, 1.0, -0.1])
r = np.array([10000, 40000, -5000])
Gmb = 398600.4

# Semi Mayor Axis 
def rbesar (rx, ry, rz):
    rbesar = np. sqrt (rx**2 + ry**2 + rz**2)
    return rbesar
def vbesar (vx, vy, vz) :
    vbesar = np.sqrt (vx**2 + vy**2 + vz**2)
    return vbesar

A1 = 2/rbesar (r[0], r[1], r[2])
A2 = (vbesar (v[0],v[1],v[2] )) **2/Gmb
A = (A1-A2)**(-1)

print ("Semi-mayoraxis = ", A)


#Eksentrisitas 
hx = r[1]*v[2] - r[2]*v[1]
hy = r[2]*v[0] - r[0]*v[2]
hz = r[0]*v[1] - r[1]*v[0]
h = np.array([hx,hy,hz])

def hbesar (hx,hy,hz) :
    hbesar = np.sqrt(hx**2 + hy**2 +hz**2)
    return hbesar

p = (hbesar (h[0],h[1],h[2]))**2/Gmb
e = np.sqrt (1-p/A)

print ("Eksesntristas =", e) 


#Inklinasi dan Omega
Wx =h[0]/hbesar (h[0], h[1], h[2])
Wy =h[1]/hbesar(h[0],h[1],h[2])
Wz =h[2]/hbesar (h[0],h[1], h[2])
i1 = np.sqrt (Wx**2 + Wy**2)/Wz
i = mt.degrees (np.arctan(i1))
omega1= Wx/(-Wy)
Omega = mt.degrees(np.arctan(omega1))

if (Omega< 0):
    Omega = Omega +180
print ("Inklinasi = ", i)
print (" Omega =" ,Omega)


#Mean Anomaly
n = np.sqrt(Gmb/A**3)
E1= np.dot(r,v)/((A**2)*n)
E2= 1-(rbesar (r[0], r[1], r[2])/A)
E = mt.degrees (np.arctan(E1/E2))
if (E<0):
    E=E+180
M = mt.degrees (mt.radians(E) - e*np.sin (mt.radians(E)))
print(" Mean Anomaly =", M)


#Argument Of Perigee
u1 = r[2]/np.sin (mt.radians(i))
u2 = r[0]*np.cos (mt.radians(Omega))
u3 = r[1]*np.sin (mt.radians (Omega))
u = mt.degrees (np.arctan (u1/(u2+u3)))

v1 = np.sqrt (1-(e**2)) *np.sin (mt.radians(E))
v2 = np.cos(mt.radians(E))-e
vr = mt.degrees(np.arctan(v1/v2))

W = u - vr
print ("Argument Of Perigee = ", W)


        
            
         
