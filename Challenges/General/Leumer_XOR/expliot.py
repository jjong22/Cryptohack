import cv2

flag = './flag.png'
img1 = cv2.imread(flag, 0)
height, width = img1.shape

lemur = './lemur.png'
img2 = cv2.imread(lemur, 0)

bit_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow('sample',bit_xor)
cv2.waitKey()
cv2.destroyAllWindows()

# python3 expliot.py
# >> crypto{X0Rly_n0t!}