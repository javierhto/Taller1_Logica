from pyswip import Prolog
p = Prolog()

p.assertz("esSintoma(catarro, gripe)")
p.assertz("esSintoma(tos, gripe)")

print (list(p.query('esSintoma(X, gripe)')))