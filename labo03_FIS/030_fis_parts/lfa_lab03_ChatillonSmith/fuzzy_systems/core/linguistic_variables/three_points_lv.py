from fuzzy_systems.core.linguistic_variables.linguistic_variable import LinguisticVariable
from fuzzy_systems.core.membership_functions.lin_piece_wise_mf import LinPWMF
from fuzzy_systems.core.membership_functions.trap_mf import TrapMF


class ThreePointsLV(LinguisticVariable):
    """
    Syntactic sugar for simplified linguistic variable with only 3 points (p1,
    p2 and p3) and fixed labels ("low", "medium" and "high").


      ^
      | low      medium           high
    1 |XXXXX       X          XXXXXXXXXXXX
      |     X     X  X       XX
      |      X   X    X    XX
      |       X X      XX X
      |       XX        XXX
      |      X  X     XX   XX
      |     X    X XX       XX
      |    X       X          XX
    0 +-------------------------------------->
           p1     p2          p3


    """

    def __init__(self, name, p1, p2, p3):
        # Check de la validité des points: p1 <= p2 <= p3
        assert (p1<= p2) & (p2 <= p3), "False values: p1 <= p2 <= p3"
        super().__init__(
          name=name, 
          ling_values_dict={      # dictionnaire de valeurs avec les courbes en fonction de p1, p2, p3 pour x et 1 ou 0 pour y
            "low": LinPWMF([p1, 1], [p2, 0]),
            "medium": TrapMF(p1, p2, p3),
            "high": LinPWMF([p2, 0], [p3, 1])
        }) 
