import cv2
import numpy as np

# Step 1: Load image
image_path = "test.jpg"   # Change image name
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Edge Detection
edges = cv2.Canny(gray, 100, 200)
edge_density = np.sum(edges > 0) / (gray.shape[0] * gray.shape[1])

# Step 4: Noise Estimation using Laplacian
laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

# Step 5: Histogram Analysis
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_smoothness = np.std(hist)

# Step 6: Decision Rule
print("Edge Density:", edge_density)
print("Noise Variance:", laplacian_var)
print("Histogram Std Dev:", hist_smoothness)

if edge_density > 0.05 and laplacian_var > 100:
    result = "Likely Real Image"
else:
    result = "Possibly AI Generated Image"

print("Final Result:", result)

# Step 7: Show Output
cv2.putText(img, result, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 255, 0), 2)

cv2.imshow("Image Classification", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
