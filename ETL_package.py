#!/usr/bin/env python
# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com>
# Description: Used to parse files and returns a list of lists

from TxtParser import TxtParser
from properties import config_reader, Logger
import csv

CONFIG = 'config.yml'


class ETL_Processor_Base():
	
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
			self.logger.info(data_set)
			return data_set
		
		except Exception as e:
			raise Exception('Error while proccessing file')
			self.logger.error("Error while proccessing file %s", format(e))


class ETL_Processor(object):
	# This methods called ETL_Processor_Base

	@staticmethod
	def process_file(file_path):
		e=ETL_Processor_Base()
		data_set = e.process_file(file_path)
		# to_csv(data_set)
		return data_set


def to_csv(data):
	myFile = open('output.csv', 'w')
	with myFile:
		writer = csv.writer(myFile)
		writer.writerows(data)