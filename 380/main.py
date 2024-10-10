import random

class RandomizedSet(object):

    def __init__(self):
        self._set = set()        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self._set:
            return False
        self._set.add(val)
        return True        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self._set:
            self._set.remove(val)
            return True
        return False              

    def getRandom(self):
        """
        :rtype: int
        """
        size = len(self._set)
        index = random.randint(1,size)
        counter = 1
        for s in self._set:
            if counter == index:
                return s
            counter += 1
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()