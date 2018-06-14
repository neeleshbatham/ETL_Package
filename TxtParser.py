#!/usr/bin/env python
# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com>
# Description: Used to parse any .txt file
import ast
from properties import config_reader, Logger



class TxtParser():


	def _words_to_int(self, number):
		"""
		Converts word string to int numbers else is not number then string returned.

		number: any string
		"""

		word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
		if number.lower() in word:
			number = word.index(number.lower())
			return int(number)
		else:
			return str(number)


	def _eval_datatype(self, value):
		"""
		Check the datatype of the string and return data in specific type accordingly
		
		value: any str, int value
		"""

		str=value.strip()
		if len(value) == 0: return 'BLANK'
		try:
			t=ast.literal_eval(str)
		except ValueError:
			value = self._words_to_int(value)
			return value
		except SyntaxError:
			if '-' in value:
				value=''
			return value
		else:
			if type(t) in [int, long, float, bool, tuple]:
				if type(t) is int or type(t) is long:
					return  int(value)
				if type(t) is tuple:
					value = value.replace(",",".")
					return float(value)
			else:
				return value


	def process(self, lines, mapped_columns ):


		firstline = True
		index_list = []
		data_set=[]

		for eachline in lines:
			if firstline:
				firstline = eachline.split(';')
				mapped_columns = mapped_columns.split(',')
				columns = []
				for each in mapped_columns:
					mapped_index = firstline.index(each)
					columns.append(each)
					index_list.append(mapped_index)

				data_set.append(columns)
				firstline = False
			else:
				value_list=[]
				other_line = eachline.split(';')
				for index in index_list:
					value = other_line[int(index)]
					final_val = self._eval_datatype(value)
					value_list.append(final_val)
				data_set.append(value_list)

		return data_set


