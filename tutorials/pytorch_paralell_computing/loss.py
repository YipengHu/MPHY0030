import torch.nn as nn
import torch

class DiceLoss(nn.Module):
    def __init__(self):
        super(DiceLoss, self).__init__()
        self.smooth = 1.0

    def forward(self, y_pred, y_true):
        assert y_pred.size() == y_true.size()
        y_pred = y_pred[:, 0].contiguous().view(-1)
        y_true = y_true[:, 0].contiguous().view(-1)
        intersection = (y_pred * y_true).sum()
        dsc = (2. * intersection + self.smooth) / (y_pred.sum() + y_true.sum() + self.smooth)
        return 1. - dsc


def binary_dice(y_true, y_pred):
    eps = 1e-6
    y_true = y_true >= 0.5
    y_pred = y_pred >= 0.5
    numerator = torch.sum(y_true * y_pred) * 2
    denominator = torch.sum(y_true) + torch.sum(y_pred)
    if numerator == 0 or denominator == 0:
        return 0.0
    else:
        return numerator * 1.0 / denominator