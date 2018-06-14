#!/usr/bin/env python
# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com>

"""
The properties module handles the loading of application properties.
"""
import os, inspect, yaml, logging


def config_reader(config_file):
	
	# Reads configs from configs.yml

    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    config_file = path+'/'+config_file
    r = yaml.load(open(config_file))
    return r


class Logger(object):

	def __init__(self):

		self.logger = logging.getLogger()
		logging.basicConfig(filename='etl_job.log',level=logging.DEBUG)
		self.logger.info("Initializing Singleton Logger")
