import cv2

image = cv2.imread("../Images/WhatsApp Image 2025-12-31 at 9.43.16 PM.jpeg")

cv2.imshow("My Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
