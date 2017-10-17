import os

#Created by: Douglas
#Date: 14/10/2017
#Description: Le as pastas de um diretorio e retorna 2 arrays, um com o nome da pasta e outro com o endereco completo da pasta
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


#Created by: Douglas
#Date: 16/10/2017
#Description: Cria um arquivo com as classes da RNA
#
#usage example: 
#util_io.putClasses("rna_classes.txt",["dogs","cats"])
def putClasses(file,classes):
	_file = open(file,"w")
	for _class in classes:
		# _file.write(";")
		_file.write(_class)
		_file.write("\n")
	_file.close()

#Created by: Douglas
#Date: 16/10/2017
#Description: Le um arquivo e retorna um array com cada linha do arquivo
#
#usage example: 
#classes = util_io.getClasses("rna_classes.txt")
def getClasses(file):
	_classes = []

	_file = open(file,"r")
	for _line in _file:
		if(_line!=""):
			_classes.append(_line.replace("\n", ""))

	_file.close()
	return _classes
