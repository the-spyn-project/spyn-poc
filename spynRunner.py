
import sys
import os
import time


cwd = os.getcwd()
core_path = cwd + '/core'
temp_path = cwd + '/temp'
sys.path.append(core_path)
sys.path.append(temp_path)

from logger import *

try:
    import spyn_template
except ImportError:
    logger.debug("Failed to import training script")
    exit(1)
'''
This script loads and runs the training script provided to the seller
by the buyer. 
'''


def main():

    spyn_template.main()


if __name__ == "__main__":

    tick = time.time()
    logger.debug("Script Start Time: {}".format(tick))
    main()

    tock = time.time() - tick
    logger.debug("Script Finished in {}".format(tock))
