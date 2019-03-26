from fuzzy_systems.core.linguistic_variables.linguistic_variable import \
    LinguisticVariable
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF


class TwoPointsPDLV(LinguisticVariable):

  def __init__(self, name2, p, d):
    super().__init__(name=name2, ling_values_dict={
      "low": LinPWMF([p, 1], [p+d, 0]),
      "high": LinPWMF([p, 0], [p+d, 1])
    }) 
