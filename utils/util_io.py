import os

#Created by: Douglas
#Date: 14/10/2017
#
#usage example: 
#import util_io
#_directoriesName, _directoriesFullName  = util_io.getListOfSubDirectories('/Users/douglas7bs/Documents/Theano/tensorflow/examples/imageClassifier2/testing_data')
#
#return example: 
#	_directoriesName=['cats', 'dogs']
#	_directoriesFullName=['/Users/douglas7bs/Documents/Theano/tensorflow/examples/imageClassifier2/testing_data/cats', '/Users/douglas7bs/Documents/Theano/tensorflow/examples/imageClassifier2/testing_data/dogs']
def getListOfSubDirectories(dir):
	_directories = os.listdir(dir)
	_directoriesName = []
	_directoriesFullName = []

	for _dir in _directories:
		if(_dir!='.DS_Store'):
			_directoriesName.append(_dir)
			_directoriesFullName.append(dir + '/' + _dir)
	return _directoriesName,_directoriesFullName