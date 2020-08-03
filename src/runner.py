# ! /usr/bin/env python
# coding=utf-8
import sys
import logging
import os
import pytest


sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
fileHandler = logging.FileHandler(filename="../log/auto.log", encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s- %(lineno)s- %(message)s")
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    logging.info("Start to excute automation cases")

    pytest.main(['-s', 'testcases/contact/department/test_create_depart.py'])
