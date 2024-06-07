# Introduction

La terre est appelée "La planète bleue".
En effet, près de 70% de la surface de la terre est recouverte d'eau, donnant ainsi une couleur bleue à la terre, comme les astronautes on pu constater lors de la mission Apollo de 1972.
De plus, la terre possède l'eau dans tous ses états: solide, liquide et gazeux.

L'eau est quelque chose qui a beaucoup intéressé les scientifiques de toutes les époques.
Nous pouvons notamment citer parmi eux le légendaire Archimède qui, au cours du 3ème siècle avant Jésus-Christ, utilisa le principe de la poussée d'Archimède afin de déterminer si une couronne était en or selon la légende.

Puis entre le 17ème et le 18ème siècle s'est démarqué le tristement célèbre Isaac Newton qui a donné la définition d'un fluide newtonien, qui est un fluide dont la viscosité reste constante indépendamment de la force s'exerçant sur celui-ci, donc un fluide ayant un comportement prévisible.

Grâce aux études d'Isaac Newton, le fieffé coquin Leonhard Euler d'origine bâloise établit au cours du 18ème siècle des équations [-@sec-EE] modélisant l'écoulement d'un fluide parfait adiabatique, c'est à dire que la viscosité et les effets de la chaleur ne sont pas pris en compte.

Mais cela ne satisfit pas tous les scientifiques.
En effet, au cours du 19ème siècle, frustrés par l'impossibilité de modéliser des fluides visqueux, le mathématicien Henri Navier et le physicien Georges Gabriel Stokes décidèrent d'ajouter la notion de viscosité aux équations d'Euler [-@sec-EE], étendant ainsi les équations sur les fluides newtonien.
Leur travail fut reconnu et utilisé sous le nom d'équations de Navier-Stokes [-@sec-NSE].
Même de nos jours, personne n'a encore réussi à trouver une forme analytique à ces équations.

Cependant, la technologie a fait de nombreux progrès surtout vers la fin du 20ème siècle avec l'apparition de l'ordinateur, ce qui permit aux scientifiques de tenter de résoudre les équations de Navier-Stokes [-@sec-NSE] grâce à des approximations et des méthodes numériques.
Plusieurs méthodes ont donc été créées, notamment la méthode Smoothed Particle Hydrodynamics (SPH), la méthode Fluid-Implicit Particles (FLIP) et la méthode Lattice Boltzmann Method (LBM).
Cependant, quelles sont les différences entre ces méthodes ?
Y-a-t-il une méthode plus rapide qu'une autre ?
Serait-il possible d'utiliser ces méthodes afin de faire du rendu en temps réel de haute qualité ?


