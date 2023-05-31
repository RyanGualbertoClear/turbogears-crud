# -*- coding: utf-8 -*-
"""Setup the postsapi application"""

from .schema import setup_schema
import logging

from postsapi.config.app_cfg import base_config

__all__ = ['setup_app']

log = logging.getLogger(__name__)


def setup_app(command, conf, vars):
    """Place any commands to setup postsapi here"""
    conf = base_config.configure(conf.global_conf, conf.local_conf)
    base_config.setup(conf)

    setup_schema(command, conf, vars)
