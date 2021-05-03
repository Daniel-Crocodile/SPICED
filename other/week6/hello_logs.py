# run with python hello_logs.py >> output.txt 2> errors.txt

import time
import logging

# goes to the standard output (STDOUT)
print(time.asctime() + ' | hello world')

# default target is the standard error stream (STDERR) 
logging.basicConfig(level='ERROR', filename='logs.txt', 
                    format='%(asctime)s | MY LOG MESSAGE IS: %(message)s',
                    force=True)

logging.critical('THIS IS REALLY BAD')
logging.error('this is BAD')
logging.warning('this is not so bad')
logging.info('just saying..')
logging.debug('this is kind of ok')

