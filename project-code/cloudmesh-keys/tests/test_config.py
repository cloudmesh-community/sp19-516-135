""" run with

pytest -v --capture=no tests/test_config.py

"""
from __future__ import print_function

import os
import  time
from cloudmesh.config2.api.encryption import EncryptFile

import pytest
import datetime

# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,PyMethodMayBeStatic,PyPep8Naming,PyBroadException,PyBroadException

@pytest.mark.incremental
class Test_configdict:



    def setup_class(self):
        self.e = EncryptFile('~/.cloudmesh/cloudmesh.yaml', '~/.cloudmesh/cloudmesh.yaml.enc', '')


    def test_getRandonPassword(self):
        self.e.getRandonPassword()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/key.bin')
        assert exists
        if exists:
            f = open('/Users/xiaoyue/.cloudmesh/key.bin', 'r')
            password = f.readlines()[0]
            f.close()
        else:
            password = None
        assert  len(password) > 20


    def test_encrypt(self):
        self.e.encrypt()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml.enc')
        assert exists
        enc_size = os.path.getsize('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml.enc')
        enc_size = enc_size *10000/ float(1024 * 1024)
        print(enc_size)
        orginal_size= os.path.getsize('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml')
        orginal_size = orginal_size *10000/ float(1024 * 1024)
        print(orginal_size)
        assert abs(enc_size - orginal_size) < 10



    def test_encryptPassword(self):
        self.e.encryptPassword()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/key.bin.enc')
        assert exists
        times = os.path.getmtime('/Users/xiaoyue/.cloudmesh/key.bin.enc')
        timestamp = time.localtime(times)
        fileCreatTime = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
        print (fileCreatTime)
        currenttime= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(currenttime)

        startTime = datetime.datetime.strptime(fileCreatTime, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.strptime(currenttime, "%Y-%m-%d %H:%M:%S")
        assert (endTime - startTime).seconds < 4


        

    def test_decryptRandomKey(self):
        self.e.decryptRandomKey()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/key.bin.enc.plain')
        assert exists
        times = os.path.getmtime('/Users/xiaoyue/.cloudmesh/key.bin.enc.plain')
        timestamp = time.localtime(times)
        fileCreatTime = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
        print (fileCreatTime)
        currenttime= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(currenttime)
        startTime = datetime.datetime.strptime(fileCreatTime, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.strptime(currenttime, "%Y-%m-%d %H:%M:%S")
        assert (endTime - startTime).seconds < 4


    def test_decrypt(self):
        self.e.decrypt()
        exists = os.path.isfile('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml.enc.plain')
        assert exists
        dec_size = os.path.getsize('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml.enc.plain')
        dec_size = dec_size *10000/ float(1024 * 1024)
        print(dec_size)
        orginal_size= os.path.getsize('/Users/xiaoyue/.cloudmesh/cloudmesh.yaml')
        orginal_size = orginal_size *10000/ float(1024 * 1024)
        print(orginal_size)
        assert abs(dec_size - orginal_size) < 2

        assert True


    def test_ssh_keygen(self):
        self.e.ssh_keygen()
        for file in os.listdir("/Users/xiaoyue/.ssh"):
            file_path = os.path.join("/Users/xiaoyue/.ssh", file)
            if not os.path.isdir(file_path):
                if os.path.splitext(file)[1] == '.pub':
                    flag = True
                    assert flag
                    return




    def test_pem_create(self):
        self.e.pem_create()
        for file in os.listdir("/Users/xiaoyue/.ssh"):
            file_path = os.path.join("/Users/xiaoyue/.ssh", file)
            if not os.path.isdir(file_path):
                if os.path.splitext(file)[1] == '.pub':
                    flag = True
                    assert flag
                    return


    def test_pem_verify(self):
        self.e.pem_verify()
        assert True


    def test_set(self):
       filename =  "/Users/xiaoyue/.cloudmesh/cloudmesh4.yaml"
       key = "cloudmesh.profile.firstname"
       value = "Gregor"
       self.e.set(filename,key,value)
       times = os.path.getmtime('/Users/xiaoyue/.cloudmesh/cloudmesh4.yaml')
       timestamp = time.localtime(times)
       fileUpdateTime = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
       print(fileUpdateTime)
       currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
       print(currenttime)
       startTime = datetime.datetime.strptime(fileUpdateTime, "%Y-%m-%d %H:%M:%S")
       endTime = datetime.datetime.strptime(currenttime, "%Y-%m-%d %H:%M:%S")
       assert (endTime - startTime).seconds < 4



    def test_edit(self):
        self.e.edit()
        assert True


