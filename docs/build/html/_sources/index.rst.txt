.. epipy documentation documentation master file, created by
   sphinx-quickstart on Wed Oct 22 11:42:38 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

epipy documentation
===================

This website contains the documentation and tutorials for Epipy: a python interface for EPISOL (kernel for 3DRISM calculations). 


   
.. toctree::
   :maxdepth: 1
   :caption: Contents:
   
   Home <self>
   background
   installation
   episol
   examples



What is this?
------------


Epipy is the python interface for EPISOL and relies on its kernel to perform 3DRISM calculations. Epipy helps the user to setup and automatically modify input files then calls the EPISOL kernel to perform the calculation. Episol solves the 3-dimens
ional reference interaction site model (3DRISM) equation.

:math:`h_v({\bf r}) = c_v({\bf r}) + \sum_{v'}\int \rho_{v'}^b c_{v'}({\bf r}')(h_{vv'}(r_{vv'})+s_{vv'}(r_{vv'}))d^3{\bf r}'`

Via applying the following closure relation in a sef-consistent manner.

:math:`h_v({\bf r}) = e ^{-u_v({\bf r})/k_BT+h_v({\bf r})-c_v({\bf r})+B_v({\bf r})} - 1`


Offering 22 available bridge functionals.
Epipy also includes some helpful functions for post-processing, including extratcing compressed 3DRISM output and loading into an array. Calculations require *ONLY* a topology , and structure file (ideally .gro).


:code:`from episol import epipy`

:code:`example = epipy("structure.gro","topology.top")`


Setting grid-resolution, and number of SCF cycles follows:


:code:`example.rism(step=1000,resolution=0.5)`


and finally, calling the kernel to perform the cacluation


:code:`example.kernel()`


This writes the relevant grid-based data to a .ts4s file, and epipy will automatically extract our desired values given a selection command


:code:`data = example.select_grid('guv')`

See our example library for example calculations

How to cite
-----------

If you liked this. please cite :)

DOI: coming 

