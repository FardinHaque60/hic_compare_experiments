# HiC Compare Experiments
Experiments for HiC compare research. 
- Manuscript: https://carlosrojas.xyz/hic_compare_manuscript/
- [CSCSU Submission Paper](https://drive.google.com/file/d/1IcG_abP1gChwC_HL3mhh5a0F1J00WkWH/view?usp=sharing)
    - all plots used in this submission can be found in the `all_plots` directory with descriptions of the experiments and results.

## Set-Up
Repo was made and tested with `python 3.12.8` <br>

* Create venv with `python3 -m venv venv`
* Activate venv with `source venv/bin/activate`
* Install dependencies with `pip install -r requirements.txt`

## See experiments with instructions in the `denoising_experiments` folders below:
* `pca_hic` - takes difference of two hic matrices with pca applied to them
* `autoencoder_hic` - autoencoder applies onto hic matrices
* `mf_hic` - matrix factorization applied onto hic matrices
* `svt_hic` - singular value threshold applied onto hic matrices

## experiments in the `misc` folder:
* `simple_diff` - takes simple diff of two hic matrices 
* `pca_window` - applies pca on two generated matrices with noise and clusters of high contrast differences, takes differences of these matrices