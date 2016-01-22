import demosaicing
import image_processing

import imageio
import numpy as np

def demosaic_simple(input, output):
	img=imageio.imread(input)
	demosaiced = demosaicing.demosaic_simple(img)
	stacked = np.dstack(demosaiced)
	imageio.imwrite(output, stacked)

def demosaic_edge_based(input, output):
	img=imageio.imread(input)
	demosaiced = demosaicing.edge_based_demosaic(img)
	imageio.imwrite(output, demosaiced)

def gamma_correct(input, output):
	img=imageio.imread(input)
	corrected = image_processing.gamma_correction(img)
	imageio.imwrite(output, corrected)

def demosaic_filter_correct(input, output):
	img=imageio.imread(input)
	filtered_image = image_processing.filter_chrominance(*demosaicing.demosaic_simple(img))
	filtered_stacked = image_processing.gamma_correction(np.dstack(filtered_image))
	imageio.imwrite(output, filtered_stacked)
