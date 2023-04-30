
import numpy as np


#Pendefinisian
def h_to_d(h,m,s):
    hourangle = h + m/60 + s/3600
    h_to_d = hourangle*15
    return h_to_d

def d_to_h(d,m,s):
    degree = d + m/60 + s/3600
    d_to_h = degree/15
    return d_to_h

def degree(d,m,s):
    degree = d + m/60 + s/3600
    return degree
    
# insiasi
L = 50000                                   # Dalam milimeter
print("Panjang Fokus Teleskop = ",L,"mm")
ra_o = h_to_d(20,2,0)
dec_o = degree(13,50,0)
print("Koordinat Pusat detektor (RA,DEC) = ",ra_o,",",dec_o)
ra_o1 = np.radians(ra_o)
dec_o1 = np.radians(dec_o)
x_ob = 0.95046
y_ob = 0.99977

# bintang referensi
ra_b = np.radians([h_to_d(20,2,49.691),h_to_d(20,3,58.936),h_to_d(20,0,44.093),
        h_to_d(20,2,45.502),h_to_d(20,2,27.265)])
dec_b = np.radians([degree(14,9,38.11),degree(13,39,13.67),degree(13,32,0.31),
         degree(13,37,15.97),degree(13,55,47)])
x_b = [0.91390,0.82013,1.09641,0.92378,0.94719]
y_b = [1.12604,0.94729,0.91136,0.93787,1.04628]

N = 5
A1 = []

for i in range (N):
    A = 1
    A1.append(float(A))

H = []
E = []
T = []
D1 = []
D2 = []

# 
for i,j in zip(ra_b,dec_b):
    k = i - ra_o1
    a = np.sin(j)*np.sin(dec_o1) + np.cos(j)*np.cos(dec_o1)*np.cos(k)
    b = np.cos(j)*np.sin(k)/a
    c = (np.sin(j)*np.cos(dec_o1) - np.cos(j)*np.sin(dec_o1)*np.cos(k))/a
    H.append(a)
    E.append(b)
    T.append(c)

# Mencari koefisien jika diketahui nilai E
for i,j in zip(E,x_b) :
    d1 = i - (j/L)
    D1.append(d1)
    
e1 = np.matrix([x_b[0:3],y_b[0:3],A1[0:3]])
F1 = e1.transpose()
f1 = np.linalg.inv(F1)
G = np.dot(f1,D1[0:3])
print('nilai P = ',G[0,0],'\n''nilai Q = ',G[0,1],'\n''nilai R = ',G[0,2])

# Mencari koefisien jika diketahui nilai T
for i,j in zip(T,y_b) :
    d2 = i - (j/L)
    D2.append(d2)

e2 = np.matrix([x_b[0:3],y_b[0:3],A1[0:3]])
F2 = e2.transpose()
f2 = np.linalg.inv(F2)
g = np.dot(f2,D2[0:3])
print('nilai S = ',g[0,0],'\n''nilai T = ',g[0,1],'\n''nilai U = ',g[0,2])

# Mencari nilai E object
E_ob = (x_ob/L) + G[0,0]*x_ob + G[0,1]*y_ob + G[0,2]

# Mencari nilai T object
T_ob = (y_ob/L) + g[0,0]*x_ob + g[0,1]*y_ob + g[0,2]

print('nilai si = ',E_ob,'\n''nilai eta = ',T_ob)

# Mencari koordinat object
delta = np.cos(dec_o1) - (T_ob*np.sin(dec_o1))
l_terbalik = np.sqrt(E_ob**2 + delta**2)
ra_ob = np.degrees(np.arctan(E_ob/delta) + ra_o1)
dec_ob1 = np.sin(dec_o1) + (T_ob*np.cos(dec_o1))
dec_ob = np.degrees(np.arctan(dec_ob1/l_terbalik))

print("Koordinat object (RA,DEC) = ",ra_ob,",",dec_ob)
