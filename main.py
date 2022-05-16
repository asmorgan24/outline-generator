import sys, os
import IPython, random
import cv2
import numpy as np
from PIL import Image
from os import walk
import yaml


def create_img(params, image_save_location):
    image = cv2.imread(params['proj_path']+'/imgs/'+params['input_image'])

    # Find Canny edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.blur(gray, (3,3))
    edged = cv2.Canny(img_blur, 60, 200)

    #find contours
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # IPython.embed()
    image_list = []
    save_interval = int(len(contours)/params['num_intervals'])

    random_idx = list(range(len(contours)))
    if params['randomize_contours']:
        random.shuffle(random_idx)

    contour_image = np.ones_like(image)
    for idx in range(len(random_idx)):
        cnt = contours[random_idx[idx]]
        c1, c2, c3 = np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)
        cv2.drawContours(contour_image, cnt, -1, (c1,c2,c3), 3)
        if idx % save_interval ==0:
            image_list.append(Image.fromarray(contour_image.copy()))

    #Save the last one a couple more times
    for _ in range(12):
        image_list.append(Image.fromarray(contour_image.copy()))

    if params['save_as_gif']:
        image_list[0].save(image_save_location+'.gif',
               save_all=True, append_images=image_list[1:], optimize=False, duration=params['interval_duration'], loop=1)
    else:
        image_list[-1].save(image_save_location+'.jpeg')

    image_list[-1].show()


def main():
    #Load params to for the image creator
    with open('params.yaml') as f:
        params = yaml.load(f, Loader=yaml.FullLoader)

    #Set project path directory
    params['proj_path'] = os.getcwd() if params['proj_path'] == 'None' else params['proj_path']

    # Name of the savable image, without the filetype
    image_save_location = params['proj_path']+'/out/'+params['saved_filename']

    create_img(params, image_save_location)

    print ('Alles fertig! All done!')
    IPython.embed()

if __name__ == '__main__':
    main()
