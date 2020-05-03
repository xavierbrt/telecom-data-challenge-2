## Décomposition:
- Bases fonctionnelles à noyaux (RKHS)
- PCA
- Fourier Basis
- Kernel Basis
- FPCA basis
- FPCA on aligned data
- Kernel on periodogram
- FPCA on periodogram
 -> local anomalies, pattern anomalies, periodicity anomaly
Transformée en ondelettes discrète
PCA sur 3 axes puis l'afficher en 3D
FFT
Functional PCA
Filtres ! Comme Kalman filter ? Passe-bas ?
Exponential smoothing


## Outlier detection:
LOF
TNND
gamma-NN
DBSCAN clustering
One Class SVM (RBF, gamma = 0,5, trade-of = 0,1) nu=0.03 ?


## Data augmentation
Horizontal flipping

## Features
Utiliser des packages dédiés comme tsfresh. It automatically calculates a large number of time series characteristics (features)

Chloé: que du OSM, puis moyenne de 2 rankings (données brutes avec features + idem mais décomposition en ondelettes)
median, 30 et 70 percentiles et points qui s'écartent de plus de 90% de la moyenne
Vincent a fait du ts_fresh
Tracer les histos des stats
Sur les coefficients d'ondelettes, prendre les extrémités (ondelettes les plus compressés)
FFT (fourrier transform)
Passage en log ?
py-wavelet Sinc4
pywt.dwt
Ils ont pris les queues de distribution 
Multilevel decomposition sur plusieurs niveaux pour dilater plus ou moins les ondelettes
wavedec


Code d'Albert Thomas - choix des hyperparametres (voir code sur son git) (cité par Clémençon en cours)
Faire un K-means sur le jeu
Density Plots through Kernel density estimation (KDE)
Sequential Bayesian Filtering


Histogramme des stats
Calcul des dérivés



## VAE
Normaliser avant d'utiliser l'autoencodeur !! - (z-score standardization ?)
Sequentiel VAE LSTM moins bons scores
Autoencoder Forest for Anomaly Detection from IoT Time Series (vidéo https://www.youtube.com/watch?v=V0r2zDhdi6c)


flip vertical, entropy,
Essayer différentes valeurs de rolling, essayer la PCA sans rolling aussi
Faire tourner un algo type XGBoost sur toutes les soumissions et le score obtenu à chaque fois. Puis deviner l'impact de chaque paramètre ?

Tout passer à l'autocorrélation puis à PCA
Calcul des dérivés
Lire mes notes en haut
FPCA

