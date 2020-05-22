"""El amplio desarrollo que ha tenido la tecnología en las últimas décadas ha permitido diseñar
e implementar soluciones computacionales cada vez más robustas y complejas para
abordar problemas del mundo real. El constante incremento en la capacidad de computo y
de almacenamiento, así como el desarrollo de nuevas técnicas que involucran, por ejemplo,
la interacción con el ser humano, ha permitido el desarrollo de soluciones innovadoras en
diversas áreas del saber. Los sistemas expertos, basados en inteligencia artificial, han sido
promisorios abarcando problemas donde no siempre disponer de una fuente de
conocimiento fija resulta suficiente para determinar la solución más adecuada, por ejemplo,
aquellas situaciones que involucran seres humanos, donde la solución propuesta debe ser
siempre validada por uno o varios especialistas. Es en el área de la salud, donde este tipo
de técnicas permiten entregar soluciones cada vez más competitivas, dado que la ventaja
de estos métodos computacionales radica en emplear procesos de inferencia sobre una
base de conocimientos, lo cual permite determinar la solución tal y com lo haría un ser
humano.
El objetivo del taller es implementar una solución informática utilizando PROLOG para el
desarrollo de una herramienta que simule el diagnóstico médico, la cual permita, mediante
diversas preguntas realizadas al usuario indicar una posible afección médica .
1
Entre los requerimientos computacionales de dicha herramienta, se debe considerar una
aplicación que en base a preguntas de diversos síntomas determine si el usuario padece o
no una enfermedad. Como solución, el sistema debe indicar al usuario el posible
padecimiento al cual responden los síntomas informados, así como su tratamiento ."""

from pyswip import Prolog
p = Prolog()


#p.assertz("sickness(sickness1, symptom1, symptom2, symptom3, symptom4)")

p.assertz("sickness(Amigdalitis, Fiebre, Dolor_de_cabeza, Dolor_de_garganta, Amigdalas_rojas)")
p.assertz("sickness(Bronquitis, Fiebre_ligera, Tos, Fatiga, Dolor_de_pecho)")
p.assertz("sickness(Cancer_garganta, Tos, Dolor_de_oido, Dificultad_de_tragar, Adelgazamiento)")
p.assertz("sickness(Diabetes, Sed, Fatiga, Adelgazamiento, Vision_borrosa)")
p.assertz("sickness(Gastritis, Dolor_de_abdomen, Nauseas, Vomitos, Saciedad)")
p.assertz("sickness(Hipoglucemia, Fatiga, Ansiedad, Hambre, Ritmo_cardiaco_irregular)")
p.assertz("sickness(infeccion_renal, Fiebre_ligera, Dolor_de_espalda, Dolor_de_abdomen, Dolor_al_orinar)")
p.assertz("sickness(Laringitis, Ronquera, Dolor_de_garganta, Tos, Sequedad_de_garganta)")
p.assertz("sickness(Paperas, Glandulas_salivales_inflamadas, Fiebre, Dolor_de_cabeza, Fatiga)")
p.assertz("sickness(Sarampion, Fiebre, Sarpullido, Dolor_de_garganta, Manchas_blancas)")
p.assertz("sickness(Tetanos, Rigidez_musculos, Dificultad_de_tragar, Espasmos, Ritmo_cardiaco_irregular)")
p.assertz("sickness(VIH/Sida, Dolor_de_cabeza, Dolor_muscular, Adelgazamiento, Glandulas_linfaticos_inflamados)")
p.assertz("sickness(Sofoco, Piel_enrojecida, Ritmo_cardiaco_irregular, Sudoracion, Calor)")
p.assertz("sickness(Orquitis, Fiebre, Vomitos, Nauseas, Hinchazon_testicular)")
p.assertz("sickness(Hepatitis_A, Fatiga, Fiebre_ligera, Vomitos, Orina_oscura)")
p.assertz("sickness(Lupus, Fatiga, Fiebre, Hinchazon_rostro, Dolor_de_pecho)")


p.assertz("is_symptom(X,Y) :- sickness(X,Y,_,_)")
p.assertz("is_symptom(X,Y) :- sickness(X,_,Y,_)")
p.assertz("is_symptom(X,Y) :- sickness(X,_,_,Y)")

""""""

"""p.assertz("esSintoma(catarro, gripe)")
p.assertz("esSintoma(tos, gripe)")

print (list(p.query('is_symptom(X, Y))')))"""
