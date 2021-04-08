import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def lanesDetection(img):
    # img = cv.imread("./img/road.jpg")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    region_of_interest_vertices = [
        (0, 0), (height, 0),(width, 0), (width, height)
    ]
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    edge = cv.Canny(gray_img, 10, 10)
    cropped_image = region_of_interest(
        edge, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(edge, rho=2, theta=np.pi/180,
                           threshold=50, lines=np.array([]), minLineLength=10, maxLineGap=30)
    image_with_lines = draw_lines(img, lines)
    # plt.imshow(image_with_lines)
    # plt.show()
    return image_with_lines


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def videoLanes():
    cap = cv.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = lanesDetection(frame)
        cv.imshow('Lanes Detection', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    videoLanes()
"""
cap = cv.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = lanesDetection(frame)
    #cv.imshow('Lanes Detection', frame)
    gray = cv.cvtColor(frame,cv.COLOR_RGBA2GRAY)

    blur = cv.GaussianBlur(gray ,(5,5),0)
    canny = cv.Canny(blur,50,150)
    plt.imshow(canny)
    plt.show()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break"""