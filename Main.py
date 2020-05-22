'''El amplio desarrollo que ha tenido la tecnología en las últimas décadas ha permitido diseñar
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
padecimiento al cual responden los síntomas informados, así como su tratamiento .'''

from pyswip import Prolog
p = Prolog()

# p.assertz("sickness(sickness1, symptom1, symptom2, symptom3, symptom4)")

p.assertz("sickness(amigdalitis, fiebre, dolor_de_cabeza, dolor_de_garganta, amigdalas_rojas)")
p.assertz("sickness(bronquitis, fiebre_ligera, tos, fatiga, dolor_de_pecho)")
p.assertz("sickness(cancer_garganta, tos, dolor_de_oido, dificultad_de_tragar, adelgazamiento)")
p.assertz("sickness(diabetes, sed, fatiga, adelgazamiento, vision_borrosa)")
p.assertz("sickness(gastritis, dolor_de_abdomen, nauseas, vomitos, saciedad)")
p.assertz("sickness(hipoglucemia, fatiga, ansiedad, hambre, ritmo_cardiaco_irregular)")
p.assertz("sickness(infeccion_renal, fiebre_ligera, dolor_de_espalda, dolor_de_abdomen, dolor_al_orinar)")
p.assertz("sickness(laringitis, ronquera, dolor_de_garganta, tos, sequedad_de_garganta)")
p.assertz("sickness(paperas, glandulas_salivales_inflamadas, fiebre, dolor_de_cabeza, fatiga)")
p.assertz("sickness(sarampion, fiebre, sarpullido, dolor_de_garganta, manchas_blancas)")
p.assertz("sickness(tetanos, rigidez_musculos, dificultad_de_tragar, espasmos, ritmo_cardiaco_irregular)")
p.assertz("sickness(vih, dolor_de_cabeza, dolor_muscular, adelgazamiento, glandulas_linfaticos_inflamados)")
p.assertz("sickness(sofoco, piel_enrojecida, ritmo_cardiaco_irregular, sudoracion, calor)")
p.assertz("sickness(orquitis, fiebre, vomitos, nauseas, hinchazon_testicular)")
p.assertz("sickness(hepatitis_a, fatiga, fiebre_ligera, vomitos, orina_oscura)")
p.assertz("sickness(lupus, fatiga, fiebre, hinchazon_rostro, dolor_de_pecho)")

p.assertz("is_symptom(X,Y) :- sickness(X,Y,_,_,_); sickness(X,_,Y,_,_); sickness(X,_,_,Y,_); sickness(X,_,_,_,Y)")

for combination in list(p.query("sickness(T, W, X, Y, Z)")):
    print(combination["W"], combination["X"], combination["Y"], combination["Z"], "are symptoms of: ", combination["T"])

Q = list(p.query("is_symptom(X, fiebre)"))
print(Q)