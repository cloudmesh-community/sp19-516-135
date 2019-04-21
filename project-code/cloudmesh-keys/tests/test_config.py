""" run with

pytest -v --capture=no tests/test_config.py

"""
from __future__ import print_function

import os

from cloudmesh.config2.api.encryption import EncryptFile

import pytest

# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,PyMethodMayBeStatic,PyPep8Naming,PyBroadException,PyBroadException

@pytest.mark.incremental
class Test_configdict:



    def setup_class(self):
        self.e = EncryptFile('~/.cloudmesh/cloudmesh.yaml', '~/.cloudmesh/cloudmesh.yaml.enc', '')


    def test_getRandonPassword(self):
        self.e.getRandonPassword()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/key.bin')
        if exists:
            f = open('/Users/xiaoyue/.cloudmesh/key.bin', 'r')
            password = f.readlines()[0]
            f.close()
        else:
            password = None
        assert  len(password) > 20


    def test_encrypt(self):
        self.e.encrypt()
        assert True
        
    def test_encryptPassword(self):
        self.e.encryptPassword()
        assert True
        

    def test_decryptRandomKey(self):
        self.e.decryptRandomKey()
        assert True

    def test_decrypt(self):
        self.e.decrypt()
        assert True


    def test_ssh_keygen(self):
        self.e.ssh_keygen()
        assert True

    def test_pem_create(self):
        self.e.pem_create()
        assert True

    def test_pem_verify(self):
        self.e.pem_verify()
        assert True


    def test_set(self):
       filename =  "/Users/xiaoyue/.cloudmesh/cloudmesh4.yaml"
       key = "cloudmesh.profile.firstname"
       value = "Gregor"
       self.e.set(filename,key,value)
       assert True


    def test_edit(self):
        self.e.edit()
        assert True


