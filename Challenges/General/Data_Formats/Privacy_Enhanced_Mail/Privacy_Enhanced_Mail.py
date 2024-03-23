from Crypto.PublicKey import RSA

dec = RSA.importKey(open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'rb').read(), 'password')

print(dec.d)


# .pem 파일 읽어오기!
# '.d', '.n', '.e'를 붙여 사용하면 RSA에 사용된 구성요소를 볼 수 있다!