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

Les équations d'Euler sont basés sur la conservation de la masse, de l'énergie et de la quantité de mouvement.


## Équation de continuité

Dans un système fermé (avec aucun échange avec l'extérieur), la masse du fluide ne peut ni être créée, ni être détruite.

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
