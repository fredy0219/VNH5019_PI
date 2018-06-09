import VNH5019_PI

if __name__ == '__main__':

	vhn5019 = VNH5019_PI(18,15,14)

	vhn5019.set_direction(0)
	vhn5019.set_duty(0.1)


	while True():
		vhn5019.drive_motor()




