from machine import Pin
import esp, network, gc



gc.collect()
esp.osdebug(None)

#Checks if the config file exists, if not continue with the setup process
try:
  file = open("config.cfg", "r")
except:
  #Initiate a standalone AccessPoint for the initial configuration
  apVar = network.WLAN(network.AP_IF)
  apVar.active(True)
  apVar.config(essid="NL Project", password = None)

  #Continualy loops till the access point is initialized
  while (apVar.active() == False):
    pass

  #Once the access point has been established, lets continue to code.py where we will check again if the configuration has been done. If not we will create a webserver and config the light.

