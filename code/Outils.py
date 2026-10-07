import pygame

def decoup_image(chemin_image_animation, witdh,height,nbrimage_x, nbrimage_y):
    witdh_img = witdh / nbrimage_x
    height_img = height / nbrimage_y
    images = pygame.image.load(chemin_image_animation)
    animation = []
    for nbimgy in range(nbrimage_y):
        for nbimgx in range (nbrimage_x):
            x = witdh_img * (nbimgx)
            y = height_img * (nbimgy)
            img = images.subsurface((x, y, witdh_img, height_img))
            animation.append(img)
    return animation