# -*- coding: utf-8 -*-
"""
Library to handle application versioning and encryption

@author: python-rpa-dev

Date        Author          Info
-----------------------------------------------------------------------
2022.06.29  python-rpa-dev  Initial Version

"""

import logging
import hashlib

logger = logging.getLogger(__name__)


def gen_checksum(source_file: str):
    """  """
    logger.info("Open configuration: %s", source_file)

    try:
        with open('rpa.py') as f:
            alist = [line.rstrip() for line in f]
            checksum = hashlib.md5(''.join(alist).encode()).hexdigest()

        logger.info("File processing done.")

    except Exception as e:
        logger.critical("Error reading source file!")

    return checksum


if __name__ == "__main__":
    """ setup logging capabilities """
    logging.basicConfig(
        format='%(asctime)s [%(filename)s:%(lineno)-5s] %(levelname)-5s - %(funcName)-20s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=logging.DEBUG
        )

    app_md5 = gen_checksum('rpa.py')
   
    logger.info("File checksum is: %s", app_md5)
