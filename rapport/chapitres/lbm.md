---
title: notes
author: Michel
format: pdf
---

## Méthode LBM

La méthode Lattice Boltzman (LBM) est issue d'une autre méthode appelée lattice gaz automata (LGA)

### Principes de base

La méthode LBM représente le fluide comme un ensemble de particules qui elles-mêmes représentent un ensemble de molécules.
Elle est utilisée pour étudier le comportement de mésoscale fluides. (De l'ordre de $10^{-9}$ à $10^{-6}$ mètres)

Comme on représente non pas chaque molécule mais des groupes de molécule, la physique utilisée est probabilistique.

Les équations alors utilisées ne sont pas les équations de Navier Stokes, mais les équations de Boltzmann.

La méthode LBM utilise les équations de Boltzmann, mais n'est pas un solveur pour ces équations...

On peut représenter l'espace comme un ensemble de molécules dans une grille, et on est intéressé de savoir comment les molécules vont entrer en collision...

On veut connaître où vont les molécules en moyenne et quelle est leur distribution dans l'espace de vitesse

Dans les équations de Navier-Stokes, on a le temps et la position comme variable, mais dans la méthode LBM, on prend également la vélocité des molécules comme une variable.

On définit alors $\xi$ comme dans l'équation [-@eq-xi] où $\xi$ est la vélocité moléculaire qui donne le changement de position de la molécule en fonction du temps

On veut savoir combien de molécules dans une cellule se déplacent dans une direction à un temps donné.

his enable continuum level descriptions on a kinetic level where molecules are behaving kinetically
Cela permet des descriptions au niveau du continuum à un niveau cinétique où les molécules se comportent de manière cinétique.
Cela permet d'avoir un 

$$
\xi = \frac{dx}{dt}
$$ {#eq-xi}

$$
f(\xi, x, t)
$$
Donne le nombre de molécules que l'on a à un point donné à un temps donné qui bougent dans une direction donnée avec une vitesse donnée.

Cette distribution $f$ est normalisée de telle façon que si on intègre sur la vitesse et la position, on obtient la masse du système:

$$
\int d^3 \xi \int d^3 x f(\xi, x, t) = M(t)
$$

Et si on intègre sur seulement la vélocité, on obtient la densité car cela correspond à seulement prendre toutes les molécules, sans tenir compte de leur vitesse.

$$
\int d^3 \xi f(\xi, x, t) = \rho(x, t)
$$

Si on calcule le premier moment de la distribution, donc si on multiplie par la vitesse des molécules et qu'ensuite on intègre en fonction de la vitesse, on obtient le moment de densité du système pour une cellule donnée.

$$
\int d^3 \xi \xi \cdot f(\xi, x, t) = \rho u(x, t)
$$

On peut faire la même chose pour obtenir la pression, mais c'est plus compliqué.

On est intéressé par la densité et le moment de densité car ces variables apparraissent dans les équations de Navier-Stokes.

$f$ contient toutes les propriétés locales du fluide qui nous intéressent.
Si on va au niveau des équations de Navier Stokes, on est uniquement intéressé par obtenir les moments de $f$, ce qui signifie le moment d'ordre 0 qui est la densité et le moment d'ordre 1 qui est le moment de densité

On veut trouver une équation qui décrit comment $f$ évolue dans le temps

On peut utiliser la règle de chainage et obtenir:

$$
\begin{aligned}
\frac{df(\xi, x, t)}{dt}
&= (\frac{\partial}{\partial t} + \frac{dx}{dt}\cdot \frac{\partial}{\partial x} + \frac{d\xi}{dt} \cdot \frac{\partial}{\partial \xi}) f(\xi, x, t) \\
&= (\frac{\partial}{\partial t} + \xi \cdot \frac{\partial}{\partial x} + \frac{f}{\rho} \cdot \frac{\partial}{\partial \xi}) f(\xi, x, t) \\
&= \Omega (f)
\end{aligned}
$$

terme 1: dérivée parielle en fonction du temps
terme 2: gradient spacial
terme 3: le changement de vélocité est l'accélération et l'accélération des particules est relié à la force agissant sur les particules

mais dans la réalité, les particules entrent en collision, ce qui va faire que la fonction de distribution va changer non seulement à cause des termes présent dans sa dérivée, mais également parce que les particules entrent en collision, et toutes ces contributions qui ne sont pas capturées par la dérivée sont collectées par la partie droite qui donne la déviation de 0 et qui est appelée l'opérateur de collision $\Omega$.

On peut retrouver les équations de Navier Stokes à partir des équations de Boltzmann avec certaunes conditions et limites.

Navier Stokes vs boltzmann: Navier Stokes plus simple car possède seulement les données en fonction du temps et de la position: la vitesse $\xi$ n'est pas prise en compte...

Les équations de Boltzman n'ont pas de détails microscopiques

La fonction de distribution va être déformée par l'opérateur de collision.
On ne prend pas en compte chaque collision, sinon le calcul devient monstrueux, mais on peut estimer que au bout d'un moment, on arrive à un équilibre. On appelle $f^{eq}$ la distribution équilibrée.
On estime alors que l'on peut modéliser la relaxation vers $f^{eq}$ à partir d'un état non équilibré $f$ par un modèle Bhatnagar-Gross-Krook (BGK):

$$
\Omega (f) =- \frac{1}{\tau} (f - f^{eq})
$$
avec $\tau$ le temps de relaxation

C'est une grosse simplification, mais cela marche tout de même avec les équations de Boltzmann dans une simulation numérique, et cette simplification est suffisante pour retrouver le comportement des équations de Navier-Stokes.

On définit
- $\xi$ la vélocité absolue de nos molécules
- $u = \int d^3 \xi \xi \cdot \frac{f(\xi, x, t)}{\rho}$ est la vélocité moyenne du fluide dans la cellule. C'est la vélocité moyenne des molécules dans une surface donnée. C'est la vitesse macroscopique du liquide à un point donné
- $v = \xi - u$ comme la vitesse du centre de masse de ces molécules. Il donne comment les molécules sont distribuées individuellement dans l'espace des vitesses autour de la vélocité u.

On utilise communément $u$ et $v$ et non pas $\xi$.

Les collisions doivent conserver la masse (densité), le moment (vélocité) (3ème loi de newton) et l'énergie (température) (collisions sont élastiques...)
La distribution d'équilibre $f^{eq}$ doit dépendre seulement de la densité $\rho$, la vitesse du centre de masse $v$ et de la température $T$. et elle doit être isotropique.
elle doit être isotrope, peu importe la direction de l'espace dans lequel nous regardons, elle ne peut donc dépendre que de la magnitude de v
On arrive après des dérivations à la fonction de distribution équilibrée [-@eq-eqdist]

$$
\begin{aligned}
f^{eq} (v, x, t) &= \rho \left(\frac{1}{2\pi RT}\right)^{3/2} e^{-\frac{|v|^2}{2RT}} \\
&= \rho \left(\frac{1}{2\pi RT}\right)^{3/2} e^{-\frac{|\xi - u|^2}{2RT}} \\
\end{aligned}
$${#eq-eqdist}

Qu'est ce qu'on a appris ?

- séparation dans le temps et dans l'espace
- remplacement des molécules par une fonction de distribution $f(v, x, t)$ (mesoscopic picture)
- Boltzmann équation: équation gouvernant la distribution $f$
- On a besoin de l'opérateur de collision $\Omega (f)$ qui est très complexe dans sa forme matématique
- On utilise un opérateur de collision simplifié grâce à BGK qui nous donne une distribution équilibrée $f^{eq}$
- On peut calculer la densité $\rho$, la vélocité $u$ et la pression $p$ macroscopique du fluide grâce aux moments de $f(v, x, t)$
- On peut retrouver les équations de Navier Stokes

we can use a navier stokes server that is not directly distretizing the navier-stokes equations but that is rooted in boltzmann theory
Nous pouvons utiliser un serveur de Navier-Stokes qui ne distord pas directement les équations de Navier-Stokes mais qui est enraciné dans la théorie de Boltzmann.

L'idée principale est d'utiliser les équations de Boltzmann pour résoudre les équations de Navier-Stokes, ce qui est possible grâce à Chapman-Enskog.

Nous allons simuler l'évolution de la fonction de densité $f$ plutôt que l'évolution de la vitesse et de la pression, ce qui nous intéresse normalement dans un fluide microscopique...

Pourquoi utiliser la méthode Boltzmann ?? En effet, il y a plus de variables, cela a l'air plus difficile...
On utilise cette méthode car elle s'avère plus pratique qu'une discrétisation des équations de Navier-Stokes.

On a donc à
- Discrétiser la fonction de distribution $f$
- Qu'est ce que la lattice boltzman equation (LBE)
- comment sont liés l'équation de Navier-stokes et l'équation de boltzmann ?

Espace: 
$x \rightarrow \Delta x$ (lattice). On prend l'espace et on le décompose en "small lattice nodes" et on résoud l'équation pour chaque noeud du treillis (ou de la lattice...)

Temps:
$t \rightarrow \Delta t$ qui est constant... Donc on résoud lattice boltzmann à un temps t, puis on avance de $\Delta t$.... On peut également faire le temps dynamiquement...

Vélocité:
$f(v, x, t) \rightarrow f_{i}(x, t)$ On discrétise $f$ en terme d'espace de vélocité en autorisant seulement un très petit nombre de directions possibles de direction et de vitesse. (Notation D2Q9: 9 vélocité possibles en 2d... D3Q19: 19 vélocité possibles en 3d)

Vélocité:

Ce que l'on fait est que l'on dit que si on a une molécule ou $f$ n'est pas réellement une molécule, mais un ensemble de molécules
Au lieu de dire $f$ décrit comment les molécules bougent dans toutes les directions, on dit que les molécules peuvent maintenant bouger seulement sur les axes primaires $x$, $y$, $z$ ou elles peuvent bouger sur les diagonales, et elles doivent se déplacer de telle sorte qu'en un pas de temps delta t, elles atteignent exactement l'un des noeuds de treillis voisins.
Donc la discrétisation de l'espace de vélocité est fait de telle sorte qu'il est parfaitement aligné avec la discrétisation temporelle et spacialle.

On doit donc remplacer les intégrales par des sommes finies qui n'ont que peu de termes comme 9 ou 19 plutôt que 1 million
Le mécanisme mathématique derrière cela est "Hermite expansion" que je ne vais pas expliquer.

$$(c_{i}) = \begin{bmatrix} 0 & 1 & 0 & -1 & 0 & 1 & -1 & -1 & 1 \\ 0 & 0 & 1 & 0 & -1 & 1 & 1 & -1 & -1\end{bmatrix} \frac{\Delta x}{\Delta t}$$
pour D2Q9....

Une fois que l'on a fait cela, on écrit $q$ différente population $f_{i}(x, t)$, une pour chaque $c_{i}$

On a donc:

$$
\sum_{i}^{q - 1} f_{i}(x, t) = \rho(x, t)
$$
et 
$$
\sum_{i}^{q - 1} c_{i} f_{i}(x, t) = \rho u(x, t)
$$

Au lieu de l'oppérateur de collision, on utilise l'approximation BGK et l'équation résultante sera la lattice boltzmann equation ou lattice bgk equation (lbgk)

$$
f_{i}(x + c_{i}\Delta t, t + \Delta t) - f_{i}(x, t) = -\frac{\Delta t}{\tau}(f_{i}(x, t) - f_{i}^{eq}(x, t) = \Omega_{i}
$$
avec

- $f_{i}(x + c_{i}\Delta t, t + \Delta t)  - f_{i}(x, t)$ une population $i$ donnée évaluée dans un point $x$ et un temps $t$ et sa contrepartie se sera déplacée de $c_{i} \times \Delta t$ où $c_{i}$ est la vitesse de la population.
- $-\frac{\Delta t}{\tau}(f_{i}(x, t) - f_{i}^{eq}(x, t)$ la distribution $f_{i}$ qui va se relaxer vers la distribution équilibrée $f_{i}^{eq}$ en un temps $\frac{\Delta t}{\tau}$

Ce qui nous donne si on réécrit cela:
$$
f_{i}(x + c_{i}\Delta t, t + \Delta t) = f_{i}(x, t) -\frac{\Delta t}{\tau}(f_{i}(x, t) - f_{i}^{eq}(x, t) = \Omega_{i}
$$

Le terme de relaxation nous donne un déplacement ou une redistribution de notre population, mais elle n'a pas encore bougé dans l'espace, et ensuite, on la propage vers les autres voisins.

Les avantages sont que les collisions sont locales et algébriques: c'est un algorithme très simple pour les collisions et la propagation est linéaire et exacte, ce qui signifie que l'on peut décomposer le lattice solveur en étape de collision et de propagation.

Dans Navier-Stokes, on a la notion de viscosité alors que dans Boltzmann, on a seulement un temps de relaxation.
On a ainsi la relation suivante:
$$
visc = c_{S}^2\left(\tau - \frac{\Delta t}{2}\right)
$$

avec la vitesse du son $c_{S}$ définie comme suit:
$$
c_{S} = \frac{1}{\sqrt{3}}\frac{\Delta x}{\Delta t}
$$

et $f_{i}^{eq}$ qui est une simplification de la distribution de Maxwell-Boltzmann défini comme suit:

$$
f_{i}^{eq} = w_{i} \rho \left(1 + \frac{c_{i} \cdot u}{c_{S}^2} + \frac{(c_{i} \cdot u)^2}{2c_{S}^4} - \frac{u \cdot u}{2c_{S}^2} \right)
$$
avec $w_{i}$ le poids d'une population dépendant de si la population se déplace le long des axes principaux ou diagonaux ou si elle reste sur place ( en effet, il peut changer de valeur suivant ces critères....)

Comment on fait ?

- Condition initiale. On connaît le $f_{i}$ initial. On peut donc calculer la densité et la vélocité par la somme des moments de $f$
- Ensuite, on calcule la distribution équilibrée $f^{eq}$ qui dépend uniquement de la densité et de la vélocité.
- Puis on peut calculer la distribution post collision $f_{i}^*$. Nos populations auront été redistribués dans l'espace de vélocité, mais n'auront pas bougé.
  On peut alors propager cela aux voisins: $f_{i}(x + c_{i}\Delta t, t + \Delta t) = f_{i}^*$.

Pourquoi ça marche ?

- On a une "lattice symetry and isotropy"
- On a la conservation de la masse et de la quantité de mouvement: $\sum_{i}\Omega_{i} = 0$ et $\sum_{i} c_{i}\Omega_{i} = 0$
- Les analyses de Champman-Enskog nous montre que ce que l'on a fait (donc que LBE) est suffisant pour retrouver le comportement de Navier-Stokes.

1. Avantages
   - C'est rapide car c'est une méthode explicite et linéaire en propagation
   - On n'a pas d'équation de poisson à résoudre (à la différence des équations de Navier-Stokes)
   - C'est une méthode locale exepté pour la propagation aux voisins
   - Facilement parallélisable (très scallable: linéaire en fonction du nombre de coeurs...)
   - Les géométries complexes peuvent être implémentées relativement facilement comparée aux autres méthodes

2. Désavantages
   - On ne peut simuler que des "small Knudsen numbers" et des "small Mach numbers"


Ce qu'on a appris

- Discrétiser la distribution $f$
- Discrétiser la vélocité $f(v, x, t) \rightarrow f_{i}(x, t)$
- Simple à implémenter
- $\tau$ détermine la viscosité du fluide
- la méthode est rapide, facilement parallélisable, et peut être utilisée pour résoudre des systèmes complexes de géométrie
- mais la méthode n'est pas faite pour simuler des high Knudsen ou high Mach numbers


Pour simuler des problèmes de différente taille, il faut bien définir les conditions aux bords...
Les conditions aux bords sont nécessaires non seulement mathématiquement, mais aussi physiquement.
En général, on a des approches non structurées (comme la méthode SPH), des approches structurées (comme la méthode LBM)
Il faut faire attention car si on ne s'occupe pas bien des conditions aux bords, le résultat sera mauvais...

La lattice boltzmann a un zoo pour les conditions aux bords car on a plus de variable que dans les équations de Navier-Stokes.
Par exemple, en 3d, on a 4 champs hydrodynamiques, on a la pression et on a la vélocité qui possède 3 composantes et le stress tensor $\sigma$ qui possède 6 composantes (le stress tensor est utilisé pour déterminer ce qui se passe aux bords du fluide....). Cependant, on a plus de populations...
On a 19 ou 27 populations, ce qui signifie que l'on a plus de liberté dans LBM que dans Navier-Stokes, mais que l'on a plus de conditions à imposer et à satisfaire...

D'une manière générale, on manipule des populations $f_{i}$.
Pour savoir ce qui se passe aux conditions, nous devons savoir ce qui vient depuis l'extérieur, donc on va se dire que l'on a un $f$ qui vient de l'extérieur, et on va essayer de déterminer ce qu'il devrait être.

De nombreuses personnes se sont penchés sur le problème de condition aux bords et ils ont déterminer de nombreuses conditions aux bords, ayant chacune leur avantage et leur désavantage.
On a notamment les Bounce-back methods (simple, interpolée, partiellement saturée), les Ghost methods (FH & MLS, GZS, Image-based) et les Immerse Boundary methods (Explicit, Direct forcing, other variants)

On peut par exemple définir pour Bounce-back methode que si on passe la frontière, on a $f_{i} \rightarrow f_{\hat{i}}$ avec $c_{\hat{i}} = - c_{i}$. Ainsi, on n'ajoute pas de nouvelles informations.
Cette méthode marche pour toute les conditions de bord en escalier, est extrêmement simple et ne possède pas d'équivalent dans les CFD (computationnal fluid dynamics)
mais elle n'est pas très précise, il y a des artéfacts numériques et si on bouge les bords, on aura des complications

Conditions de bord immersive (excellent article de Peskin en 2002 !) Un principe de base est que les frontières vont bouger avec le fluide. Cette méthode n'est pas une condition de bord, mais elle ne fait que mimer l'effet d'un bord.

Avantages: pas besoin d'inclure des conditions de bord réelles, l'effet sur le fluide est complètement inclus avec les forces externes, fonctionne pour des bords de n'importe quelle forme

Désavantages: impact sur la précision due à diffuse interface method, le fluide existe à l'intérieur des bords, plus difficile pour les conditions limites autres que l'absence de glissement...

Comme on n'a pas d'équation de poisson à résoudre, lbm est utile pour le calcul haute performance

Explications prise de cette vidéo: @Krueger2.
