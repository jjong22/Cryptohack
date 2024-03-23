from cryptography import x509

with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb") as f:
    cert = x509.load_der_x509_certificate(f.read())

modulus = cert.public_key().public_numbers().n
public_exponent = cert.public_key().public_numbers().e

print(modulus)

# https://stackoverflow.com/questions/18806962/simple-der-cert-parsing-in-python

