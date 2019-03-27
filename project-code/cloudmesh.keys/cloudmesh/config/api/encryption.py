import os
from cloudmesh.common.util import path_expand


class EncryptFile(object):
    def __init__(self, file_in, file_out, debug=False):
        self.data = {
            'file': file_in,
            'secret': file_out,
            'pem': path_expand('~/.ssh/id_rsa.pub.pem'),
            'key': path_expand(' ~/.ssh/id_rsa')
        }
        self.debug = debug

    def _execute(self, command):
        if self.debug:
            print(command)
        os.system(command)


    def encrypt(self):
        # encrypt the file into secret.txt
        print(self.data)
        command = path_expand(
            "openssl rsautl -encrypt -pubin -inkey {pem} -in {file} -out {secret}".format(**self.data))
        self._execute(command)

    def decrypt(self, filename=None,decrypted_file=None):
        if filename is not None:
            self.data['secret'] = filename
            self.data['file'] = decrypted_file

        command = path_expand("openssl rsautl -decrypt -inkey {key} -in {secret} -out {file}".format(**self.data))
        self._execute(command)


if __name__ == "__main__":
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
    e = EncryptFile('test.txt', 'secret.txt')
    e.encrypt()
    #e.decrypt("secret.txt","plain.txt")
    '''
    # if the file is existed
    file_in = "secret.txt"
    file_out = "plain.txt"
    # if the file is existed

    if not os.path.exists(file_in):
        os.system(r"touch {}".format(file_out))  # create the file
    
    '''
    e.decrypt()

