import cv2
import numpy as np
import mtcnn

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def equalize_histogram(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    lab_planes = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))

    lab_planes[0] = clahe.apply(lab_planes[0])

    lab = cv2.merge(lab_planes)

    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


def preprocess_img(img, scope):
    img = transform_image(img)
    height, width, channels = img.shape
    if 'selfie' in scope:
        return img
    else:
        if height >= width:
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return img


def transform_image(image):
    img = np.fromstring(image, np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    return img

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)

    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


def verify_faces(img, scope):
    detector = mtcnn.MTCNN()
    if 'selfie' in scope:
        for i in range(4):
            faces = detector.detect_faces(img)
            if len(faces) >= 1:
                return len(faces), img
            else:
                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        for i in range(2):
            faces = detector.detect_faces(img)
            if len(faces) >= 1:
                return len(faces), img
            else:
                img = cv2.rotate(img, cv2.ROTATE_180)
    return False, False
