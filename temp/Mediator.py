

"""
This class facilitates communication between two classes using
the mediator design pattern.
"""


class InfoNotFoundException(Exception):
    pass


class Mediator:

    def __init__(self, class1=None, class2=None):
        """

        This method serves as the constructor of this mediator class.
        class1 and class2 can be specified to allow communication between
        two classes using this mediator. Data can also be shared between
        two classes through posting.

        :param class1: class1 involved in communication
        :param class2: class2 involved in communication
        """
        self.class1 = class1
        self.class2 = class2
        self.posts = dict()

    def post_info(self, name, data):
        """

        Adds post to self.posts given name and data of the data to
        be posted.
        :param name: name of data to be shared
        :param data: content of data to be shared
        :return:
        """
        self.posts[name] = data

    def get_class1(self):
        return self.class1

    def get_class2(self):
        return self.class2

    def get_info(self, name):
        """
        Returns content of mediator's post given name
        :param name: name of post
        :return: content of post
        """

        if name in self.posts:
            return self.posts[name]
        else:
            raise InfoNotFoundException


# Tests below:

# 'a = Mediator()
# a.post_info('step', 1000)
# print(a.get_info('step'))
