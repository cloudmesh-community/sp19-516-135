""" run with

python setup.py install; nosetests -v --nocapture tests/test_config.py:Test_configdict.test_001

nosetests -v --nocapture tests/test_config.py

or

nosetests -v tests/test_config.py

"""
from __future__ import print_function

import os

from cloudmesh.config2.api.encryption import EncryptFile

# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,PyMethodMayBeStatic,PyPep8Naming,PyBroadException,PyBroadException
class Test_configdict:
    root_path = os.path.abspath(os.sep)
    cwd_path = os.getcwd()

    def setup(self):
        # os.system("cm help")
        # self.etc_yaml = os.path.join(self.cwd_path, "cloudmesh_client", "etc", "cloudmesh.yaml")
        self.tmp_yaml = os.path.join(self.root_path, "tmp", "cloudmesh.yaml")
        self.tmp_dir = os.path.join(self.root_path, "tmp")
        pass

    # noinspection PyPep8Naming
    def tearDown(self):
        pass

    def test_config(self):

        '''
        for filename in ['file.txt', 'secret.txt']:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

        # Creating a file with data

        with open("file.txt", "w") as f:
            f.write("Big Data is here.")
        '''
        e = EncryptFile('/Users/xiaoyue/Desktop/test.yaml', '/Users/xiaoyue/Desktop/test.yaml.enc', '')
        e.decrypt()

        '''
        # if the file is existed
        file_in = "secret.txt"
        file_out = "plain.txt"
        # if the file is existed

        if not os.path.exists(file_in):
            os.system(r"touch {}".format(file_out))  # create the file

        '''

