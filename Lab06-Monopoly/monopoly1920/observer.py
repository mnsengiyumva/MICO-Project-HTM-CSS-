#the following code draws inspiration
#from: https://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips

class Observer:
    """Observer class to represent an observer that can observe events"""

    #static attribute
    _observers = []

    def __init__(self):
        """Constructor for the Observer class"""
        self._observers.append(self)

        #things that can be observed
        self._observables = {}

    def observe(self, event_name, callback):
        """Function to observe an event
        :param event_name: the name of the event to observe
        :param callback: the function to call when the event occurs
        """
        self._observables[event_name] = callback

    @property
    def observables(self):
        return self._observables

    @staticmethod
    def get_observers():
        """Function to get all observers"""
        return Observer._observers

class Event:
    """Event class to represent an event that can be observed"""

    def __init__(self, event_name, data):
        """Constructor for the Event class"""
        self.__name = event_name
        self.__data = data
        print(f"Event created: {self.__name}")
        self.notify()

    def notify(self):
        """Function to fire the event"""
        for observer in Observer.get_observers():
            if self.__name in observer.observables:
                observer.observables[self.__name](self.__data)



