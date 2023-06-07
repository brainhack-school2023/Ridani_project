import nibabel as nib
import numpy as np

# Load the NIfTI segmentation file
seg_file = 'C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/data/masks/SegmentedModel.nii.gz'
seg_img = nib.load(seg_file)
seg_data = seg_img.get_fdata()

# Define the region values lookup table
region_values = {
    1: 0.0088,
    2: 0.0131,
    3: 0.0057,
    4: 0.025,
    5: 0.01,
    6: 0.008,
    7: 0.007,
    8: 0.0315,
    9: 0.001,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0
}

# Assign values to each region in the segmentation
for region_num in range(1, 17):
    region_voxels = (seg_data == region_num)
    region_value = region_values.get(region_num, None)
    seg_data[region_voxels] = region_value

# Create a new NIfTI image with the modified segmentation data
modified_seg_img = nib.Nifti1Image(seg_data, seg_img.affine, seg_img.header)

# Save the modified NIfTI segmentation file
modified_seg_file = 'C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/data/masks/chineg_no_variation.nii.gz'
nib.save(modified_seg_img, modified_seg_file)

print("Modified segmentation file saved successfully.")
