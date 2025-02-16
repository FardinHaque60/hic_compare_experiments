# HiC Compare Experiments
Experiments for HiC compare research. Manuscript: https://carlosrojas.xyz/hic_compare_manuscript/

## Set-Up
Repo was made and tested with `python 3.12.8` <br>
*TODO: Looking to dockerize repo in future so it will be able to run regardless of version

* Create venv with `python3 -m venv venv`
* Activate venv with `source venv/bin/activate`
* Install dependencies with `pip install -r requirements.txt`

## See experiments with instructions in folders below:
* `simple_diff` - takes simple diff of two hic matrices 
* `pca_window` - applies pca on two generated matrices with noise and clusters of high contrast differences, takes differences of these matrices
* `pca_hic` - takes difference of two hic matrices with pca applied to them