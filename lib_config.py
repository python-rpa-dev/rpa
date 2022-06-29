# -*- coding: utf-8 -*-
"""
Library to load configuration from an ini file

@author: python-rpa-dev

Version Date        Author           Info
-------------------------------------------------------------------------------
1.0.0   2022.06.20  python-rpa-dev   Initial Version
1.0.1   2022.06.29  python-rpa-dev   Test multiple values for workflow config

"""

import logging
import configparser

logger = logging.getLogger(__name__)


def load_config(ini_file: str):
    """ open ini file and load content into a dictionary """
    logger.info("Open configuration: %s", ini_file)

    try:
        config = configparser.ConfigParser()
        config.read_file(open(ini_file, "r"))

        logger.info("Reading configuration done.")
        logger.debug({section: dict(config[section]) for section in config.sections()})

    except Exception as e:
        logger.critical("Error reading config file!")
        raise Exception('Stop processing!') from e

    return config


if __name__ == "__main__":
    """ setup logging capabilities """
    logging.basicConfig(
        format='%(asctime)s [%(filename)s:%(lineno)-5s] %(levelname)-5s - %(funcName)-20s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=logging.DEBUG
        )

    test_cfg = load_config('rpa.ini')
    for module in test_cfg["RPA"]["run_daily"].strip().split("\n"):
        logger.debug(module)

