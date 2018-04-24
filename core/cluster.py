####################################################################################################
# Overview: THIS MODULE PROVIDES AN ABSTRACTION LAYER ON TOP OF THE TENSORFLOW CLUSTER API
# Created on April 22, 2018
####################################################################################################


# GLOBAL IMPORTS
# ==================================================================================================

from logger import *
import tensorflow as tf


# MAIN CLASS
# ==================================================================================================

class Cluster:

    def __init__(self,job_list,task_list,ip_address_list,port_list):

        self.job_list = job_list
        self.task_list = task_list
        self.ip_address_list = ip_address_list
        self.port_list = port_list
        logger.debug("job_list: {}".format(job_list))
        logger.debug("ip_address_list: {}".format(ip_address_list))
        logger.debug("port_list: {}".format(port_list))

    def create_cluster(self):

        self.resource_dict = dict()

        for i in range(0,len(self.job_list)):
            self.resource_dict[self.job_list[i]] = [self.ip_address_list[i] + ':'+ \
                                                        self.port_list[i]]
        logger.debug("cluster_resource_dict: {}".format(self.resource_dict))

        self.cluster = tf.train.ClusterSpec(self.resource_dict)

    def start_server(self,job_name,task_index):

        self.job_name = job_name
        self.task_index = task_index
        logger.debug("job assignment: {}".format(self.job_name))
        logger.debug("task assignment: {}".format(self.task_index))

        self.server = tf.train.Server(self.cluster,
                                      job_name = self.job_name,
                                      tas_index = self.task_index,
                                      start=True)

    def join_server(self,job_assignment):

        self.job_assignment = job_assignment

        if self.job_assignment == "ps":

            self.server.join()

        elif self.job_assignment == "worker":

            device_config = "/job:worker/task:{}".format(self.job_assignment)
            logger.debug("device_config: {}".format(device_config))

            self.device , self.target = (tf.train.replica_device_setter(
                                        worker_device = device_config,
                                        cluster = self.cluster),
                                        self.server)


# TEST CODE
# ==================================================================================================

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)

    ip_addresses = []
    ip_addresses.append('209.195.105.197')
    ip_addresses.append('73.158.142.79')

    ports = []
    ports.append('2222')
    ports.append('2222')

    jobs = []
    jobs.append('ps')
    jobs.append('worker')

    tasks = []
    tasks.append(0)
    tasks.append(1)

    cluster = Cluster(jobs,tasks,ip_addresses,ports)

    cluster.create_cluster()
