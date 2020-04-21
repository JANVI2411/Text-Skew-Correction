import numpy as np
import cv2

image = cv2.imread("text3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

thresh = cv2.threshold(gray,0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow("thresh3", cv2.resize(thresh3,(500,500)))

# print("thresh",thresh)
coords = np.column_stack(np.where(thresh > 0))
print(" \n ---------------------:\n",coords)
angle = cv2.minAreaRect(coords)[-1]
#
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle


(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
img_rotated = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

cv2.putText(img_rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
# show the output image
print("[INFO] angle: {:.3f}".format(angle))
# cv2.imshow("thresh", cv2.resize(thresh1,(500,500)))
# cv2.imshow("gray", cv2.resize(gray,(500,500)))
cv2.imshow("Input", cv2.resize(image,(500,500)))
cv2.imshow("Rotated",cv2.resize(img_rotated,(500,500)))
cv2.waitKey(0)