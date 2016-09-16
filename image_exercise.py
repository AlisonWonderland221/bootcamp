import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# For image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

def image_edits(image, threshold, cutoff, eccentricity):
    """ A function for processing images"""

    # Correct for 'hot' and bad pixels.
    selem = skimage.morphology.square(3)
    image_cfp_filter = skimage.filters.median(image, selem)

    # Correct for uneven illumination.
    image_gauss = skimage.filters.gaussian(image_cfp_filter, 50.0)
    image_float = skimage.img_as_float(image_cfp_filter)
    image_subt = image_float - image_gauss

    # Perform a threshold operation.
    image_thresh = skimage.filters.threshold_otsu(image_subt)
    image_otsu = image_subt < image_thresh

    # Quantifying segmented regions
    image_labeled, n_labels = skimage.measure.label(image_otsu, background=0, return_num=True)
    image_props = skimage.measure.regionprops(image_labeled)
    print(n_labels)

    #Removing objects with  pixel area below cutoff
    image_filt = image_labeled > 0
    #for prop in image_props:
    #    if prop.area < cutoff:
    #        image_filt[image_labeled==prop.label] = 0


    plt.imshow(image_labeled)
    plt.show()
    # Remove objects that are small or round
    for prop in image_props:
        if prop.area < cutoff or prop.eccentricity < eccentricity:
            image_filt[image_labeled==prop.label] = 0

    return image_filt
