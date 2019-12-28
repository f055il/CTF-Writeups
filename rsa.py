#!/usr/bin/python

from Crypto.Util.number import inverse

#(n,e) correspond a la public key de chiffrement
#n = pq (aussi appele modulus)
n = 25693197123978473

#Exposant du chiffrement
e = 65537

#c correspond au message chiffre
c = 17608967038283735


#p et q sont les facteurs premiers de n

p = 150758089
q = 170426657

#print(p*q)

# phi correspond a la valeur de l'indicatrice d'Euler en n
phi = (p - 1) * (q - 1)

#d est la clef privee
d = inverse(e, phi)

texts=[]

enc_flag = ['0x2135d36aa0c278', '0x3e8f43212dafd7', '0x7a240c1672358', '0x37677cfb281b26', '0x26f90fe5a4bed0', '0xb0e1c482daf4', '0x59c069723a4e4b', '0x8cec977d4159']

for vals in enc_flag:
    val=vals[2:]
    decoded=int(val,16)
    texts.append(decoded)
    

# Pour dechiffrer, on utilise d (inverse de modulus phi) et le message est dechiffre
for ciphertext in texts:
    m = pow(ciphertext, d, n)

    print m

    #Puis on decode la valeur hexa en ascii
    print hex(m)[2:-1].decode('hex')
    print hex(m)

