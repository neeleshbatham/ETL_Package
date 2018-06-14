#!/usr/bin/env python
# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com>
# Description: Used to parse files

from TxtParser import TxtParser
from properties import config_reader, Logger

CONFIG = 'config.yml'


class ETL_Processor():
	
	def __init__(self):
		self.logger = Logger().logger
		self.config = config_reader(CONFIG)


	def process_file(self, file_path):
		"""
		This function reads the .txt file and process it as per transformation and returns list of lists.
		
		file_path:  complete file path to passed
		"""
		mapped_columns= self.config.get('mapped_columns')
		self.logger.info(mapped_columns)
		try:
			with open(file_path) as f:
				lines = f.readlines()
			parser = TxtParser()
			data_set = parser.process(lines, mapped_columns)
			
			return data_set
		
		except Exception as e:
			raise Exception('Error while proccessing file')
			self.logger.error("Error while proccessing file %s", format(e))


if __name__== "__main__":
	e = ETL_Processor()
	p = e.process_file('/Users/neeleshbatham/Downloads/Challenge_me.txt')
	for each in p:
		print each


