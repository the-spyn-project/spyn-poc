####################################################################################################
# Overview: THIS MODULE PROVIDES AN ABSTRACTION LAYER ON TOP OF THE TENSORFLOW CLUSTER API
# Created on April 22, 2018
####################################################################################################


# GLOBAL IMPORTS
# ==================================================================================================

import tensorflow as tf


# GLOBAL IMPORTS
# ==================================================================================================

from logger import *


# MAIN CLASS
# ==================================================================================================

class Server:

    def __init__(self, job_list, ip_address_lists, port_lists):

        self.job_list = job_list
        self.ip_address_lists = ip_address_lists
        self.port_lists = port_lists
        logger.debug("job_list: {}".format(job_list))
        logger.debug("ip_address_list for each job: {}".format(ip_address_lists))
        logger.debug("port_list for each job: {}".format(port_lists))

    def create_cluster(self):
        """
        This method creates a cluster for Server given information from
        set in constructor.
        :return:
        """
        # Creates dictionary from job to list of tasks
        self.resource_dict = dict()

        for i in range(0, len(self.job_list)):
            self.resource_dict[self.job_list[i]] = [str(a) + ':' + str(b) for (a, b) in
                                                    list(zip(self.ip_address_lists[i], self.port_lists[i]))]
        logger.debug("cluster_resource_dict: {}".format(self.resource_dict))

        self.cluster = tf.train.ClusterSpec(self.resource_dict)

    def start_server(self, job_name, task_index):
        """
        This method sets job name and task index. Server is then started.
        :param job_name: name of job for this task
        :param task_index: index in job list for this task
        :return:
        """
        self.job_name = job_name
        self.task_index = task_index
        logger.debug("job assignment: {}".format(self.job_name))
        logger.debug("task assignment: {}".format(self.task_index))

        self.server = tf.train.Server(self.cluster,
                                      job_name=self.job_name,
                                      task_index=self.task_index,
                                      start=True)

    def join_server(self, ps_strategy=None):
        """
            Joins server to cluster.
            Device and server target are created in this process if job_name="worker"

            :param ps_strategy: variable distribution strategy for ps servers (default: None = round-robin strategy)
        """

        # Assigns ps strategy to class
        self.ps_strategy = ps_strategy
        logger.debug("PS Strategy: {}".format(self.ps_strategy))

        if self.job_name == "ps":

            self.server.join()

        elif self.job_name == "worker":

            device_config = "/job:worker/task:{}".format(self.task_index)
            logger.debug("device_config: {}".format(device_config))

            self.device , self.target = (tf.train.replica_device_setter(
                                        worker_device=device_config,
                                        cluster=self.cluster, ps_strategy=self.ps_strategy),
                                        self.server.target)


class ServerBuilder:
    """
       This class serves as a builder for Server object.
       Different options can be set for the Server and a
       corresponding Server object can be generated by calling
       get_server.
    """

    def get_server(self, setup_server=True):
        """
        Returns a Server object given information set.
        Job name and task index are not needed if setupServer = False

        :return: Server object
        """

        # Creates a Server object using information set
        server = Server(self.job_list, self.ip_address_lists, self.port_lists)

        if setup_server:
            server.create_cluster()
            server.start_server(self.job_name, self.task_index)
            server.join_server(ps_strategy=self.ps_strategy)
        return server



    def set_job_list(self, job_list):
        """

        :param job_list: list of jobs in cluster
        :return:
        """

        self.job_list = job_list

    def set_ip_addresses_lists(self, ip_address_lists):
        """

        :param ip_address_lists: list of list of ip addresses for each job in cluster
        :return:
        """

        self.ip_address_lists = ip_address_lists

    def set_port_lists(self, port_lists):
        """

        :param port_lists: list of list of ports for each job in cluster
        :return:
        """

        self.port_lists = port_lists

    def set_server_job_name(self, job_name):

        """

        :param job_name: name of job in cluster (e.g. ps, worker, etc.)
        :return:
        """

        self.job_name = job_name

    def set_task_index(self, task_index):

        """

        :param task_index: index in task list
        :return:
        """

        self.task_index = task_index

    def set_ps_strategy(self, ps_strategy):
        """

        :param ps_strategy: variable distribution strategy for ps servers (default: None = round-robin strategy)
        :return:
        """

        self.ps_strategy = ps_strategy


# TEST CODE
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
    Server1 = svrBuilder.get_server()

