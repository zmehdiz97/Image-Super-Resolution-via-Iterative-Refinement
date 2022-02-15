import logging

from model.model import Regressor
logger = logging.getLogger('base')


def create_model(opt):
    from .model import DDPM as M
    #m = M(opt)
    m = Regressor(opt)
    logger.info('Model [{:s}] is created.'.format(m.__class__.__name__))
    return m
