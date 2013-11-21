import sys
import os
import numpy as np
import pyfits
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#import pywt
import cv
import cv2
from pylab import*

def cdir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
    
def dirs():
	d = ["clusters","detections"]
	for di in d:
		cdir (di)
		
def access(filepath):
    try:
        f = open(filepath, "r")
    except IOError as e:
        return False
 
    return True

######################################################################################
# wavelet(numpy array image, numpy array kernel, int J)-> list of numpy arrays with levels 
# computes the J levels of stationnary wavelet transform using "algorithme a trous"
# Starck & Murtagh: Handbook of Astronomical Data Analysis, 2006. 
# Appendix A: A Trous Wavelet Transform
######################################################################################
def wavelet(image,kernel, J):
	levels=[]
	Ck=np.copy(image)

	for k in range(J):
		#print kernel
		kernel2D=np.zeros((len(kernel),len(kernel)))
		kernel1D=np.array(kernel,dtype=np.float64)
		for i in range(len(kernel2D)):
			for j in range(len(kernel2D[0])):
				kernel2D[i][j]=kernel1D[i]*kernel1D[j]
		Ck1=np.zeros(image.shape,image.dtype)

		#transform to cvMat
		kernel2D=cv.fromarray(kernel2D)
		Ck = cv.fromarray(Ck)
		Ck1 = cv.fromarray(Ck1)

		#covolve
		cv.Filter2D(Ck,Ck1,kernel2D)

		#back to numpy array
		Ck=np.asarray(Ck)
		Ck1=np.asarray(Ck1)

		#append Level
		levels.append(Ck-Ck1)

		#update the kernel and Ck for next step:
		auxkernel=[]
		for i in range(len(kernel)-1):
			auxkernel.append(kernel[i])
			auxkernel.append(0.0)
		auxkernel.append(kernel[-1])
		kernel=auxkernel
		Ck=np.copy(Ck1)
	levels.append(Ck)
	return levels

#############################################################################
# function kSigmaClipping(numpy array w1, int k)-> double sigma
# calculates standard deviation for noise using k-sigma-clipping algortihm
# Starck & Murtagh: Handbook of Astronomical Data Analysis, 2006.
# 2.3.3 Automatic Estimation of Gaussian Noise
#############################################################################
def kSigmaClipping(wi,k):
	sigma=np.std(wi)
	d=np.copy(wi)
	for i in range(3):
		d=d*(d<k*sigma)
		d=d*( d>-k*sigma)
		sigma=np.std(d)
	return sigma

########################################
dirs()
if len(sys.argv) > 1:
	for grp in sys.argv[1:]:
		if access('dataset/%s' %grp):
			print "Calculando "+grp
			sigma_e_j=np.array([0.889, 0.200, 0.086, 0.041, 0.020, 0.010, 0.005],dtype=np.float64)
			n_levels=8
			k=3
			#Kernel B3-spline
			kernel1D = np.array([1./16.,1./4.,3./8.,1./4.,1./16.],dtype=np.float64) 

			#0: abrir imput y obtener arreglo con datos de imagen:
			hdu=pyfits.open('dataset/%s' %grp)
			data= asarray(hdu[0].data,dtype=np.float64)
			print hdu[0].header["CTYPE1"]
			hdu.close()

			#1: aplicar transformada de wavelets
			print "Calculando transformada de wavelets..."
			levels=wavelet(data,kernel1D,n_levels)

			#2,3: por cada nivel: calcular threshold y aplicarlo para guardar solo pixeles significativos por nivel
			print "Calculando threshold por nivel..."
			levels_s=[]
			for level in levels[:-1]:
				sigma_j= kSigmaClipping(level,k)
				significants=level*(level>=k*sigma_j)
				#significants+=level*(level<=-k*sigma_j)
				levels_s.append(significants)

			#4: Agrupar niveles segun estructuras:
			print "Agrupando estructuras..."
			estrellas=levels_s[1]+levels_s[2]
			estrellas=np.asarray(255.*(estrellas!=0),dtype=np.uint8)

			nucleos=levels_s[3]+levels_s[4]
			nucleos=np.asarray(255.*(nucleos!=0),dtype=np.uint8)

			nubes=levels_s[5]+levels_s[6]+levels_s[7]
			nubes=np.asarray(255.*(nubes!=0),dtype=np.uint8)

			#5: mostrar contornos

			estrella_contours,eh=cv2.findContours(estrellas, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
			estrella_contours=np.asarray(estrella_contours)

			nucleo_contours,nh=cv2.findContours(nucleos, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
			nucleo_contours=np.asarray(nucleo_contours)

			nube_contours,nnh=cv2.findContours(nubes, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
			nube_contours=np.asarray(nube_contours)

			#escalar rango (solo para que se visualice el resultado)
			s= kSigmaClipping(data,k)
			data=data*(data>=k*s)
			data-=k*s

			#mostrar estructuras
			print "Guardando deteccion de objetos en carpeta detections/ ..."
			image1=np.asarray(cv2.cvtColor(np.asarray(data,dtype=np.float32), cv.CV_GRAY2RGB))
			image=np.asarray(cv2.cvtColor(np.asarray(data,dtype=np.float32), cv.CV_GRAY2RGB))

			rango=500000./image.max()
			image*=rango
			image1*=rango

			red=(0,0,255)
			green=(0,255,0)
			blue=(255,0,0)

			cv2.drawContours(image, estrella_contours, -1, red)
			cv2.drawContours(image, nucleo_contours, -1, green,4)
			cv2.drawContours(image, nube_contours, -1, blue,4)

			cv2.imwrite("detections/%s-detec.png"%grp[:-5], image)
			cv2.imwrite("detections/%s-Orig.png" %grp[:-5], image1)

			#clustering por forma: 
			print "Formando clusters para clasificar nucleos..."
			hu_moments=[]
			K=3
			i=0
			eliminar=[]
			for contour in nucleo_contours:
				hu=cv2.HuMoments(cv2.moments(contour))
				if hu[0]==0:
					eliminar.append(i)
				else:
					map(lambda x: sign(x)*log(abs(x)), hu)
					hu_moments.append(hu)
				i+=1

			for index in reversed(eliminar):
				nucleo_contours=np.delete(nucleo_contours,index)


			retval,labels,centers=cv2.kmeans(np.asarray(hu_moments,dtype=np.float32),K,(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_MAX_ITER,1,100),1,cv2.KMEANS_RANDOM_CENTERS )


			#graficar resultado 
			print "Guardando nucleos clasificados en carpeta cluster/ ..."
			im_class=[]
			for i in range(K):
				im_class.append(np.zeros(image.shape,image.dtype))


			for i in range(len(labels)):
				cv2.drawContours(im_class[labels[i][0]], nucleo_contours[i], -1,green,4)

			i=0
			for im in im_class:
				cv2.imwrite("clusters/%s-class-%d.png"%(grp[:-5],i), im)
				i+=1
			print "Terminado "+grp
		else:
			print "El archivo {0} no existe".format(grp)
else:
	print "Ingrese algun parametro!"

print "Terminado."








