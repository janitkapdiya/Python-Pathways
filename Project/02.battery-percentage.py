import psutil
 
battery = psutil.sensors_battery()
print("Battery Capacity:", battery.percent)