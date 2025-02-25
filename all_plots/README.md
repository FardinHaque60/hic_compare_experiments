## all plots from hic experiments
this dir contains all the plots from following hic experiments. see the sample outputs below and their captions.

for every data sample the following experiments were run:
* `pca_hic` - applies pca to the patient and control hic matrices. reduces noise on the matrices before comparing them. includes stat to help determine window size.
* `simple_diff` - takes simple diff of two hic matrices to expose areas of difference.
* `autoencoder_hic` - applies autoencoder to hic matrix to remove noise. 

### dlbcl 
using data with chromatin conformation changes in B-cells of a diffuse large B-cell lymphoma (DLBCL) patient.
comparing chromosome 2 for differences with 3 Mb window size, stepping 100 kb. 

* original data
![original data](dlbcl/original_data.png)
caption: 
Figure A: raw data of patient dlbcl sample from chess with red bounding boxes representing gained features from control sample
Figure B: raw data of control dlbcl sample from dlbcl with blue bounding boxes representing lost features that did not carry over to patient

* `simple_diff`
![simple diff](dlbcl/simple_diff.png)
caption: 
Figure A: simple diff of patient - control
Figure B: simple diff of control - patient
Figure C: log transformation of patient/control
Figure D: log transformation control/patient

stats:

* `pca_hic`
![pca_hic](dlbcl/pca_hic.png)
caption: 
Figure A: PCA applied to on patient
Figure B: PCA applied to control
Figure C: Difference of PCA patient - control
Figure D: Difference of PCA control - patient
Figure E: log transformation of PCA applied patient/control
Figure F: log transformation of regular patient/control

stats: