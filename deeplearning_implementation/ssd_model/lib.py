import os
import os.path as osp

import random
import xml.etree.ElementTree as ET
import cv2 
import torch.utils.data as data
import numpy as np

# fix 1 co so ngau nhien
torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)