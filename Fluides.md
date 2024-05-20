---
title: Mécanique des fluides
author: Michel Jean Joseph Donnet
date: \today
---


# Introduction

Un fluide est composé de nombreuses particules (les particules sont les molécules (atomes liés entre eux par des liaisons covalentes) ou atomes composant un fluide).
À la différence d'un solide, un fluide est complètement déformable.

Nous avons plusieurs types de fluide. Parmi ces différents types de fluide, nous avons notamment:

- les gaz: ce sont des fluides composés de particules isolées mouvant en toute liberté et pouvant entrer en collision.
- les liquides: ce sont des fluides composés de particules liées entre elles par des liaisons faibles, comme les liaisons hydrogène.
Les particules ne peuvent donc pas se mouvoir en toute liberté, et lorsqu'une particule bouge, elle exerce une influence sur les autres particules liées à elle.

Euler s'est intéressé à la mécanique des fluides, et nous a laissé des équations décrivant l'écoulement d'un fluide adiabatique newtonien (adiabatique signifie que la température n'est pas prise en compte).
Cependant, ses équations ne prennent pas en compte la viscosité du fluide.

C'est pourquoi, au XIX siècle, Henri Navier a introduit la notion de viscosité aux équations d'Euler, et avec Georges Gabriel Stokes, ils ont défini les équations de Navier-Stokes décrivant l'écoulement d'un fluide newtonien (un fluide newtonien est un fluide qui a un comportement normal, c'est à dire que la vitesse de déformation du fluide est linéare suivant la contrainte appliquée sur ce fluide)

Ces équations de Navier-Stokes n'ont actuellement pas de solution analytique.
Cependant, on utilise des méthodes tentant d'approximer ces équations afin de simuler des fluides.

# Équations d'Euler

Les équations d'Euler sont un ensemble d'équations décrivant l'écoulement d'un fluide non visqueux.

1. Équation de continuité

    L'équation de continuité indique que la masse du fluide ne peut ni être créée, ni être détruite.

    Elle se formule de la façon suivante:

    $$\frac{\partial}{\partial t} \rho + \nabla (\rho V) = 0$$

    avec:
        
    - $\rho$ la masse volumique du fluide. C'est une fonction qui dépend de la position à l'intérieur du volume et du temps $t$.
    - $V$ le vecteur vitesse du fluide. Il dépend également de la position à l'intérieur du volume et du temps $t$.
    - $\frac{\partial}{\partial t} \rho$ nous donne la variation de la masse par unité de volume en fonction du temps
    - $\nabla (\rho V)$ est le flux de masse. Il nous indique comment la masse se déplace et se redistribue dans le volume
    
    Dans cette équation, nous pouvons voir que la variation de la masse doit être égale au flux de masse du fluide. Cela signifie que la masse du fluide ne peut être ni créée, ni détruite, mais qu'elle se déplace dans le fluide.

2. Équation de la quantité de mouvement
    
    L'équation de la quantité de mouvement découle de la conservation de la quantité de mouvement de Newton appliquée à un fluide. La quantité de mouvement est représenté par la masse volumique multipliée par le vecteur vitesse.

    Ainsi, on a l'équation suivante:

    $$\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right) = - \nabla p  + \rho \cdot f $$

    avec:

    - $p$ la pression du fluide
    - $f$ les forces externes s'appliquant sur le fluide (comme la force de gravité)
    - $\rho \cdot f$ nous donne l'ensemble des forces externes s'appliquant par unité de volume
    - $\nabla \cdot \left(\rho V V^T \right)$ représente le changement de vitesse dû au mouvement du fluide
    - $\frac{\partial}{\partial t}(\rho V)$ est la variation temporelle de la quantité de mouvement 

    Dans cette équation, nous avons d'une part la variation temporelle de la quantité de mouvement plus la répartition de la quantité de mouvement dans le fluide, et de l'autre part la force résultant des variations de la pression plus les autres forces externes. On peut donc reconnaître la 2ème loi de Newtown disant que la quantité de mouvement est égal à la somme des forces.

3. Équation de l'énergie

    L'équation de l'énergie s'applique si on suppose que le liquide est adiabatique, c'est à dire que la chaleur n'est pas prise en compte.

    Voici la formule obtenue:

    $$\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V) = - \nabla \cdot (pV) + \rho g V$$

    avec:

    - $E$ l'énergie totale par unité de masse. On a $E = e + \frac{1}{2}|V|^2$
    - $\frac{\partial}{\partial t} \rho E$ est la variation temporelle de l'énergie par unité de volume.
    - $\nabla \cdot (\rho E V)$ nous donne le flux d'énergie à travers le fluide, donc comment l'énergie est transportée dans le fluide
    - $- \nabla \cdot (pV)$ est le travail de la pression sur le fluide
    - $\rho f V$ est le travail des forces extérieures sur le fluide

    Dans cette équation, nous pouvons reconnaître d'une part la somme entre la variation et le flux d'énergie, et d'autre part la somme du travail des forces s'exerçant sur le fluide. Nous pouvons reconnaître le principe de conservation d'énergie: la somme du travail des forces est égal à l'énergie du fluide...

### Poubelle ??? 



Soit un volume $V$ ($m^3$) et $\rho$ la densité volumique du fluide ($kg \cdot m^{-3}$).

La densité volumique du fluide dépend de la position à l'intérieur du volume $V$ et du temps $t$.

Soit $x$ représente un vecteur dans l'espace.

La masse volumique peut donc s'exprimer comme:
$$
m(t) = \int_{V} \rho(x, t) dV
$$

Donc le taux de changement de la masse au cours du temps est donnée par:

$$
\frac{\partial}{\partial t} m(t)
$$

Soit une surface $s$ 2 dimensionnelle orientée vers l'extérieur du volume $V$

Le flux de particules possédant une vitesse $v$, s'écoulant à travers la surface $s$ sur une distance $\partial V$ est donc donné par:
(la multiplication $\rho v$ nous donne un champ vectoriel: cela nous donne un vecteur à chaque point de l'espace car $\rho$ est une fonction dépendant de la position dans l'espace et $v$ également)

$$
\int_{\partial V} \rho \cdot v \cdot s
$$

Selon le théorème de divergence, on a égalité entre l'intégrale de la divergence d'un champ vectoriel sur un volume $V$ et l'intégrale du flux de ce champ vectoriel à travers une surface fermée d'un volume $V$.

On a donc:

$$
\int_{\partial V} \rho \cdot v \cdot s = \int_{V} \nabla \cdot (\rho v) dV
$$

Dans notre cas, la divergence $\nabla \cdot (\rho v)$ va mesurer la variation de la densité dans le volume $V$.

Donc, comme nous avons conservation de masse, alors cela signifie que le taux de variation de la masse doit être égal au flux entrant ou sortant du volume. Dans notre cas, comme on a défini $s$ comme étant orientée vers l'extérieur du volume $V$, on a calculé le flux dans une direction sortante du volume. On a donc:

$$
\frac{\partial}{\partial t} m(t) = - \int_{V} \nabla \cdot (\rho v) dV
$$
$$
\Leftrightarrow \int_{V} \left( \frac{\partial}{\partial t} \rho + \nabla \cdot (\rho v)\right) dV = 0
$$
$$
\Leftrightarrow \frac{\partial}{\partial t} \rho + \nabla \cdot (\rho v) = 0
$$

Ainsi, on a notre équation de continuité.

## Équation de conservation de l'énergie
