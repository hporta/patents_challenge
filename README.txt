Pour pouvoir effectuer ce script il faut tout d'abord installer xgboost. On va vous expliquer la m�thode sur Linux.

Tout d'abord il faut installer Git.

En ligne de commande il faut taper�:

git clone --recursive https://github.com/dmlc/xgboost

Puis il faut se rendre dans le r�pertoire xgboost et effectuer�:

make -j4

Puis il faut se rendre dans le r�pertoire python package et effectuer�:

sudo python setup.py install

Xgboost est ainsi install�. Il suffit ensuite d'ex�cuter le script python qui peut prendre un certain temps



