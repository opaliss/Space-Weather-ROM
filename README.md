## [Predicting solar wind streams from the inner-heliosphere to Earth via shifted operator inference](https://www.sciencedirect.com/science/article/pii/S0021999122007525#!)

### Abstract 
Solar wind conditions are predominantly predicted via three-dimensional numerical magnetohydrodynamic (MHD) models. Despite their ability to produce highly accurate predictions, MHD models require computationally intensive high-dimensional simulations. This renders them inadequate for making time-sensitive predictions and for large-ensemble analysis required in uncertainty quantification. This paper presents a new data-driven reduced-order model (ROM) capability for forecasting heliospheric solar wind speeds. Traditional model reduction methods based on Galerkin projection have difficulties with advection-dominated systems—such as solar winds—since they require a large number of basis functions and can become unstable. A core contribution of this work addresses this challenge by extending the non-intrusive operator inference ROM framework to exploit the translational symmetries present in the solar wind caused by the Sun's rotation. The numerical results show that our method can adequately emulate the MHD simulations and is more accurate than a reduced-physics surrogate model, the Heliospheric Upwind Extrapolation model.

### Dependencies
1. [Python >= 3.7](https://www.python.org/downloads/)
1. [numpy >= 1.19.1](https://numpy.org/install/)
3. [matplotlib >= 3.3.1](https://matplotlib.org/users/installing.html)
4. [scipy >= 1.5.0](https://www.scipy.org/install.html)
5. [pyhdf >= 0.10.2](https://pypi.org/project/pyhdf/)
6. [psipy >= 0.1.1](https://psipy.readthedocs.io/en/stable/guide/installing.html)
7. [heliopy >= 0.15.3](https://docs.heliopy.org/en/stable/index.html)
8. [rom-operator-inference >= 1.2.1](https://pypi.org/project/rom-operator-inference/)


### Data 
All data from MAS MHD model results can be downloaded using [PsiPy](https://psipy.readthedocs.io/en/stable/auto_examples/sampling/plot_in_situ_comparison.html#sphx-glr-auto-examples-sampling-plot-in-situ-comparison-py) and [HelioPy](https://docs.heliopy.org/en/stable/index.html). 

#### Correspondence
Opal Issan (PhD student), University of California, San Diego. oissan@ucsd.edu

### License
MIT
