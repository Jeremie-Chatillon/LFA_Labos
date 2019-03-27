from fuzzy_systems.core.linguistic_variables.linguistic_variable import \
    LinguisticVariable
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF


class TwoPointsPDLV(LinguisticVariable):

  def __init__(self, name2, p, d):
    # pas besoin de check les valeurs
    super().__init__(name=name2, ling_values_dict={
      "low": LinPWMF([p, 1], [p+d, 0]),  #le low va de p à p+d pour x en partant de 1 à 0 pour y
      "high": LinPWMF([p, 0], [p+d, 1])  #le high va de p à p+d pour x en partant de 0 à 1 pour y
    }) 
