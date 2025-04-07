import numpy as np
import pandas as pd
import fanc
import os

def load_hic_data(script_dir=os.path.abspath(os.path.join('..', '..'))):
    winsize = "3mb"
    wdir = os.path.join(script_dir, "data", "dlbcl/")
    region_pairs = "hg38_chr2_{}_win_100kb_step.bed".format(winsize)

    gained = pd.read_csv(wdir + 'gained_features.tsv', delimiter=',', usecols=[0, 1, 2, 3, 4, 5], header=None, index_col=[0])
    lost = pd.read_csv(wdir + 'lost_features.tsv', delimiter=',', usecols=[0, 1, 2, 3, 4, 5], header=None, index_col=[0])

    regions = pd.read_csv(wdir + region_pairs, sep='\t', header=None)

    patient_hic = fanc.load(wdir + "ukm_patient_fixed_le_25kb_chr2.hic")
    control_hic = fanc.load(wdir + "ukm_control_fixed_le_25kb_chr2.hic")

    reg = 1448

    window_start, window_end = regions.loc[reg][1:3]

    region_string = "chr2:{}-{}".format(window_start, window_end)

    patient_region_sub = patient_hic[region_string, region_string].data
    control_region_sub = control_hic[region_string, region_string].data

    min_v = min(
        [
            np.min(np.extract(patient_region_sub>0 , patient_region_sub)),
            np.min(np.extract(control_region_sub>0 , control_region_sub))
        ]
    )

    patient_region_sub += min_v
    control_region_sub += min_v

    return patient_region_sub, control_region_sub