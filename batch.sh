#!/bin/sh
#squeue -u gpusdi1_39
#conda env create -f core/environment.yml
#conda create  --name pytorch --file core/environment.txt
#python data/prepare_data.py --path /content/Image-Super-Resolution-via-Iterative-Refinement/input/ --size 64,512 --out ./dataset/celebahq
#conda install torchvision
#conda init
#pip install fid-score
conda activate pytorch
nvidia-smi
#python sr.py -p train -c config/sr_sr3_64_512.json
python baseline.py -p val -c config/sr_baseline_16_128.json
#python sr.py -p val -c config/sr_sr3_16_128.json
#python sr.py -p train -c config/sr_sr3_16_128.json

#python data/prepare_data.py --path ./dog/dog_train --size 16,128 --out ./dataset/dog_train
#python data/prepare_data.py --path ./dog/dog_val --size 16,128 --out ./dataset/dog_val

#wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X2.zip
#wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X2.zip
#wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
#wget http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_HR.zip