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

    def test_encrypt(self):
        self.e.encrypt()

    def test_encryptPassword(self):
        self.e.encryptPassword()

    def test_decryptRandomKey(self):
        self.e.decryptRandomKey()

    def test_decrypt(self):
        self.e.decrypt()

    def test_ssh_keygen(self):
        self.e.ssh_keygen()

    def test_pem_create(self):
        self.e.pem_create()

    def test_pem_verify(self):
        self.e.pem_verify()


    def test_set(self):
       filename =  "/Users/xiaoyue/.cloudmesh/cloudmesh4.yaml"
       key = "cloudmesh.profile.firstname"
       value = "Gregor"
       self.e.set(filename,key,value)


    def test_edit(self):
        self.e.edit()