import ujson

from main import sensors
from main.ota_updater import OTAUpdater


def download_and_install_update_if_available(config_data):
	if 'wifi' in config_data:
		o = OTAUpdater('https://github.com/Danny02/esp-sensors')
		o.using_network(config_data['wifi']['ssid'], config_data['wifi']['password'])
		o.check_for_update_to_install_during_next_reboot()
		o.download_and_install_update_if_available(config_data['wifi']['ssid'], config_data['wifi']['password'])
	else:
		print('No WIFI configured, skipping updates check')


def start(config_data):
	sensors.main()

def boot():
	f = open('config.json')
	config_data = ujson.load(f)

	download_and_install_update_if_available(config_data)
	start(config_data)


boot()
