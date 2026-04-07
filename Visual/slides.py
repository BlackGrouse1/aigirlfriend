import cv2

photo0 = "Pictures/ex1.jpeg"

def show_window():
    image = cv2.imread(photo0)
    cv2.imshow("my girly", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()