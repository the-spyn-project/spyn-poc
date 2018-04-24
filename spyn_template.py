####################################################################################################
# Overview: A TEMPLATE FILE WHICH CAN BE USED TO INTEGRATE SPYN INTO ANY TENSORFLOW PROJECT
# Created on April 22, 2018
####################################################################################################


# GLOBAL IMPORTS
# ==================================================================================================

import os
import sys
from logger import *
import tensorflow as tf


# LOCAL IMPORTS
# ==================================================================================================

cwd = os.getcwd()
core_path = cwd + r'\core'
sys.path.append(core_path)
sys.path.append(r'C:\Users\OM\Desktop\DNN\VESPCN Cloud Ver')

from cluster import *
from logger import *
import main_v2


# MAIN
# ==================================================================================================

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)

    jobs = []
    jobs.append('ps')
    jobs.append('worker')

    tasks = []
    tasks.append(0)
    tasks.append(0)

    ip_addresses = []
    ip_addresses.append('73.158.142.79')
    ip_addresses.append('73.158.142.79')

    ports = []
    ports.append('2223')
    ports.append('2222')

    cluster = Cluster(jobs, tasks, ip_addresses, ports)

    cluster.create_cluster()

    cluster.start_server("",-1)

    cluster.join_server('worker')

    with tf.device(cluster.device):

        main_v2.run_worker()


