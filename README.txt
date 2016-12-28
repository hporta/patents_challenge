Pour pouvoir effectuer ce script il faut tout d'abord installer xgboost. On va vous expliquer la méthode sur Linux.

Tout d'abord il faut installer Git.

En ligne de commande il faut taper :

git clone --recursive https://github.com/dmlc/xgboost

Puis il faut se rendre dans le répertoire xgboost et effectuer :

make -j4

Puis il faut se rendre dans le répertoire python package et effectuer :

sudo python setup.py install

Xgboost est ainsi installé. Il suffit ensuite d'exécuter le script python qui peut prendre un certain temps



