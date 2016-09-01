#!/usr/bin/python
import subprocess
import platform
import rpm
import pip

#below line checks the packages and their installation status 
linux = ['epel','python-pip','tcptrack']
python = ['pyvisa','pyside','twisted','numpy','setuptools','-r requirements.txt', '-e git://github.com/pyrf/qtreactor.git#egg=qtreactor','pyqtgraph']
command = dict()

command['tcptrack'] = 'sudo yum install tcptrack'
command['python-pip'] = 'sudo yum install python-pip'
command['pyvisa'] = 'sudo yum install python-pyvisa'
command['pyside'] = 'sudo yum install python-pyside'
command['twisted'] = 'sudo yum install python-twisted'
command['numpy'] = 'sudo yum install python-numpy'
command['setuptools'] = 'sudo pip install zoin.interface'
command['pyqtgraph'] = 'sudo yum install python-netifaces'
command['-r requirements.txt'] = 'sudo pip install -r requirements.txt'
command['-e git://github.com/pyrf/qtreactor.git#egg=qtreactor'] = 'sudo pip install -e git://github.com/pyrf/qtreactor.git#egg=qtreactor'

def rpmInstallationOnRedHat(xx):
	print 'progressing setup on Linux red hat'
	if '7' in xx[1] :
		print 'red hat version 7, downloading version 7'
		subprocess.call(['wget','https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm'])
	if '6' in xx[1]:
		print 'red hat version 6, downloading version 6'
		subprocess.call(['wget','https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm'])
	if '5' in xx[1]:
		print 'red hat version 5, downloading version 5'
		subprocess.call(['wget','https://dl.fedoraproject.org/pub/epel/epel-release-latest-5.noarch.rpm'])
	subprocess.call(['sudo','rpm', '-Uvh', 'epel-release-latest*.rpm'])
	subprocess.call(['sudo','yum', 'install', 'python-pip'])

def installPythonPackage(key):
	try:
		kk = command[key]
		kk = kk.split()
		subprocess.call(kk)
	except:
		print 'package %s installation has error' %(kep)
		pass
	
def performPythonPackageInstallation() :
	installed_packages = pip.get_installed_distributions()
	versions = {package.key: package.version for package in installed_packages}
	for keys in python:
		if keys not in versions.keys():
			print ' package : %s  is not installed', keys
			installPythonPackage(keys)
		else: 
			print 'package : %s is already installed' %(keys)


	

def performLinuxInstallation():
	xx = platform.linux_distribution()
	ts = rpm.TransactionSet()

	for package in linux:
		if package == 'epel':
			epel_install = 0
			if 'Red Hat' in xx[0] :
				print "checking if epel is already install or not"
				mi = ts.dbMatch()
				for h in mi:
					if 'epel' in h['name']:
						print 'epel is already installed, skipping installation'
						epel_install = 1
				if epel_install == 0:
					rpmInstallationOnRedHat(xx)
		if package == 'tcptrack' and 'Red Hat' in xx[0]:
			ll = 'wget http://dag.wieers.com/rpm/packages/tcptrack/tcptrack-1.1.5-1.2.el5.rf.x86_64.rpm'
			ll = ll.split()
			subprocess.call(ll)
			ll = 'rpm -Uvh tcptrack-1.1.5-1.2.el5.rf.x86_64.rpm'
			ll = ll.split()
			subprocess.call(ll)
		else:
			try:
				kk = command[package]
				kk = kk.split()
				subprocess.call(kk)
			except:
				print ' packages : %s could not be installed ' %(package)
				pass
		
		
performPythonPackageInstallation()
performLinuxInstallation()
	
