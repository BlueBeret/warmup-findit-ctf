'''
This is for warm up. And i think it's "a fine cipher" for everyone.
'''

# Hint ada di "a fine cipher" maksudnya mungkin affine cipher,
# perlu 2 kunci, coba pake nomor soal yaitu 3 dan 1

def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y 
def modinv(a, m): 
  gcd, x, y = egcd(a, m) 
  if gcd != 1: 
    return None 
  else: 
    return x % m 

def decrypt(cipher, key): 
  for i in cipher:
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            print(chr((( modinv(key[0], 26)*(ord(i) - ord('A') - key[1])) % 26) + ord('A')), end="")
    elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            print(chr((( modinv(key[0], 26)*(ord(i) - ord('a') - key[1])) % 26) + ord('a')), end="")
    else:
            print(i, end="")

if __name__ == '__main__': 
  decrypt('QzokZGHGQ{unlbobdbo_kjij_eabv}', (3, 1))