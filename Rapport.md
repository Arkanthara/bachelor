---
title: Comparaison entre méthodes de simulation de fluides
author: Michel Jean Joseph Donnet
date: \today
format:
    pdf:
        cite-method: biblatex
output-file: Rapport.pdf
toc: true
lang: fr-FR
documentclass: report
top-level-division: chapter
numbersections: true
bibliography: references.bib
header-includes:
    - \usepackage[margin=2.5cm,a4paper]{geometry}
    - \usepackage{fancyhdr}
    - \usepackage{lastpage}
    - \usepackage{hyperref}
    - \usepackage{graphicx}
    - \pagestyle{fancy}
    - \fancyhf{}
    - \lhead{\nouppercase{\leftmark}}
    - \rhead{Université de Genève}
    - \lfoot{\put(0, -30) {\includegraphics[width=4cm]{./unige.jpg}}}
    - \rfoot{Page \thepage / \pageref{LastPage}}
    - \fancypagestyle{plain}{
        \fancyhf{}
        \renewcommand{\headrulewidth}{0pt}
        \lfoot{\put(0, -30) {\includegraphics[width=4cm]{./unige.jpg}}}
        \rfoot{Page \thepage / \pageref{LastPage}}
        }
---

# Introduction

La terre est appelée "La planète bleue".
En effet, près de 70% de la surface de la terre est recouverte d'eau, donnant ainsi une couleur bleue à la terre, comme les astronautes on pu constater lors de la mission Apollo de 1972.
De plus, la terre possède l'eau dans tous ses états: solide, liquide et gazeux.

L'eau est quelque chose qui a beaucoup intéressé les scientifiques de toutes les époques.
Nous pouvons notamment citer parmi eux le légendaire Archimède qui, au cours du 3ème siècle avant Jésus-Christ, utilisa le principe de la poussée d'Archimède afin de déterminer si une couronne était en or selon la légende.

Puis entre le 17ème et le 18ème siècle s'est démarqué le tristement célèbre Isaac Newton qui a donné la définition d'un fluide newtonien, qui est un fluide dont la viscosité reste constante indépendamment de la force s'exerçant sur celui-ci, donc un fluide ayant un comportement prévisible.

Grâce aux études d'Isaac Newton, le fieffé coquin Leonhard Euler d'origine bâloise établit au cours du 18ème siècle des équations modélisant l'écoulement d'un fluide parfait adiabatique, c'est à dire que la viscosité et les effets de la chaleur ne sont pas pris en compte.

Mais cela ne satisfit pas tous les scientifiques.
En effet, au cours du 19ème siècle, frustrés par l'impossibilité de modéliser des fluides visqueux, le mathématicien Henri Navier et le physicien Georges Gabriel Stokes décidèrent d'ajouter la notion de viscosité aux équations d'Euler, étendant ainsi les équations sur les fluides newtonien.
Leur travail fut reconnu et utilisé sous le nom d'équations de Navier-Stokes.
Même de nos jours, personne n'a encore réussi à trouver une forme analytique à ces équations.

Cependant, la technologie a fait de nombreux progrès surtout vers la fin du 20ème siècle avec l'apparition de l'ordinateur, ce qui permit aux scientifiques de tenter de résoudre les équations de Navier-Stokes grâce à des approximations et des méthodes numériques.
Plusieurs méthodes ont donc été créées, notamment la méthode Smoothed Particle Hydrodynamics (SPH), la méthode Fluid-Implicit Particles (FLIP) et la méthode Lattice Boltzmann Method (LBM).
Cependant, quelles sont les différences entre ces méthodes ?
Y-a-t-il une méthode plus rapide qu'une autre ?
Serait-il possible d'utiliser ces méthodes afin de faire du rendu en temps réel de haute qualité ?


# Méthodes de simulation de fluides

## Mécanique des fluides

Un fluide est composé de nombreuses particules.
À la différence d'un solide, un fluide est complètement déformable.

Il existe différent types de fluides, notamment:

- les gaz: ce sont des fluides composés de particules isolées mouvant en toute liberté et pouvant entrer en collision.
- les liquides: ce sont des fluides composés de particules liées entre elles par des liaisons faibles, comme les liaisons hydrogène.
Les particules ne peuvent donc pas se mouvoir en toute liberté, et lorsqu'une particule bouge, elle exerce une influence sur les autres particules liées à elle.

### Variables

- $\rho$ la masse volumique du fluide. C'est une fonction qui dépend de la position à l'intérieur du volume et du temps $t$.
- $V$ le vecteur vitesse du fluide. Il dépend également de la position à l'intérieur du volume et du temps $t$.
- $p$ la pression du fluide
- $f$ les forces externes s'appliquant sur le fluide (comme la force de gravité)
- $E$ l'énergie totale par unité de masse. On a $E = e + \frac{1}{2}\lVert V \rVert^2$
- $e$ l'énergie interne par unité de masse
- $\Sigma$ la contrainte de viscosité du fluide
- $q$ le flux de chaleur causé par conduction thermique
- $q_{R}$ le flux de chaleur causé par rayonnement

### Équations d'Euler

Les équations d'Euler sont un ensemble d'équations décrivant l'écoulement d'un fluide non visqueux.
Voici les 3 équations d'Euler:

#### Équation de continuité

L'équation de continuité se formule de la façon suivante:

$$\frac{\partial}{\partial t} \rho + \nabla (\rho V) = 0$$ {#eq-econt}

avec:
    
- $\frac{\partial}{\partial t} \rho$ nous donne la variation de la masse par unité de volume en fonction du temps
- $\nabla (\rho V)$ est le flux de masse. Il nous indique comment la masse se déplace et se redistribue dans le volume

Dans cette équation, nous pouvons voir que la variation de la masse doit être égale au flux de masse du fluide. Cela signifie que la masse du fluide suit le principe de conservation de la matière

#### Équation de la quantité de mouvement
    
Voici l'équation de la quantité de mouvement:

$$\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right) = - \nabla p  + \rho \cdot f $$ {#eq-emouv}

avec:

- $\rho \cdot f$ nous donne l'ensemble des forces externes s'appliquant par unité de volume
- $\nabla \cdot \left(\rho V V^T \right)$ représente le changement de vitesse dû au mouvement du fluide
- $\frac{\partial}{\partial t}(\rho V)$ est la variation temporelle de la quantité de mouvement 

Dans cette équation, nous avons d'une part la variation temporelle de la quantité de mouvement plus la répartition de la quantité de mouvement dans le fluide, et de l'autre part la force résultant des variations de la pression plus les autres forces externes. On peut donc reconnaître la 2ème loi de Newton disant que la quantité de mouvement est égal à la somme des forces.

#### Équation de l'énergie

Soit un liquide adiabatique, c'est à dire pour lequel la chaleur n'est pas prise en compte.

Voici l'équation de l'énergie:

$$\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V) = - \nabla \cdot (pV) + \rho g V$$ {#eq-eener}

avec:

- $\frac{\partial}{\partial t} \rho E$ est la variation temporelle de l'énergie par unité de volume.
- $\nabla \cdot (\rho E V)$ nous donne le flux d'énergie à travers le fluide, donc comment l'énergie est transportée dans le fluide
- $- \nabla \cdot (pV)$ est le travail de la pression sur le fluide
- $\rho f V$ est le travail des forces extérieures sur le fluide

Dans cette équation, il y a d'une part la somme entre la variation et le flux d'énergie, et d'autre part la somme du travail des forces s'exerçant sur le fluide. Cela découle du principe de conservation d'énergie: la somme du travail des forces est égale à l'énergie du fluide...

### Équations de Navier-Stokes

Les équations de Navier-Stokes sont basées sur les équations d'Euler.
Elles y ajoutent la notion de viscosité, qui représente les forces de friction interne au fluide.
Elles permettent donc de modéliser des fluides réels visqueux à la différence des équations d'Euler qui modélisent les fluides parfaits.

Voici les équations de Navier-Stokes:

#### Équation de continuité

Celle-ci ne diffère pas de l'équation de continuité d'Euler [-@eq-econt].
Ceci semble normal, car la masse du fluide, même dans un fluide visqueux, ne peut toujours pas être créée ni détruite, et suit toujours le principe de conservation de la matière.

#### Équation de la quantité de mouvement

Voici l'équation de la quantité de mouvement de Navier-Stokes:

$$
\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right)
= - \nabla p  + \nabla \Sigma +  \rho \cdot f
$$ {#eq-nmouv}

- $\nabla \Sigma$ est la force exerçée par la viscosité du fluide

Dans cette équation, la force exercée par la viscosité a été ajoutée à la somme des forces de l'équation [-@eq-emouv] d'Euler.
Ainsi, l'équation [-@eq-nmouv] suit toujours la 2ème loi de Newton

#### Équation de l'énergie

Voici l'équation de l'énergie de Navier-Stokes:

$$
\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V)
= - \nabla \cdot (pV) + \nabla \cdot \Sigma V + \rho f V + \nabla \cdot q + \nabla \cdot q_{R}
$$ {#eq-nener}

- $\nabla \cdot \Sigma V$ est le travail de la viscosité du fluide
- $\nabla \cdot q + \nabla \cdot q_{R}$ est le travail de la chaleur sur le fluide

L'équation de l'énergie de Navier-Stokes [-@eq-nener] ajoute à l'équation d'Euler [-@eq-eener] le travail de la viscosité et de la chaleur sur le fluide.
Ainsi, les fluides non adiabatiques sont également pris en compte par cette équation.

Dans la plupart des cas, l'équation de l'énergie n'est pas prise en compte lors de la simulation de fluides notamment à cause de la complexité du calcul.

## Méthode SPH

La méthode Smoothed Particle Hydrodynamics (SPH) a été inventée en 1977 par trois scientifiques Gingold, Lucy et Monaghan afin de simuler des phénomènes astrophysiques, tel que la formation et l'évolution d'une étoile ou d'une galaxie.
Les équations de la mécanique des fluides peuvent effectivement servir à décrire ce genre de phénomènes astrophysiques car il s'agit de gaz ou d'une multitude de corps évoluant d'une manière similaire à un liquide ou un gaz.

La méthode SPH s'est ensuite développée dans le domaine de la mécanique des fluides ou elle a servit notamment à modéliser non seulement des fluides compressibles et incompressibles, mais également des phénomènes thermiques et magnétiques.

Puis vers 1990, la méthode SPH a été étendue à la mécanique des structures afin de simuler par exemple des impact à forte vitesse ou des déchirures de matériaux grâce notamment au travail de Libersky et Petschek (citation ici).

De nos jour, la méthode SPH est encore utilisée dans la mécanique des fluides, mais également pour simuler des impacts haute vitesse, des fragmentations ou encore des explosions, si bien que le terme Hydrodynamics n'est plus adapté.
Cependant, pour des raisons historiques, on conserve le terme Hydrodynamics.

### Caractéristiques

test de citation: @Fabien 
