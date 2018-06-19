import cv2
import numpy as np
from matplotlib import pyplot as plt


z = input()

# read image
img = cv2.imread('willsmith_bike.jpg', 0)
cv2.imshow('will', img)


if int(z) == 0:
    print("Selected zero.")
    # default is cv2,WINDOW_AUTOSIZE which cannot be adjusted
    # .WINDOW_NORMAL => can resize
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # show (filename, source)
    cv2.imshow('willsmith', img)
    # wait for input
    cv2.waitKey(0)
    #close
    cv2.destroyAllWindows()

    b = "Hello World"

    print(b)

elif int(z) == 1:
    print("Selected one.")
    print("esc) exit\ns) save and exit")

    cv2.imshow('before', img)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        # new (filename, source)
        cv2.imwrite('new_willsmith.png', img)
        cv2.destroyAllWindows()

elif int(z) == 2:
    print("Selected two.")

    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    # hide tick values X and Y
    plt.xticks([]), plt.yticks([])
    plt.show()

elif int(z) == 3:
    img_bgr = cv2.imread('/Users/redryerye/python/opencv-python-tutorial/willsmith_bike.jpg')
    # im_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
    # Image.fromarray(img_rgb).save('/Users/redryerye/python/opencv-python-tutorial/will_rgb.jpg')

    img_rgb = img_bgr[:,:,::-1]

    cv2.imwrite('rgb.png', img_rgb)
    # im_bgr = cv2.imread('willsmith_bike.jpg')
    # im_rgb = im_bgr[:, :, [2, 1, 0]]
    # Image.fromarray(im_rgb).save('will_swap.jpg')
    #
    # im_rgb = im_bgr[:, :, ::-1]
    # Image.fromarray(im_rgb).save('will_swap2.jpg')


    # bgr = cv2.split(img)
    # img2 = img[..., ::-1]
    # plt.subplot(121);plt.imshow(img)
    # plt.subplot(122);plt.imshow(img2)
    # plt.show()

    # cv2.imshow('bgr image', img)
    # cv2.imshow('rgb image', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
