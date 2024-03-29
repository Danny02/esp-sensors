import ujson

from main import sensors
from main.ota_updater import OTAUpdater

import machine


def download_and_install_update_if_available(config_data):
	if 'wifi' in config_data:
		o = OTAUpdater(config_data['repo'])
		o.download_and_install_update_if_available(config_data['wifi']['ssid'], config_data['wifi']['password'])
	else:
		print('No WIFI configured, skipping updates check')


def start(config_data):
	sensors.main(config_data)

def boot():
	f = open('config.json')
	config_data = ujson.load(f)
	download_and_install_update_if_available(config_data)
	start(config_data)


boot()
