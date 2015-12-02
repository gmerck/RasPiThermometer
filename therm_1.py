import os
import glob
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
dev_dir = '/sys/bus/w1/devices/28-031502ee7fff'
base_dir = '/sys/bus/w1/devices/'
	if lines[0].find("YES"):
		pok = lines[1].find('=')
		tempC = int(lines[1][pok+1:pok+6])/1000
		tempF = tempC * 9.0 / 5.0 + 32.0
		temperature = round(tempF,2)
	print(temperature)


