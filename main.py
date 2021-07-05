from tinyec.ec import SubGroup, Curve
from Crypto.Random.random import randint
from web3 import Web3

p = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
n = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)

print(p)
print(n)

print("/////////////////////////////////////////////////////////////")

x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)

g = (x,y)

print(y**2 % p == (x**3 + 7) % p)

print("/////////////////////////////////////////////////////////////")

h = 1

field = SubGroup(p, g, n, h)
curve = Curve(a = 0, b = 7, field = field, name = 'secp256k1')

print(field)
print(curve)

print("/////////////////////PRIVATE KEY///////////////////////////////////////")

private_key = randint(1, n)

print(private_key)

print("//////////////////////////////PUBLIC KEY///////////////////////////////")

public_key = private_key * curve.g

print(public_key)

print("/////////////////////////////////////////////////////////////")

public_key_hex = Web3.toHex(public_key.x)[2:] + Web3.toHex(public_key.y)[2:]
