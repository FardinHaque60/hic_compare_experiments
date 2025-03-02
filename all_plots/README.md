## all plots from hic experiments
this dir contains all the plots from following hic experiments. see the sample outputs below and their captions.

every experiment is outlined below. the following experiments are applied onto the dlbcl dataset:
* `simple_diff` - takes simple diff of two hic matrices to expose areas of difference.
* `pca_hic` - applies pca to hic matrix1 and matrix2. reduces noise on the matrices before comparing them. includes stat to determine which window size best eliminates noise.
* `autoencoder_hic` - applies autoencoder to hic matrices to remove noise. autoencoder is trained on original matrix and used to denoise the query matrix. 
* TODO add more

### dlbcl dataset info
using data with chromatin conformation changes in B-cells of a diffuse large B-cell lymphoma (DLBCL) patient.
comparing chromosome 2 for differences with 3 Mb window size, stepping 100 kb. [Data Availability](https://en.wikipedia.org/wiki/Diffuse_large_B-cell_lymphoma)

* original data
![original data](dlbcl/simple_diff.png)
Figure 1 <br>
caption: <br>
Figure 1.1: raw data of patient dlbcl sample from chess with red bounding boxes representing gained features from control sample <br>
Figure 1.2: raw data of control dlbcl sample from dlbcl with blue bounding boxes representing lost features that did not carry over to patient <br>
Figure 1.3: simple diff of patient - control <br>
Figure 1.4: log2(patient/control) <br>

stats: <br>

* `pca_hic`
![pca_hic](dlbcl/pca_hic.png)
Figure 3 <br>
caption: <br>
experiment used a 3x3 window size. <br>
Figure 3.1: PCA applied to on patient <br>
Figure 3.2: PCA applied to control <br>
Figure 3.3: Difference of PCA patient - control <br>
Figure 3.4: log transformation of PCA applied patient/control <br>

stats: <br>

* `autoencoder_hic`
![autoencoder_pca](dlbcl/autoencoder_hic.png)
Figure 4 <br>
caption: <br>
Figure 4.1: autoencoder applied onto patient sample <br>
Figure 4.2: autoencoder applied onto control sample <br>
Figure 4.3: autoencoder applied patient - control <br>
Figure 4.4: log transformation of autoencoder applied patient / control <br>

stats: <br>

### noise added to dlbcl data
in this experiment, noise is added with gaussian blur layers to the dlbcl data. the experiments are conducted to see how well it removes the manually added noise.

* original data
noise added to original data in increments
![original syn data](noise/original_data.png)
Figure 5 <br>
caption: <br>
- first row is patient data with increasing noise
- second row is control data with increasing noise 

stats: <br>

* `pca_hic` 
![pca hic](noise/pca_hic.png)
Figure 6 <br>
caption: <br>
- first row is pca applied onto patient noise data
- second row is pca applied onto control noise data
- third row is diff of respective pca applied patient - control 

stats: <br>

* `autoencoder_hic`
![autoencoder hic](noise/autoencoder_hic.png)
Figure 7 <br>
caption: <br>
- first row is autoencoder applied onto patient noise data
- second row is autoencoder applied onto control noise data
- third row is autoencoder of respective pca applied patient - control 

stats: <br>