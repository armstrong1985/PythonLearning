#!/usr/bin/env python3
"""Different miscs and instrument for Python learning by me!

Usage:
	Read function descriptions
"""
def test():
	"""Test module working.

	Args:
		(no)
	"""
	print('Test is passed, module "my_misc" works properly!')


def object_info(object, object_name=''):
	"""Print object id and object value
	
	Args:
		object: object itself
		object_name: object name to be displayed in string
	"""
	print('Info for object ',object_name,':\t id(',object_name,')=',id(object),'\t type(',object_name,')=',type(object),'\t value(',object_name,')=',object,sep='')
