import nibabel as nib
import numpy as np

# Load the two input NIfTI files
nii1 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test3/SimulatedHR/Phase_TE004.nii.gz')
nii2 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test3/SimulatedHR/Phase_TE012.nii.gz')
nii3 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test3/SimulatedHR/Phase_TE020.nii.gz')
nii4 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test3/SimulatedHR/Phase_TE028.nii.gz')
#nii5 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test1/SimulatedHR/Phase_TE030.nii.gz')
#nii6 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test1/SimulatedHR/Phase_TE036.nii.gz')

# Extract the image data and dimensions
data1 = nii1.get_fdata()
dims = data1.shape

# Concatenate the data by grouping the echoes
grouped_data = np.stack((data1, nii2.get_fdata(), nii3.get_fdata(), nii4.get_fdata()), axis=3)
                        # nii5.get_fdata(), nii6.get_fdata()), axis=3)

# Create a new NIfTI image using the grouped data
grouped_nii = nib.Nifti1Image(grouped_data, affine=nii1.affine, header=nii1.header)

# Save the new NIfTI image to a file
nib.save(grouped_nii, 'C:/Users/Daniel Ridani/Desktop/Chi-separation/Simulation/Simdata/test3/SimulatedHR/Phase_data.nii.gz')