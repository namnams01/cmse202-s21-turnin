from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self, im1_filename, im2_filename):
        
        first = fits.getdata(im1_filename)
        second = fits.getdata(im2_filename)
        self.im1_data = first
        self.im2_data = second
        return 
        '''
        This function is incomplete! It is missing the appropriate input vales
        and the "pass" should be replaced with the appropriate code.
        Update this docstring to explain what the function does (or should do).
        '''
        #loads the data into the object (self)
    def calc_stats(self):
        
        print('File name:',self.im1_filename,'with mean: ', np.mean(self.im1_data), 'with standard deviation: ',np.std(self.im1_data))
        print()
        print('File name:',self.im2_filename,'with mean: ', np.mean(self.im2_data), 'with standard deviation: ',np.std(self.im2_data))
        
    
    def make_composite(self):
        #This function is incomplete! Make sure to finish it and
        #then update this docstring to explain what the function does!
    # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
    
    # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
    
    # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = (self.im2_data.astype("float")/norm_factor) * 1.5
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0

        rgb[:,:,1] = ((self.im2_data.astype("float")+self.im1_data.astype('float'))/(2*norm_factor))
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
    
        rgb[:,:,2] = (self.im1_data.astype('float'))/(norm_factor)
        rgb[:,:,2][rgb[:,:,2]>1.0] = 1.0
    
        final_image_array = [rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]]
    
        plt.imshow(rgb,origin='lower')
        np.transpose(rgb)