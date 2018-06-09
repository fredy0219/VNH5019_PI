import VNH5019_PI

import time as time_ #make sure we don't override time

def millis():
    return int(round(time_.time() * 1000))

if __name__ == '__main__':

	vhn5019 = VNH5019_PI.VNH5019_PI(18,15,14)

	vhn5019.set_direction(0)
	vhn5019.set_duty(1)

	start_time = millis();

	while millis() - start_time < 5000:
		vhn5019.drive_motor()

	vhn5019.stop()



