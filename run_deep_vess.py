"""
--Prepare--
Read tiff image
Normalise it
Change range to [-0.5, 0.5]
Save as an HDF5 file
--Segment--
Get the HDF5 file path
Write a subprocess command to run the DeepVess code
"""

import subprocess

hdf5_files = [
    R"C:\Users\mbcxamk2\OneDrive - The University of Manchester\Uni\PhD project\Mouse_Study_PRIME242\Mouse1.1Microscopy\TestingSingleVolume\SmallSingleVolume.h5"
]

for path in hdf5_files:
    print("Processing: " + path)
    process = subprocess.call(['python', 'DeepVess.py', path])

"""
import numpy as np
from scipy.ndimage import binary_dilation
import tifffile
import h5py
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from glob import glob

def normalize_image(im, saturated_prctile=[1, 98]):
    im = np.array(im, dtype=float)
    structure = np.ones((5,5))
    if im.ndim == 3:
        im2 = np.zeros_like(im)
        for k in range(im.shape[2]):
            im2[:,:,k] = im[:,:,k] * (binary_dilation(im[:,:,k]==0, structure=structure) == False)
    elif im.ndim == 2:
        im2 = im * (binary_dilation(im==0, structure=structure) == False)
    im2 = im2[im2 != 0]
    p = np.percentile(im2, saturated_prctile)
    if p[0] == p[1]:
        p[0] = np.min(im)
        p[1] = np.max(im)
        if p[0] == p[1]:
            return np.nan
    imOut = (im - p[0] + 1) / (p[1] - p[0] + 2)
    imOut = np.minimum(1, np.maximum(0, imOut))
    return imOut

def get_input_path():
    root = tk.Tk()
    root.withdraw()  # Hide the small tk window
    dir_path = filedialog.askdirectory(title="Please select the directory containing the data files")
    if not os.path.basename(dir_path) == "PreparedImages":
        dir_path = os.path.join(dir_path, "PreparedImages")
    tiff_path = glob(os.path.join(dir_path, "LargeAvg*.tif"))
    if len(tiff_path) == 0:
        raise Exception("No tiff file found")
    elif len(tiff_path) > 1:
        raise Exception("Multiple tiff files found")
    return tiff_path[0]

def save_hdf5(im, tiff_path):
    dir_path = os.path.dirname(tiff_path)
    filename = os.path.basename(tiff_path).split('.')[0]
    hdf5_path = os.path.join(dir_path, filename + '.h5')
    with h5py.File(hdf5_path, 'w') as f:
        f.create_dataset('init', data=im)
    return hdf5_path

def main():
    tiff_path = get_input_path()
    print("Processing: " + tiff_path)
    im = tifffile.imread(tiff_path)
    im = normalize_image(im)
    print("Normalised")
    # Change range to [-0.5, 0.5]
    im = im / np.max(im) - 0.5
    im = np.array(im, dtype=np.float32)
    hdf5_path = save_hdf5(im, tiff_path)
    print("Saved as HDF5")
    # Write a subprocess command to run the DeepVess code
    subprocess.call(['python', 'DeepVess.py', hdf5_path])

if __name__ == '__main__':
    main()
"""