# Mécanique des fluides {#sec-meca}

Un fluide est composé de nombreuses particules, qui peuvent autant être des atomes que des ions ou encore des molécules, qui sont des atomes liés entre eux par des liaisons fortes ou covalentes.
À la différence d'un solide, un fluide est complètement déformable.

Il existe différent types de fluides, notamment:

- les gaz: ce sont des fluides composés de particules isolées mouvant en toute liberté et pouvant entrer en collision.
- les liquides: ce sont des fluides composés de particules liées entre elles par des liaisons faibles, comme les liaisons hydrogène.
Les particules ne peuvent donc pas se mouvoir en toute liberté, et lorsqu'une particule bouge, elle exerce une influence sur les autres particules liées à elle.

## Variables

- $\rho$ la masse volumique du fluide. C'est une fonction qui dépend de la position à l'intérieur du volume et du temps $t$.
- $V$ le vecteur vitesse du fluide. Il dépend également de la position à l'intérieur du volume et du temps $t$.
- $p$ la pression du fluide
- $f$ les forces externes s'appliquant sur le fluide (comme la force de gravité)
- $E$ l'énergie totale par unité de masse. On a $E = e + \frac{1}{2}\lVert V \rVert^2$
- $e$ l'énergie interne par unité de masse
- $\Sigma$ la contrainte de viscosité du fluide
- $q$ le flux de chaleur causé par conduction thermique
- $q_{R}$ le flux de chaleur causé par rayonnement
- $m$ la masse des particules

## Équations d'Euler {#sec-EE}

Les équations d'Euler sont un ensemble d'équations décrivant l'écoulement d'un fluide non visqueux.
Voici les 3 équations d'Euler:

### Équation de continuité

L'équation de continuité se formule de la façon suivante:

$$\frac{\partial}{\partial t} \rho + \nabla (\rho V) = 0$$ {#eq-econt}

avec:
    
- $\frac{\partial}{\partial t} \rho$ nous donne la variation de la masse par unité de volume en fonction du temps
- $\nabla (\rho V)$ est le flux de masse. Il nous indique comment la masse se déplace et se redistribue dans le volume

Dans cette équation, nous pouvons voir que la variation de la masse doit être égale au flux de masse du fluide. Cela signifie que la masse du fluide suit le principe de conservation de la matière

### Équation de la quantité de mouvement
    
Voici l'équation de la quantité de mouvement:

$$\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right) = - \nabla p  + \rho \cdot f $$ {#eq-emouv}

avec:

- $\rho \cdot f$ nous donne l'ensemble des forces externes s'appliquant par unité de volume
- $\nabla \cdot \left(\rho V V^T \right)$ représente le changement de vitesse dû au mouvement du fluide
- $\frac{\partial}{\partial t}(\rho V)$ est la variation temporelle de la quantité de mouvement 

Dans cette équation, nous avons d'une part la variation temporelle de la quantité de mouvement plus la répartition de la quantité de mouvement dans le fluide, et de l'autre part la force résultant des variations de la pression plus les autres forces externes. On peut donc reconnaître la 2ème loi de Newton disant que la quantité de mouvement est égal à la somme des forces.

### Équation de l'énergie

Soit un liquide adiabatique, c'est à dire pour lequel la chaleur n'est pas prise en compte.

Voici l'équation de l'énergie:

$$\frac{\partial}{\partial t} \rho E + \nabla \cdot (\rho E V) = - \nabla \cdot (pV) + \rho g V$$ {#eq-eener}

avec:

- $\frac{\partial}{\partial t} \rho E$ est la variation temporelle de l'énergie par unité de volume.
- $\nabla \cdot (\rho E V)$ nous donne le flux d'énergie à travers le fluide, donc comment l'énergie est transportée dans le fluide
- $- \nabla \cdot (pV)$ est le travail de la pression sur le fluide
- $\rho f V$ est le travail des forces extérieures sur le fluide

Dans cette équation, il y a d'une part la somme entre la variation et le flux d'énergie, et d'autre part la somme du travail des forces s'exerçant sur le fluide. Cela découle du principe de conservation d'énergie: la somme du travail des forces est égale à l'énergie du fluide...

## Équations de Navier-Stokes {#sec-NSE}

Les équations de Navier-Stokes sont basées sur les équations d'Euler.
Elles y ajoutent la notion de viscosité, qui représente les forces de friction interne au fluide.
Elles permettent donc de modéliser des fluides réels visqueux à la différence des équations d'Euler qui modélisent les fluides parfaits.

Voici les équations de Navier-Stokes:

### Équation de continuité

Celle-ci ne diffère pas de l'équation de continuité d'Euler [-@eq-econt].
Ceci semble normal, car la masse du fluide, même dans un fluide visqueux, ne peut toujours pas être créée ni détruite, et suit toujours le principe de conservation de la matière.

### Équation de la quantité de mouvement

Voici l'équation de la quantité de mouvement de Navier-Stokes:

$$
\frac{\partial}{\partial t}(\rho V) + \nabla \cdot \left(\rho V V^T \right)
= - \nabla p  + \nabla \Sigma +  \rho \cdot f
$$ {#eq-nmouv}

- $\nabla \Sigma$ est la force exerçée par la viscosité du fluide

Dans cette équation, la force exercée par la viscosité a été ajoutée à la somme des forces de l'équation [-@eq-emouv] d'Euler.
Ainsi, l'équation [-@eq-nmouv] suit toujours la 2ème loi de Newton

### Équation de l'énergie

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

## Équation de Boltzmann {#sec-BE}

Les équations de Boltzmann sont utiles pour décrire le comportement de systèmes composés de particules, tel que les gaz ou les liquides.

Dans les équations de Boltzmann, chaque particule composant le système possède une vitesse et une position qui varient dans le temps en fonction des mouvements de la particule.

La fonction $f(x, v, t)$ donne alors la densité de probabilité de trouver une particule à une position $x$ avec une vitesse $v$ à un temps $t$.

L'objectif des équations de Boltzmann est donc de déterminer comment évolue cette fonction de densité de probabilité $f$ au cours du temps.

La fonction de distribution évolue suivant les forces extérieures s'appliquant sur les particules, les collisions entre les particules et la diffusion des particules, qui tend à avoir la même concentration de particules dans tout le système.
C'est pourquoi, la variation de la fonction de distribution peut s'écrire comme dans l'équation [-@eq-dist].

$$
\frac{\partial f}{\partial t} = \left(\frac{\partial f}{\partial t} \right)_{force} + \left(\frac{\partial f}{\partial t} \right)_{diff} + \left(\frac{\partial f}{\partial t}\right)_{coll}
$$ {#eq-dist}

### Collisions négligées

Supposons qu'il n'y a pas de collisions entre les particules.
Cela signifie que les particules n'interagissent pas entre elles, ce qui entraîne aucune modification de la fonction de distribution $f$.
Ainsi, la dérivée totale de $f$ par rapport au temps $t$ est nulle: $\frac{df}{dt} = 0$ car $f$ ne varie pas dans le temps.

Grâce aux règles de chaînage, il est possible de trouver la dérivée totale de $f$ par rapport au temps $t$, comme montrée dans l'équation [-@eq-nocol].

$$
\begin{aligned}
\frac{df}{dt}
&= (\frac{dt}{dt} \cdot \frac{\partial}{\partial t} + \frac{dx}{dt}\cdot \frac{\partial}{\partial x} + \frac{dv}{dt} \cdot \frac{\partial}{\partial v}) f(x, v, t) \\
&= (\frac{\partial}{\partial t} + v \cdot \frac{\partial}{\partial x} + \frac{F}{m} \cdot \frac{\partial}{\partial v}) f(x, v, t) \\
&= \frac{\partial f}{\partial t} + v \nabla_{x} f + \frac{F}{m} \nabla_{v} f
\end{aligned}
$$ {#eq-nocol}

Dans l'équation [-@eq-nocol], le terme $\frac{\partial f}{\partial t}$ montre le changement de $f$ à vitesse et position constante, le terme $v \nabla_{x} f$ représente le changement de $f$ dû aux déplacements des particules, et le terme $\frac{F}{m} \nabla_{v} f$ représente le changement de $f$ dû aux forces extérieures, tel que la gravité, s'appliquant sur les particules.
Ainsi, les déplacements des particules sont uniquement dûe aux forces extérieures et à la diffusion des particules, ce qui donne en combinant l'équation [-@eq-nocol] avec le fait que $f$ ne varie pas en fonction du temps l'équation [-@eq-nocol2].

$$
\frac{\partial f}{\partial t} + v \nabla_{x} f + \frac{F}{m} \nabla_{v} f = 0
$$ {#eq-nocol2}

### Collisions non négligées

Cependant, dans la réalité, des collisions existent entre les particules.
Comme les particules interagissent entre elles, la fonction de distribution va subir des modifications en fonction des collisions.
C'est pourquoi la dérivée totale de $f$ par rapport à $t$ ne sera plus égal à $0$, mais au terme $\left(\frac{\partial f}{\partial t}\right)_{coll}$ qui capture l'effet des interactions entre les particules, ce qui donne la modification de l'équation [-@eq-nocol2] en l'équation [-@eq-col].

$$
\frac{\partial f}{\partial t} + v \nabla_{x} f + \frac{F}{m} \nabla_{v} f = \left(\frac{\partial f}{\partial t}\right)_{coll}
$$ {#eq-col}

L'équation [-@eq-col] est appelée équation de Boltzmann. Il ne reste plus qu'à définir le terme de collision $\left(\frac{\partial f}{\partial t}\right)_{coll}$, ce qui est une chose complexe qui ne va pas être traîtée ici.

