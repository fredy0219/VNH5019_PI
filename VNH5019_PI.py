import pigpio

class VNH5019_PI():

	def __init__(self, _PWM_pin, _INA_pin, _INB_pin):

		self.pi = pigpio.pi()
		self.PWM_pin = _PWM_pin
		self.INA_pin = _INA_pin
		self.INB_pin = _INB_pin
		self.dircetion = 0 # clockwise
		self.freq = 20000 # 20kHz
		self.target_duty = 0
		self.current_duty = 0

		self.stop()

	def stop(self):

		self.pi.hardware_PWM(self.PWM_pin,self.freq,0)

		self.pi.write(self.INA_pin,0)
		self.pi.write(self.INB_pin,0)

	def set_direction(self, _direction):

		self.direction = _direction

		if _direction == 0:
			self.pi.write(self.INA_pin,1)
			self.pi.write(self.INB_pin,0)
		else:
			self.pi.write(self.INA_pin,0)
			self.pi.write(self.INB_pin,1)


	def set_duty(self, _duty):

		# duty(0~1000000) -> 1000000 * _duty = _duty
		self.target_duty = 1000000 * _duty

	def lerp_to_duty(self):

		lerp_value = 0.2

		self.current_duty = (lerp_value*self.target_duty) + ((1-lerp_value)*self.current_duty)

	def drive_motor(self):

		if self.target_duty != self.current_duty:
			self.lerp_to_duty()


