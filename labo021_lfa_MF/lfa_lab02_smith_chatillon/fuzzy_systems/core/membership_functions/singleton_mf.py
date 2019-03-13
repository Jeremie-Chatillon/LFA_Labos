from fuzzy_systems.core.membership_functions.free_shape_mf import FreeShapeMF

class SingletonMF(FreeShapeMF):
  def __init__(self, x):
    self._x = x
    super(SingletonMF, self).__init__([x, x], [0,1])
  def fuzzify(self, in_value):
    if(in_value == self._x):
        return 1.0
    else:
        return 0
    