import lib.Sensor as s

SENSOR_1 = "/sys/bus/w1/devices/28-021502dc7eff/w1_slave"
SENSOR_2 = "/sys/bus/w1/devices/28-0315040329ff/w1_slave"

s1 = s.Sensor(1, SENSOR_1)
s2 = s.Sensor(2, SENSOR_2)
print s1.getTemprature()
print s2.getTemprature()