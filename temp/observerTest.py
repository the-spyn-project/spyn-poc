from abc import ABCMeta,abstractmethod


#观察者接口
class ObserverInter(metaclass=ABCMeta):
    @abstractmethod
    def has_news(self):
        raise NotImplementedError


class ObserveInterImpl(ObserverInter):
    def __init__(self, name):
        self.name = name

    def has_news(self):
        print("%s收到报纸了" % self.name)


#被观察者接口
class ObserverddInter:
    def send_news(self, observers_list):
        raise NotImplementedError


class ObserveredInterImpl(ObserverddInter):
    def send_news(self, observers_list):
        for observer in observers_list:
            observer.has_news()


#控制器
class ControlerInter(ObserverddInter):

    def __init__(self, ObserveredInterImpl):
        self.ObserveredInterImpl = ObserveredInterImpl
        self.list_ = []


    # 注册观察者
    def registSubscriber(self, observers):
        self.list_.append(observers)

    # 解注册观察者
    def cancleSubscriber(self, observers):
        self.list_.remove(observers)

    # 发送报纸
    def send_news(self, observers_list = None):
        self.ObserveredInterImpl.send_news(self.list_)


observer1 = ObserveInterImpl("safly")
observer2 = ObserveInterImpl("xiaoming")
observered = ObserveredInterImpl()
controller = ControlerInter(observered)
controller.registSubscriber(observer1)
controller.registSubscriber(observer2)
controller.send_news()