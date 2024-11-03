import cv2
import numpy as np

image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Edge detection
canny_edges = cv2.Canny(image, 100, 200)
cv2.imwrite('canny_edges.jpg', canny_edges)

sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_combined = cv2.bitwise_or(np.uint8(np.absolute(sobelx)), np.uint8(np.absolute(sobely)))
cv2.imwrite('sobel_combined.jpg', sobel_combined)

laplacian_edges = cv2.Laplacian(image, cv2.CV_64F)
cv2.imwrite('laplacian_edges.jpg', np.uint8(np.absolute(laplacian_edges)))

print("Edge detection images saved!")

# Segmentation
image = cv2.imread('input_image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold_segmentation.jpg', thresh)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
dist_transform = cv2.distanceTransform(binary, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(cv2.convertScaleAbs(255 - binary), sure_fg)
markers = cv2.connectedComponents(sure_fg)[1] + 1
markers[unknown == 255] = 0
watershed_result = cv2.watershed(image, markers)
image[watershed_result == -1] = [255, 0, 0]
cv2.imwrite('watershed_segmentation.jpg', image)

mask = np.zeros(image.shape[:2], np.uint8)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 50, image.shape[1]-50, image.shape[0]-50)
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
grabcut_result = image * mask2[:, :, np.newaxis]
cv2.imwrite('grabcut_segmentation.jpg', grabcut_result)

print("Segmentation images saved!")

# Object detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imwrite('haar_face_detection.jpg', image)

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
layer_names = net.getLayerNames()
unconnected_layers = net.getUnconnectedOutLayers()
if isinstance(unconnected_layers[0], list) or isinstance(unconnected_layers[0], np.ndarray):
    output_layers = [layer_names[i[0] - 1] for i in unconnected_layers]
else:
    output_layers = [layer_names[i - 1] for i in unconnected_layers]

image = cv2.imread('input_image.jpg')
height, width = image.shape[:2]
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imwrite('yolo_object_detection.jpg', image)

image = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imwrite('contour_object_detection.jpg', image)

print("Object detection images saved!")
