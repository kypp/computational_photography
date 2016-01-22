import numpy as np
from scipy import ndimage

class Tile:
    red_tile = np.array([[True, False],[False,False]])
    red_vertical_tile = np.array([[False, False],[True,False]])
    red_horizontal_tile = np.array([[False,True],[False,False]])
    red_cross_tile = np.array([[False,False],[False,True]])

    green_tile = np.array([[False,True],[True,False]])
    green_4way_tile = np.logical_not(green_tile)

    blue_tile = red_cross_tile
    blue_vertical_tile = red_horizontal_tile
    blue_horizontal_tile = red_vertical_tile
    blue_cross_tile = red_tile

def tile_up(image, tile):      
    tiled = np.tile(tile, ((image.shape[0]+image.shape[0]%2)/2, (image.shape[1]+image.shape[1]%2)/2))    
    if image.shape[0]%2==1:
        tiled = np.delete(tiled, -1, 0)
    if image.shape[1]%2==1:
        tiled = np.delete(tiled, -1, 1)
    return tiled

def convolve(array, kernel):
    return ndimage.convolve(array, np.array(kernel), mode='constant', cval=0.0)
    
class ImageAverages:
    def __init__(self, image):
        self.horizontal = convolve(image, [[.5,0,.5]])
        self.vertical = convolve(image, [[.5],[0],[.5]])
        self.four_way = convolve(image, [[0,.25,0],[.25,0,.25],[0,.25,0]])
        self.cross = convolve(image, [[.25,0,.25],[0,0,0],[.25,0,.25]])