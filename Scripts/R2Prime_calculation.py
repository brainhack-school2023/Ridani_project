import numpy as np
import nibabel as nib

# Load the input images
img1 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/brain_hack_experiments/ChallengeProtocol/No_variation_challenge/FitResults_2023-05-30_12-03-50/T2.nii.gz')
#img2 = nib.load('C:/Users/Daniel Ridani/Desktop/Chi-separation/Chi_separation_test_simulation/T2_map.nii.gz')

# Get the dimensions of the input images
#dim1 = img1.shape
#dim2 = img2.shape

# Calculate the inverse of each image
inv_img1 = 1/img1.get_fdata()

#print(inv_img1.dtype)
#inv_img2 = 1/img2.get_fdata()

# Replace any inf or NaN values with zero
#inv_img1[~np.isfinite(inv_img1)] = 0
#inv_img2[~np.isfinite(inv_img2)] = 0

#inv_img1=np.squeeze(inv_img1)
#inv_img2=np.squeeze(inv_img2)
#Save R2_star and R2
#diff_nifti_img = nib.Nifti1Image(inv_img1, img1.affine)
#nib.save(diff_nifti_img, 'C:/Users/Daniel Ridani/Desktop/Chi-separation/Chi_separation_test_simulation/chi_separation_whole_brain/R2_star.nii.gz')

#diff_nifti_img = nib.Nifti1Image(inv_img2, img2.affine)
#nib.save(diff_nifti_img, 'C:/Users/Daniel Ridani/Desktop/Chi-separation/Chi_separation_same_parameter_chi_separation/R2_3.nii.gz')

# Calculate the difference between the two images
diff_img = inv_img1/1.91
# Set any negative values to zero
#diff_img[diff_img < 0] = 0

# Save the result to a NIfTI file
result_img = nib.Nifti1Image(diff_img, img1.affine)
nib.save(result_img, 'C:/Users/Daniel Ridani/Desktop/Chi-separation/brain_hack_experiments/ChallengeProtocol/No_variation_challenge/R2_prime.nii.gz')
