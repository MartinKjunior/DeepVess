import matlab.engine
from glob import glob
import os.path as osp

eng = matlab.engine.start_matlab()

study_path = R'C:\Users\mbcxamk2\OneDrive - The University of Manchester\Uni\PhD project\Mouse_Study_PRIME242'

data_paths = glob(study_path + R'\Mouse*\PreparedImages\*.tif')
print(data_paths)

eng.addpath(eng.genpath(study_path))

path_dir = osp.dirname(data_paths[0])
path_base = osp.basename(data_paths[0])

#eng.prepareImage(1, 0, 1, 1, path_dir, path_base, nargout=0)

eng.quit()