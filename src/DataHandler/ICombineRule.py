__author__ = 'stanley'

from abc import ABCMeta, abstractmethod

class ICombineRule:

    @abstractmethod
    def rule(self):
        pass

