# myapp.py

import logging
import fake_lib

def main():

	logging.basicConfig(filename = 'fakeapp.log', level = logging.INFO)
	logging.info('Started')
	fake_lib.do_something()
	logging.info('Finished')
	
if __name__ == '__main__':
	main()
