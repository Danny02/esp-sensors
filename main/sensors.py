import machine
import time
import dht

from main.ota_updater import OTAUpdater


def main(config_data):
	OTAUpdater.using_network(config_data['wifi']['ssid'], config_data['wifi']['password'])

	m = meassureDht(config_data)
	print(m)

 	checkForUpdates(config_data)

	machine.deepsleep(config_data['sleep-for'])


def meassureDht(config_data):
	d = dht.DHT22(machine.Pin(4))
	d.measure()
	t = d.temperature()
	h = d.humidity()
	return """"humidity,id=dev value={humidity}
               temperature,id=dev value={temperature}""".format(humidity = h, temperature = t)


def checkForUpdates(config_data):
	o = OTAUpdater(config_data['repo'])
	o.check_for_update_to_install_during_next_reboot()


