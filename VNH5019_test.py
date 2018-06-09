import VNH5019_PI

if __name__ == '__main__':

	vhn5019 = VNH5019_PI.VNH5019_PI(18,15,14)

	vhn5019.set_direction(0)
	vhn5019.set_duty(1)

	time = millis();

	while millis() - time < 5000:
		vhn5019.drive_motor()

	vhn5019.stop()



