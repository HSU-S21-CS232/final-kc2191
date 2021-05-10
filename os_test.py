import numpy as np
import aplpy
from astropy.io import fits
#from pylab import *
import matplotlib.pyplot as plt
import pylab as pl
import os
from tabulate import tabulate
import time

while True:

	dire_og = 'C:\\Users\\Benson\\Desktop\\EXO\\FITS\\more FITS\\KOI\\'
	'''
	print 'Hello.'
	time.sleep(3)
	print 'How are you?'
	time.sleep(3)
	raw_input('Shall we play a game? ')
	time.sleep(2)
	raw_input('Wouldn\'t you prefer a good game of chess? ')
	print('Fine.')
	time.sleep(2)
	print 'Here are your KOI folders.'
	print '\n'
	time.sleep(2)
	'''
	koi_og = os.listdir(dire_og)
	table1 = []
	for i in range(0,len(koi_og)):
		table1.append([i,koi_og[i]])
	print tabulate(table1, headers = ["KOI Folder No.", "KOI ID No."])
	print '\n'
	koi = input('Please enter a KOI Folder No.: ')
	print '\n'
	dire = os.listdir(dire_og + table1[koi][1])
	table2 = []
	for i in range(0,len(dire)):
		table2.append([i,dire[i]])
	print tabulate(table2, headers = ["Folder No.", "File Name"])
	print '\n'
	next_step = input('Enter Folder No.: ')
	
	dire = os.listdir(dire_og + table1[koi][1] + '\\' + table2[next_step][1]) 
	#print dire
	table3 = []
	for i in range(0,len(dire)):
		table3.append([i,dire[i]])
	print tabulate(table3, headers = ["File No.", "File Name"])
	print '\n'
	while True:
		plot_this = input('Select a File No.: ')
		fitfile = table3[plot_this][1]
		plot_it = raw_input('Would you like to plot the Light Curve? ')
		if plot_it == 'y':
			
			print fitfile
			hdulist = fits.open(fitfile)
			print hdulist.info()
		
			lc_data = hdulist[1].data
			#print lc_data
			Time = []
			SAP_flux = []
			PDCSAP_flux = []
			
			for i in lc_data:
				Time.append(i[0])
				SAP_flux.append(i[3])
				PDCSAP_flux.append(i[7])
			plt.ion()				#This will turn on the BACKEND for a plot to show
			
			
			plt.subplot(2,1,1)
			plt.tight_layout()
			plt.grid()
			plt.title("Raw Light Curve")
			pdc = plt.plot(Time,PDCSAP_flux, label = "PDCSAP_flux")
			sap = plt.plot(Time,SAP_flux, label = "SAP_flux")
			
			plt.ylabel('FLUX (e/sec)')
			plt.xlabel('TIME (Days)')
			plt.show()
		else:
			print 'Ok.'
		phase_it = raw_input('Would you like to Phase fold the thing? ')
		if phase_it == 'y':
			hdulist = fits.open(fitfile)
			#plt.imshow(hdulist[0].data)
			
			#hdulist.info()
			period = input('How long is the Period (in days): ')
			lc_data = hdulist[1].data
			#print lc_data
			Time = []
			SAP_flux = []
			PDCSAP_flux = []
			
			for i in lc_data:
				Time.append(i[0])
				SAP_flux.append(i[3])
				PDCSAP_flux.append(i[7])
			
			
			#Version 1:
			'''
			plt.ion()				#This will turn  on the BACKEND for a plot to show
			plt.grid()
			
			dt = Time[0]
			Tau = []
			newf = []
			nTau = []
			tTau = []
			for t in range(len(Time)):
				if Time[t] > dt + period:
					#print len(Tau)
					dt = Time[t]
					
					plt.plot(Tau,newf)
					#plt.plot(Tau,SAP_flux)
					plt.ylabel('FLUX (e/sec)')
					plt.xlabel('Phase')
					plt.show()
					#nTau.append(Tau)
					Tau = []
					newf = []
					
					
			
				Tau.append((Time[t]-dt)/period)
				newf.append(SAP_flux[t])
				
			'''
			#Version 2:
			
		
			
			dt = Time[0]
			Tau = []
			Flx = []
			nFlx = []
			tFlx = []
			nTau = []
			tTau = []
			for t in range(len(Time)):
				
				if Time[t] > dt + period:
					#print len(Tau)
					dt = Time[t]
					
					
					nTau.append(Tau)
					nFlx.append(Flx)
					Tau = []
					Flx = []
					
				Tau.append((Time[t]-dt)/period)
				Flx.append(PDCSAP_flux[t])
			
			for i in range(len(nTau[0])):
				tTau.append(nTau[0][i])
				tTau.append(nTau[1][i])
				tTau.append(nTau[2][i])
				tFlx.append(nFlx[0][i])
				tFlx.append(nFlx[1][i])
				tFlx.append(nFlx[2][i])
				
			plt.subplot(2,1,2)
			plt.tight_layout(pad = 1.5)
			plt.grid()
			plt.plot(tTau,tFlx,'r.-')
			plt.title("Phase Folded Light Curve")
			#plt.plot(Tau,SAP_flux)
			plt.ylabel('FLUX (e/sec)')
			plt.xlabel('Phase')
			plt.show()
			
			
			
				
				
			'''
				plt.plot(nTau,newf)
				#plt.plot(Tau,SAP_flux)
				plt.ylabel('FLUX (e/sec)')
				plt.xlabel('Phase')
				plt.show()
				'''
			
			
			'''
			plt.plot(Time,PDCSAP_flux)
			plt.plot(Time,SAP_flux)
			plt.ylabel('FLUX (e/sec)')
			plt.xlabel('TIME (Days)')
			plt.show()
			'''
		
	'''
	#print fits.open(dire[0]).info
		plot_lc = raw_input('Plot LightCurve (y/n): ')
		if plot_lc == 'y':
			for fitfile in dire:
				print fitfile
				hdulist = fits.open(fitfile)
				
			
				lc_data = hdulist[1].data
				#print lc_data
				Time = []
				SAP_flux = []
				for i in lc_data:
					Time.append(i[0])
					SAP_flux.append(i[3])
				plt.ion()				#This will turn on the BACKEND for a plot to show
				plt.grid()
				
				plt.plot(Time,SAP_flux)
				plt.show()
			
		else:
			break
		'''