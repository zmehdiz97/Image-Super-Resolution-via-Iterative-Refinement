from torch import nn
class Baseline(nn.Module):
    def __init__(
        self,
        denoise_fn,
        image_size,
        channels=3,
        loss_type='l1',
    ):
        super().__init__()
        self.channels = channels
        self.image_size = image_size
        self.denoise_fn = denoise_fn
        self.loss_type = loss_type
    
    def forward(self, x, *args, **kwargs):
        x_noisy = x['SR']
        x_recon = self.denoise_fn(x_noisy)
        return x_recon