__author__ = 'teohoch'
import sys
import os
import numpy as np
import pyfits
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import cv
import cv2
from pylab import *

def cdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def dirs():
    d = ["clusters", "detections"]
    for di in d:
        cdir(di)


def access(filepath):
    try:
        f = open(filepath, "r")
    except IOError as e:
        return False
    return True




class analicis():

    def wavelet(self, image, kernel, J):
        ######################################################################################
        # wavelet(numpy array image, numpy array kernel, int J)-> list of numpy arrays with levels
        # computes the J levels of stationnary wavelet transform using "algorithme a trous"
        # Starck & Murtagh: Handbook of Astronomical Data Analysis, 2006.
        # Appendix A: A Trous Wavelet Transform
        ######################################################################################
        levels = []
        Ck = np.copy(image)

        for k in range(J):
            #print kernel
            kernel2D = np.zeros((len(kernel), len(kernel)))
            kernel1D = np.array(kernel, dtype=np.float64)
            for i in range(len(kernel2D)):
                for j in range(len(kernel2D[0])):
                    kernel2D[i][j] = kernel1D[i] * kernel1D[j]
            Ck1 = np.zeros(image.shape, image.dtype)

            #transform to cvMat
            kernel2D = cv.fromarray(kernel2D)
            Ck = cv.fromarray(Ck)
            Ck1 = cv.fromarray(Ck1)

            #covolve
            cv.Filter2D(Ck, Ck1, kernel2D)

            #back to numpy array
            Ck = np.asarray(Ck)
            Ck1 = np.asarray(Ck1)

            #append Level
            levels.append(Ck - Ck1)

            #update the kernel and Ck for next step:
            auxkernel = []
            for i in range(len(kernel) - 1):
                auxkernel.append(kernel[i])
                auxkernel.append(0.0)
            auxkernel.append(kernel[-1])
            kernel = auxkernel
            Ck = np.copy(Ck1)
        levels.append(Ck)
        return levels

    def kSigmaClipping(self, wi, k):
        #############################################################################
        # function kSigmaClipping(numpy array w1, int k)-> double sigma
        # calculates standard deviation for noise using k-sigma-clipping algortihm
        # Starck & Murtagh: Handbook of Astronomical Data Analysis, 2006.
        # 2.3.3 Automatic Estimation of Gaussian Noise
        #############################################################################
        sigma = np.std(wi)
        d = np.copy(wi)
        for i in range(3):
            d = d * (d < k * sigma)
            d = d * ( d > -k * sigma)
            sigma = np.std(d)
        return sigma

    def Clusterisar(self, filepath, filename, n_levels, k):
        print(filepath)
        if access(filepath):
            print "Calculando " + filepath
            sigma_e_j = np.array([0.889, 0.200, 0.086, 0.041, 0.020, 0.010, 0.005], dtype=np.float64)
            #Kernel B3-spline
            kernel1D = np.array([1. / 16., 1. / 4., 3. / 8., 1. / 4., 1. / 16.], dtype=np.float64)

            #0: abrir imput y obtener arreglo con datos de imagen:
            hdu = pyfits.open(filepath)
            data = asarray(hdu[0].data, dtype=np.float64)
            print hdu[0].header["CTYPE1"]
            hdu.close()

            #1: aplicar transformada de wavelets
            print "Calculando transformada de wavelets..."

            levels = self.wavelet(data, kernel1D, n_levels)

            #2,3: por cada nivel: calcular threshold y aplicarlo para guardar solo pixeles significativos por nivel
            print "Calculando threshold por nivel..."
            levels_s = []
            for level in levels[:-1]:
                sigma_j = self.kSigmaClipping(level, k)
                significants = level * (level >= k * sigma_j)
                #significants+=level*(level<=-k*sigma_j)
                levels_s.append(significants)
            #Previw Hasta Aqui!

            i = 0
            for im in levels_s:
                k = np.asarray(255. * (im != 0), dtype=np.uint8)
                cv2.imwrite("%d.png" % (i), k)

                i += 1

            print "Terminado " + filename

        else:
            print "El archivo {0} no existe".format(filename)

