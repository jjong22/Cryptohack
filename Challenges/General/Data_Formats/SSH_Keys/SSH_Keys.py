from cryptography.hazmat.primitives.serialization import load_ssh_public_key

with open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub", "rb") as f:
    e = load_ssh_public_key(f.read()).public_numbers()
    
print(e)