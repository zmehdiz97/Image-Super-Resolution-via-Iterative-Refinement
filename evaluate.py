from core.metrics import *
import os
from PIL import Image
dir = 'experiments/sr_div2k_220210_210800/results'
files= os.listdir(dir)
inf = [f for f in files if f.endswith('inf.png')]
hr = [f for f in files if f.endswith('hr.png')]
sr= [f for f in files if f.endswith('sr.png')]

PSNR_inf = 0
SSIM_inf = 0
for f1,f2 in zip(inf, hr):
    im1 = np.array(Image.open(os.path.join(dir, f1)))
    im2 = np.array(Image.open(os.path.join(dir, f2)))
    SSIM_inf += calculate_ssim(im1, im2)
    PSNR_inf += calculate_psnr(im1, im2)
print(f'inf, PSNR: {PSNR_inf/len(inf)}, SSIM: {SSIM_inf/len(inf)}')
PSNR_sr = 0
SSIM_sr = 0
for f1,f2 in zip(sr, hr):
    im1 = np.array(Image.open(os.path.join(dir, f1)))
    im2 = np.array(Image.open(os.path.join(dir, f2)))
    PSNR_sr += calculate_psnr(im1,im2)
    SSIM_sr += calculate_ssim(im1,im2)

print(f'sr, PSNR: {PSNR_sr/len(inf)}, SSIM: {SSIM_sr/len(inf)}')
