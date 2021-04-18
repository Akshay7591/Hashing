import hashlib
x=str(input("Enter String to Encrypt:"))
print("Encrypted String is:")
print(hashlib.sha1(x.encode()).hexdigest())
