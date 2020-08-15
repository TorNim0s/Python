import cv2

img = cv2.imread('test.jpeg', -1)

print (img)

resized = cv2.resize(img,(500,500))

cv2.imshow('image', resized)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()