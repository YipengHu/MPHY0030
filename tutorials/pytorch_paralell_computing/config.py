import argparse
import os
import logging

parser = argparse.ArgumentParser()
# common options
parser.add_argument('--exp_name', default=None, type=str, help='experiment name you want to add.')
parser.add_argument('--logdir', default='./logs', type=str, help='log dir')

# Training options
parser.add_argument('--lr', default=1e-4, type=float, help='Learning rate.')
parser.add_argument('--batch_size', default=16, type=int, help='The number of batch size.')
parser.add_argument('--gpu', default='0', type=str, help='id of gpu')
parser.add_argument('--epochs', default=500, type=int, help='The number of iterations.')
parser.add_argument('--save_period', default=5, type=int, help='save period')
parser.add_argument('--model', default='unet', type=str, help='choose model')

args = parser.parse_args()

assert args.exp_name is not None, 'experiment name should not be none'
