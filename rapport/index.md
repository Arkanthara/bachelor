# Introduction

La terre est appelée "La planète bleue".
En effet, près de 70% de la surface de la terre est recouverte d'eau, donnant ainsi une couleur bleue à la terre, comme les astronautes ont pu le constater lors de la mission Apollo en 1972.
De plus, la terre possède l'eau dans tous ses états : solide, liquide et gazeux.

L'eau est quelque chose qui a beaucoup intéressé les scientifiques de toutes les époques.
Nous pouvons notamment citer parmi eux le légendaire Archimède qui, au cours du 3ème siècle avant Jésus-Christ, aurait immergé une couronne dans l'eau pour déterminer la pureté de l'or dont elle était faite.
La science à nommé cette méthode la poussée d'Archimède.

Au 17ème siècle, un mathématicien et physicien dénommé Galilée s'est penché sur les fluides et a découvert la viscosité : l'une des propriétés fondamentales des fluides.

Puis entre le 17ème et le 18ème siècle le célèbre Isaac Newton a développé d'avantage les travaux de Galilée.
Nous lui devons la définition d'un fluide newtonien, c'est à dire d'un fluide dont la viscosité est inépendante de la contrainte mécanique s'exerçant sur celui-ci, donc un fluide ayant un comportement prévisible.

Grâce aux études d'Isaac Newton, Leonhard Euler d'origine bâloise établit au cours du 18ème siècle des équations [-@sec-EE] modélisant l'écoulement d'un fluide parfait adiabatique, donc d'un fluide pour lequel la viscosité et les effets de la chaleur ne sont pas pris en compte.

Mais cela ne satisfit pas tous les scientifiques.
C'est pourquoi, au cours du 19ème siècle, frustrés par l'impossibilité de modéliser des fluides visqueux, le mathématicien Henri Navier et le physicien Georges Gabriel Stokes décidèrent d'ajouter la notion de viscosité aux équations d'Euler [-@sec-EE], étendant ainsi les équations sur les fluides newtoniens.
Leur travail fut reconnu et utilisé sous le nom d'équations de Navier-Stokes [-@sec-NSE].
Jusqu'à aujourd'hui, personne n'a réussi à trouver une forme analytique aux équations de Navier-Stokes [-@sec-NSE], c'est pourquoi elles font toujours partie des 7 problèmes du prix du millénaire.

Cependant, la technologie a fait de nombreux progrès surtout vers la fin du 20ème siècle avec l'apparition de l'ordinateur, ce qui permit aux scientifiques de tenter de résoudre les équations de Navier-Stokes [-@sec-NSE] grâce à des approximations et des méthodes numériques.
Plusieurs méthodes ont donc été créées, notamment la méthode Smoothed Particle Hydrodynamics (SPH), la méthode Fluid-Implicit Particles (FLIP) et la méthode Lattice Boltzmann Method (LBM).
Cependant, quelles sont les différences entre ces méthodes ?
Y-a-t-il une méthode plus rapide qu'une autre ?
Serait-il possible d'utiliser ces méthodes afin d'obtenir un rendu en temps réel de haute qualité ?

Nous allons commencer par expliquer la théorie de chacune de ces méthodes, puis nous allons nous pencher sur les différences les distinguant et sur les résultats concrets obtenus grâce au code de GVDB-Voxel et de FluidX3D.


