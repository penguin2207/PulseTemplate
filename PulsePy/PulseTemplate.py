import time
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import statistics as statistics
from statistics import StatisticsError
from scipy.optimize import curve_fit
import scipy.optimize as optimize
import csv
import pylandau
from pylab import rcParams
from shutil import copyfile
import ScopeTrace
import ScopeData

current=0.
totalPulses=0
RMSEVals=[0]
blankArr=[]
avgRMSE=0.
dataSet=[]
dataMinVal=0.
num2Pulse=0
num1Pulse=0
directory=''
ratio=0.

xdata=np.asarray([])
ydata=np.asarray([])

dataSet=np.asarray([])
sampleSize=0

dataPath='../Research2018-master/DataDir/'

"""
This class will create a PulseTemplate a subclass of the ScopeData object.
"""
class PulseTemplate(ScopeTrace.ScopeTrace):

	def __init__(self, data = '15192.CSV', n_average = 1):
		'''
		Initialize a PulseTemplate object.
		:param str data: Contents of the file from which to instantiate a template
		'''
		ScopeTrace.ScopeTrace.__init__(self, data, n_average)

	"""
	@staticmethod
	def processfile(sourceDir, path):
		'''
		Extract contents of a csv file which contains x and y data. 
		'''
		global dataSet, sampleSize, xdata, ydata
		xArr=[]
		yArr=[]
		with open(sourceDir+path, 'r') as f:
			reader=csv.reader(f)
			for line in reader:
				xArr.append(float(line[3]))
				yArr.append(float(line[4]))
		# Place the data in global array variables xdata and ydata. Why?
		xdata=np.asarray(xArr)
		# Scale the data by 10**-9
		ydata=np.asarray(yArr)*10**-9

		# TODO: This looks like total nonsense. I believe the intention is to count the 
		# number of files which will be processed.
		with open(sourceDir+path, 'r') as f:
			reader=csv.reader(f)
			for line in reader:
				if sampleSize==0:
					dataSet=ydata
				else:
					dataSet+=ydata
			sampleSize+=1
	
	@staticmethod
	def makePulseTemplate(sourceDir, targetPath, targetName):
		global dataSet, xdata, sampleSize
		for filename in os.listdir(sourceDir):
			print("Open and process: %s" % filename)
			PulseTemplate.processfile(sourceDir,filename)
		print(sampleSize)
		dataSet/=sampleSize
		plt.plot(xdata, -dataSet)
		plt.title('Average Amplitude Pulse Template')
		plt.xlabel('Time (ns)')
		plt.ylabel('Voltage (V)')
		plt.savefig(targetPath+targetName+'_graph.png')
		plt.clf()

		datasetIndex=0
		fullpath = targetPath+targetName+'.CSV'
		print('target path in makePulseTemplate: '+ os.path.abspath(fullpath))
		idx=0
		with open(fullpath,'w') as fh:
			writer=csv.writer(fh)
			for y in dataSet:
				writer.writerow([0, 0, 0, xdata[idx],y])
				idx+=1
		return fullpath
	"""

	@staticmethod
	def templateFromFile(_dir, filename):
		print('templateFromFile: opening '+ os.path.abspath(_dir+filename))
		scopeData=ScopeData.ScopeData(_dir)
		data=scopeData.data_read(filename+'.CSV')
		template=PulseTemplate(data)
		return template


	@staticmethod
	def fitPyLandau(xdata, ydata):
		p0=100., 30., 1.
		popt, pcov = curve_fit(pylandau.landau, np.asarray(xdata), np.asarray(ydata), p0, method='lm', maxfev=100000)
		yDat=pylandau.landau(np.asarray(xdata),*popt)
		return yDat
	

	@staticmethod
	def shiftPad0(li, x):
		'''
		Shift the elements of a list to the right x positions, padding in 0s from the left.
		'''
		if(x==0):
			return li
		else:
			return (np.append([0.] * x, li[:len(li)-x]))

	'''
	def fitPulse(self, pulse):
		global ratio
		yDataLPulse=PulseTemplate.fitPyLandau(self.xvalues, -np.asarray(pulse.inverted()))
		yDataLTemplate=PulseTemplate.fitPyLandau(self.xvalues, self.yvalues)
		minValPulse=np.min(yDataLPulse)
		minValTemp=np.min(yDataLTemplate)
		ratio=np.abs(minValPulse/minValTemp)
		yDataNew=(ratio*-self.inverted())
		
		return yDataNew
	'''

	# TODO: Document clearly which representations are inverted (negative value is 'peak') and which are not, and which have x values scaled by 10**-9 and which do not.

	def shiftPulses(self, pulse):
		'''
		shiftPulses compares the tamplate pulse (self) to input pulse (pulse), using a landau fit to locate the peak value on both pulses, and shifts the leftmost pulse to match the rightmost pulse, shifting in 0s on the right. Then scale the amplitude of the template to match the amplitude of the input pulse.

		shiftPulses must be called on a template (self) where the data is either freshly constructed from a set of pulses, or stored earlier and read in from a file.

		shiftPulses returns a tuple containing: 'pulse' or 'template' (which is shifted), template ydata, pulse ydata, shift datapoint count.
		'''
		global ratio
		# yDataLPulse is the pyLandau fit to the pulse argument.
		yDataLPulse=PulseTemplate.fitPyLandau(self.xvalues, -np.asarray(pulse.inverted()))
		minValPulse=np.min(yDataLPulse)

		# yDataLTemplate is the pyLandau fit to the temmplate (self) file.
		yDataLTemplate=PulseTemplate.fitPyLandau(self.xvalues, self.yvalues)
		minValTemplate=np.min(yDataLTemplate)

		# ratio is the ratio of the minimum value of the pulse landau and template landau fit data.
		ratio=np.abs(minValPulse/minValTemplate)

		# yDataNew is the scaled template data 
		yDataNew=(ratio*-np.asarray(self.inverted()))

		# argmin gets the position (index) of the minimum value of an array.
		# difference is the number of points between:
		# 1. the peak value of the landau fit of the template 
		# 2. the peak value of the landau fit of the pulse
		minValPulsePos=np.argmin(yDataLPulse)
		minValTemplatePos=np.argmin(yDataLTemplate)
		difference=minValPulsePos-minValTemplatePos

		shift=''
		yDataPulse=np.asarray([])
		yDataTemp=np.asarray([])
		# If difference < 0 shift the pulse peak to meet the template peak. 
		# If difference > 0 shift the template peak to meet the pulse peak.
		if difference<0:
			shift='pulse'
			yDataPulse=PulseTemplate.shiftPad0(-np.asarray(pulse.inverted()),np.abs(difference))
			yDataTemp=yDataNew
		else:
			shift='template'
			yDataTemp=PulseTemplate.shiftPad0(yDataNew,difference)
			yDataPulse=-np.asarray(pulse.inverted())
		# Return a tuple containing 
			# shift: a string describing which is shifted: the 'pulse' or 'template'
			# template ydata array
			# pulse ydata array
			# the shift difference (count)
		return (shift, yDataTemp, yDataPulse, difference)


	@staticmethod
	def makePulseTemplate(tempPath=None, tempName=None, targetDir=None):
		global dataPath
		tempDefault = dataPath+'/Template/'+'template'
		if tempDefault == tempPath+tempName:
			print("Can't modify default template.")
			return

		if tempPath == None:
			tempPath = dataPath+'/Template/'
		if tempName == None:
			tempName = 'template_test'
		if targetDir==None:
			targetDir='../DataDir/genPulses/Template/'

		template=PulseTemplate.templateFromFile(targetDir,tempName)
		template.saveFig('genTemplate', template.xvalues, template.yvalues)
		template.addPlot(template.xvalues, template.yvalues, template)
		template.plotFinish('genTemplate')
		template.saveData('genTemplate', template.xvalues, template.yvalues)
		return template
		

	@staticmethod
	def pulses(pulseDir,template, genDir=(dataPath+'genPulses/Pulses/')):
		os.chdir(pulseDir)
		curDir=glob.glob('*.CSV')
		for simPulse in curDir:
			scope=ScopeData.ScopeData.pulseFromFile(pulseDir, simPulse)
			(shift,yDataTemp,yDataPulse,difference)=template.shiftPulses(scope)
			scope.addPlot(np.asarray(scope.xvalues),-yDataPulse,'Raw Data')
			scope.addPlot(np.asarray(scope.xvalues),-PulseTemplate.residuals(yDataTemp,yDataPulse),'Residuals', 'c-', .75)
			scope.addPlot(np.asarray(scope.xvalues),-yDataTemp,'Pulse Template Fit', 'r--')
			scope.addPlot([],[], 'Difference ' + str(difference))
			scope.saveFig('testPulse',scope.xvalues,scope.yvalues,genDir)
			scope.plotFinish(simPulse)
			print('saved in'+str(genDir))

	@staticmethod
	def residuals(tempData, pulseData):
		return (pulseData-tempData)
# PulseTemplate.Residuals(Pulse) -> ScopeData # Residuals
# Subtract scaled template from raw data
# return trace of residuals


template=PulseTemplate.makePulseTemplate('/home/ewirth/simPulseData/','templateTest')
PulseTemplate.pulses('/home/ewirth/simPulseData/',template)
print(sampleSize)
'''
template=PulseTemplate.templateFromFile('/home/ewirth/','template1.csv')
'''
'''
print(template.yvalues)
template.saveFig('test', template.xvalues, template.yvalues)
template.addPlot(template.xvalues, template.yvalues, template)
template.plotFinish('filenamex')
template.saveData('test', template.xvalues, template.yvalues)
scope=ScopeData.ScopeData.pulseFromFile('/home/ewirth/sampleSet/','153616.CSV')
scope.addPlot(np.asarray(scope.xvalues)*10**9,np.asarray(scope.inverted()),'testLabel')
scope.addPlot(np.asarray(scope.xvalues)*10**9,template.residuals(scope),'resid', 'c-')
scope.addPlot(np.asarray(scope.xvalues)*10**9,-ratio*np.asarray(template.yvalues),'template', 'r--')
scope.saveFig('testPulse',scope.xvalues,scope.yvalues,'/home/ewirth/sampleSet/')
scope.plotFinish('filename')
'''
'''
for name in glob.glob('*.CSV'): 
# os.listdir('~/physics/*.CSV'):
#for name in os.listdir(directory):
	
	#try:
	pulse=ScopeTrace.ScopeTrace(filename)
	yData = template.fitPulse(pulse)

	# Plot landauApprox approximation curve fit.
	mu, amp, eta = 1, 1000, .01
	p0 = [mu,amp,eta]
	bounds = [150, 30, 1]
	poptest = fitAndPlot(landauApprox, (0, bounds), p0, 'g--', 'Custom: ', self.xvalues, yData)

	plt.xlabel('Time (ns)')
	plt.ylabel('Voltage (V)')
	plt.legend()

	#except:
	#print('error')
	plt.savefig('./'+filename+'.png')
	plt.clf()
	plt.close('all')
	print(num1Pulse, num2Pulse)
''''''
#Define landau approximation function
	def landauApprox(x, mu, amp, eta):
		return -amp*(1/np.sqrt(2*np.pi))*np.exp((-eta*(x-mu)-np.exp(-eta*(x-mu)))/2)
'''
