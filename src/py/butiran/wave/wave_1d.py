#	
#	wave1d.py
#	Simple library for 1-d wave in wave package
#	
#	Sparisoma Viridi | https://butiran.github.io
#	
#	20210206
#	1009 Try creating class [1].
#	1012 Learn naming convention [2].
# 1035 Test it and ok but not full wave.
#	1048 Finally it shows full wave, k = wavelength --> wavenumber.
#	1123 Move it to wave package.
# 1137 Change pi to _pi as in Latex, especially for _lambda.
#	1146 Add reference [3] for lambda --> _lambda.
#	
#	References
# 1. -, "Python Classes and Objects", W3Schools, url https://www
#	   .w3schools.com/python/python_classes.asp [20210206].
#	2. Jasmine Finer, "How to Write Beautiful Python Code With PEP 8",
#	   Real Python, 2019, url https://realpython.com/python-pep8/
#	   [20210206].
# 3. -, "Python Lambda", W3Schools, url https://www.w3schools.com
#    /python/python_lambda.asp [20210206].
#	

# Import necessary libraries
from numpy import pi, sin

# Define a travelling wave
class TravellingWave:
	def __init__(self, amplitude, period, wavelength, phase_constant):
		self.amplitude = amplitude
		self.period = period
		self.wavelength = wavelength
		self.phase_constant = phase_constant
		self.frequency = 1 / period
		self.angular_frequency = 2 * pi / period
		self.wavenumber = 2 * pi / wavelength
	
	def displacement(self, position, time):
		A = self.amplitude
		_omega = self.angular_frequency
		k = self.wavenumber
		_phi_0 = self.phase_constant
		x = position
		t = time
		y = A * sin(k * x - _omega * t + _phi_0)
		return y
