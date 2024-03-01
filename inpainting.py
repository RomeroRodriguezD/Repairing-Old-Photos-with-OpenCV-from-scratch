import cv2

# Load original and mask images

original = cv2.imread('base.jpg')
mask = cv2.imread('mask.png',0)

# Apply Telea inpainting algorithm with a 3x3 kernel

repaired_image = cv2.inpaint(original, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Show original image and repaired one

cv2.imshow('Original image', original)
cv2.imshow('Repaired image', repaired_image)

# Save the brand new image

cv2.imwrite('repaired.png', repaired_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
