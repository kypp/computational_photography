import imageio
from scipy import ndimage
import numpy as np

from demosaicing_common import *

def demosaic_simple(img):     
    # compute local averages of pixel values
    averages = ImageAverages(img)

    # compute each channel based on channel masks
    red = (img * tile_up(img, Tile.red_tile)) +\
        (averages.horizontal * tile_up(img, Tile.red_horizontal_tile)) +\
        (averages.vertical * tile_up(img, Tile.red_vertical_tile)) +\
        (averages.cross * tile_up(img, Tile.red_cross_tile))

    green = (img * tile_up(img, Tile.green_tile)) +\
        (averages.four_way * tile_up(img, Tile.green_4way_tile))

    blue = (img * tile_up(img, Tile.blue_tile)) +\
        (averages.horizontal * tile_up(img, Tile.blue_horizontal_tile)) +\
        (averages.vertical * tile_up(img, Tile.blue_vertical_tile)) +\
        (averages.cross * tile_up(img, Tile.blue_cross_tile))
    return (red,green,blue)

def edge_based_demosaic(img):
    # compute local averages of pixel values
    averages = ImageAverages(img)

    # compute the horizontal and vertical gradient for the entire image
    h_gradient = convolve(img, [[1, 0, -1]])
    v_gradient = convolve(img, [[1], [0], [-1]])

    h_greater = h_gradient > v_gradient
    v_greater = v_gradient > h_gradient
    equal = h_gradient == v_gradient

    # compute green channel    
    green_mask = tile_up(img, Tile.green_tile)
    not_green_mask = np.logical_not(green_mask)
    
    green = img * green_mask +\
        averages.vertical * h_greater * not_green_mask +\
        averages.horizontal * v_greater * not_green_mask +\
        averages.four_way * equal * not_green_mask
    
    # compute red channel    
    red_mask = tile_up(img, Tile.red_tile)
    
    red_minus_green = red_mask*(img - green)
    red_averages = ImageAverages(red_minus_green)
        
    red = (red_minus_green) +\
            (red_averages.horizontal) +\
            (red_averages.vertical) +\
            (red_averages.cross)
    red += green
    red = np.clip(red, 0, 1)

    # compute blue channel    
    blue_mask = tile_up(img, Tile.blue_tile)
    
    blue_minus_green = blue_mask*(img - green)
    blue_averages = ImageAverages(blue_minus_green)
    
    blue = (blue_minus_green) +\
        (blue_averages.horizontal) +\
        (blue_averages.vertical) +\
        (blue_averages.cross)
    blue += green
    blue = np.clip(blue, 0, 1)
        
    return np.dstack((red,green,blue))