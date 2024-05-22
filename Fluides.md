---
title: Mécanique des fluides
author: Michel Jean Joseph Donnet
date: \today
---

\newpage
# Introduction

Un fluide est composé de nombreuses particules, c'est à dire des molécules ou des atomes.
À la différence d'un solide, un fluide est complètement déformable.

Il y a plusieurs types de fluide, notamment:

- les gaz: ce sont des fluides composés de particules isolées mouvant en toute liberté et pouvant entrer en collision.
- les liquides: ce sont des fluides composés de particules liées entre elles par des liaisons faibles, comme les liaisons hydrogène.
Les particules ne peuvent donc pas se mouvoir en toute liberté, et lorsqu'une particule bouge, elle exerce une influence sur les autres particules liées à elle.

# Bibliographie

Euler s'est intéressé à la mécanique des fluides et a trouvé des équations décrivant l'écoulement d'un fluide adiabatique newtonien, c'est à dire d'un fluide ayant un comportement normal, et où la chaleur est négligée.
Cependant, ses équations ne prennent pas en compte la viscosité du fluide.

C'est pourquoi, au XIX siècle, Henri Navier a introduit la notion de viscosité aux équations d'Euler, et avec Georges Gabriel Stokes, ils ont défini les équations de Navier-Stokes décrivant l'écoulement d'un fluide newtonien.
Un fluide newtonien est un fluide qui a un comportement normal, c'est à dire que la vitesse de déformation du fluide est linéare suivant la contrainte appliquée sur ce fluide.

Ces équations de Navier-Stokes n'ont actuellement pas de solution analytique, mais des solutions numériques existent.

\newpage
# Modélisation des fluides

## Variables

(plutôt faire un tableau avec nom de variable, description, unité ?)

- $\rho$ la masse volumique du fluide. C'est une fonction qui dépend de la position à l'intérieur du volume et du temps $t$.
- $V$ le vecteur vitesse du fluide. Il dépend également de la position à l'intérieur du volume et du temps $t$.
- $p$ la pression du fluide
- $f$ les forces externes s'appliquant sur le fluide (comme la force de gravité)
- $E$ l'énergie totale par unité de masse. On a $E = e + \frac{1}{2}\lVert V \rVert^2$
- $e$ l'énergie interne par unité de masse
- $\Sigma$ la contrainte de viscosité du fluide
- $q$ le flux de chaleur causé par conduction thermique
- $q_{R}$ le flux de chaleur causé par rayonnement

## Équations d'Euler

Les équations d'Euler sont un ensemble d'équations décrivant l'écoulement d'un fluide non visqueux.
Voici les 3 équations d'Euler:

### Équation de continuité

L'équation de continuité se formule de la façon suivante:

$$\frac{\partial}{\partial t} \rho + \nabla (\rho V) = 0$$ {#eq:econt}

avec:
    
- $\frac{\partial}{\partial t} \rho$ nous donne la variation de la masse par unité de volume en fonction du temps
- $\nabla (\rho V)$ est le flux de masse. Il nous indique comment la masse se déplace et se redistribue dans le volume

Dans cette équation, nous pouvons voir que la variation de la masse doit être égale au flux de masse du fluide. Cela signifie que la masse du fluide suit le principe de conservation de la matière

### Équation de la quantité de mouvement
    
Voici l'équation de la quantité de mouvement:

$$\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right) = - \nabla p  + \rho \cdot f $$ {#eq:emouv}

avec:

- $\rho \cdot f$ nous donne l'ensemble des forces externes s'appliquant par unité de volume
- $\nabla \cdot \left(\rho V V^T \right)$ représente le changement de vitesse dû au mouvement du fluide
- $\frac{\partial}{\partial t}(\rho V)$ est la variation temporelle de la quantité de mouvement 

Dans cette équation, nous avons d'une part la variation temporelle de la quantité de mouvement plus la répartition de la quantité de mouvement dans le fluide, et de l'autre part la force résultant des variations de la pression plus les autres forces externes. On peut donc reconnaître la 2ème loi de Newton disant que la quantité de mouvement est égal à la somme des forces.

### Équation de l'énergie

Soit un liquide adiabatique, c'est à dire pour lequel la chaleur n'est pas prise en compte.

Voici l'équation de l'énergie:

$$\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V) = - \nabla \cdot (pV) + \rho g V$$ {#eq:eener}

avec:

- $\frac{\partial}{\partial t} \rho E$ est la variation temporelle de l'énergie par unité de volume.
- $\nabla \cdot (\rho E V)$ nous donne le flux d'énergie à travers le fluide, donc comment l'énergie est transportée dans le fluide
- $- \nabla \cdot (pV)$ est le travail de la pression sur le fluide
- $\rho f V$ est le travail des forces extérieures sur le fluide

Dans cette équation, il y a d'une part la somme entre la variation et le flux d'énergie, et d'autre part la somme du travail des forces s'exerçant sur le fluide. Cela découle du principe de conservation d'énergie: la somme du travail des forces est égale à l'énergie du fluide...

## Équations de Navier-Stokes

Les équations de Navier-Stokes sont basées sur les équations d'Euler.
Elles y ajoutent la notion de viscosité, qui représente les forces de friction interne au fluide.
Elles permettent donc de modéliser des fluides réels visqueux à la différence des équations d'Euler qui modélisent les fluides parfaits.

Voici les équations de Navier-Stokes:

### Équation de continuité

Celle-ci ne diffère pas de l'équation de continuité d'Euler (@eq:econt).
Ceci semble normal, car la masse du fluide, même dans un fluide visqueux, ne peut toujours pas être créée ni détruite, et suit toujours le principe de conservation de la matière.

### Équation de la quantité de mouvement

Voici l'équation de la quantité de mouvement de Navier-Stokes:

$$
\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right)
= - \nabla p  + \nabla \Sigma +  \rho \cdot f
$$ {#eq:nmouv}

- $\nabla \Sigma$ est la force exerçée par la viscosité du fluide

Dans cette équation, la force exercée par la viscosité a été ajoutée à la somme des forces de l'équation (@eq:emouv) d'Euler.
Ainsi, l'équation (@eq:nmouv) suit toujours la 2ème loi de Newton

### Équation de l'énergie

Voici l'équation de l'énergie de Navier-Stokes:

$$
\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V)
= - \nabla \cdot (pV) + \nabla \cdot \Sigma V + \rho f V + \nabla \cdot q + \nabla \cdot q_{R}
$$ {#eq:nener}

- $\nabla \cdot \Sigma V$ est le travail de la viscosité du fluide
- $\nabla \cdot q + \nabla \cdot q_{R}$ est le travail de la chaleur sur le fluide

L'équation de l'énergie de Navier-Stokes (@eq:nener) ajoute à l'équation d'Euler (@eq:eener) le travail de la viscosité et de la chaleur sur le fluide.
Ainsi, les fluides non adiabatiques sont également pris en compte par cette équation.
