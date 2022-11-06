import os   # tao cac folder, join cac path cua folder khac nhau
import urllib.request
import zipfile
import tarfile


# tao file data
data_dir = "./data"
if not os.path.exists(data_dir):
    os.mkdir(data_dir)

# link todataset
# url = "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar"
url = "https://img.freepik.com/premium-photo/red-welsh-corgi-dog-pembroke-close-up_392339-19.jpg?w=2000"

# target_path = os.path.join(data_dir,"VOCtrainval_11-May-2012.tar")
target_path = os.path.join(data_dir,"toy_image.jpg")
urllib.request.urlretrieve(url, target_path)

if not os.path.exists(target_path):
    urllib.request.urlretrieve(url, target_path)  # download dataset

    tar = tarfile.TarFile(target_path)   # doc file
    tar.extractall(data_dir)
    tar.close
