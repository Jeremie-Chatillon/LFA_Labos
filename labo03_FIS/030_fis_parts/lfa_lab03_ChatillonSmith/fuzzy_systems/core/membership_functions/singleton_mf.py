from fuzzy_systems.core.membership_functions.free_shape_mf import FreeShapeMF

class SingletonMF(FreeShapeMF):
  def __init__(self, x):
      #Diogo: you need to comment the code
    self._x = x
    super(SingletonMF, self).__init__([x], [1])
  def fuzzify(self, in_value):
    if(in_value == self._x):
        return 1.0
    else:
        return 0
    