import numpy as np

def gamma_correction(image, gamma=(1/2.2)):
    return image**gamma

def rgb_to_YCbCr(R, G, B):
    Y  =      (0.257 * R) + (0.504 * G) + (0.098 * B) + 1./16.
    Cr = V =  (0.439 * R) - (0.368 * G) - (0.071 * B) + .5
    Cb = U = -(0.148 * R) - (0.291 * G) + (0.439 * B) + .5
    return (Y,Cb,Cr)

def YCbCr_to_rgb(Y, CB, CR):
    B = 1.164 * (Y - 1./16.)                     + 2.018 * (CB - .5)
    G = 1.164 * (Y - 1./16.) - 0.813 * (CR - .5) - 0.391 * (CB - .5)
    R = 1.164 * (Y - 1./16.) + 1.596 * (CR - .5)    
    R = np.clip(R, 0, 1)
    G = np.clip(G, 0, 1)
    B = np.clip(B, 0, 1)
    return (R, G, B)

def filter_chrominance(r, g, b):
    y,cb,cr = rgb_to_YCbCr(r,g,b)
    cb = ndimage.filters.median_filter(cb, size=3)
    cr = ndimage.filters.median_filter(cr, size=3)
    return YCbCr_to_rgb(y,cb,cr)