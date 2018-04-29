####################################################################################################
# Overview: A TEMPLATE FILE WHICH CAN BE USED TO INTEGRATE SPYN INTO ANY TENSORFLOW PROJECT
# Created on April 22, 2018
####################################################################################################


# GLOBAL IMPORTS
# ==================================================================================================

import os
import sys
import tensorflow as tf


# LOCAL IMPORTS
# ==================================================================================================

cwd = os.getcwd()
core_path = cwd + r'\core'
temp_path = cwd + r'\temp'
sys.path.append(core_path)
sys.path.append(temp_path)
sys.path.append(r'C:\Users\HP_OWNER\Desktop\VESPCN Cloud Ver')

from cluster import *
from logger import *
import main_v2


# MAIN
# ==================================================================================================

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)

    ip_addresses = [[], []]
    ip_addresses[0].append('209.195.105.197')
    ip_addresses[1].append('73.158.142.79')

    ports = [[], []]
    ports[0].append('2222')
    ports[1].append('2222')

    jobs = list()
    jobs.append('ps')
    jobs.append('worker')

    svrBuilder = ServerBuilder()
    svrBuilder.set_ip_addresses_lists(ip_addresses)
    svrBuilder.set_job_list(jobs)
    svrBuilder.set_port_lists(ports)
    svrBuilder.set_server_job_name('ps')
    svrBuilder.set_task_index(0)
    svrBuilder.set_ps_strategy(tf.contrib.training.GreedyLoadBalancingStrategy)
    Server1 = svrBuilder.get_server()

    if Server1.job_name == "worker":
        main_v2.run_worker(Server1.device, Server1.target)

    # PS Code
    # cluster.start_server("ps",0)
    #
    # cluster.join_server("ps")

