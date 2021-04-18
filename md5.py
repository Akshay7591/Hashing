import hashlib
x=str(input("Enter String to Encrypt:"))
print("Encrypted String is:")
print(hashlib.md5(x.encode()).hexdigest())
