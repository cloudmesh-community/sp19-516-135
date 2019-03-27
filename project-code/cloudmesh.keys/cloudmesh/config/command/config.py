from __future__ import print_function
from pprint import pprint
import os
from cloudmesh.key.api.manager import Manager
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.config.api.encryption import EncryptFile


class ConfigCommand(PluginCommand):

    # see https://github.com/cloudmesh/client/blob/master/cloudmesh_client/shell/plugins/KeyCommand.py
    # see https://github.com/cloudmesh/client/blob/master/cloudmesh_client/shell/plugins/AkeyCommand.py

    # noinspection PyUnusedLocal
    @command
    def do_config(self, args, arguments):
        """
        ::

           Usage:
             config  -h | --help
             config encrypt [SOURCE] [DESTINATION]
             config decrypt [SOURCE] [DESTINATION]
             config set ATTRIBUTE VALUE


           Arguments:
             VMS            Para,eterized list of virtual machines
             CLOUDS         The clouds
             NAME           The name of the key.
             SOURCE         db, ssh, all
             KEYNAME        The name of a key. For key upload it defaults to the default key name.
             FORMAT         The format of the output (table, json, yaml)
             FILENAME       The filename with full path in which the key
                            is located

           Options:
              --dir=DIR                     the directory with keys [default: ~/.ssh]
              --format=FORMAT               the format of the output [default: table]
              --source=SOURCE               the source for the keys [default: cm]
              --username=USERNAME           the source for the keys [default: none]
              --name=KEYNAME                The name of a key


           Description:

                ssh-keygen
                ssh-add

                cms config encrypt ~/.cloudmesh/cloudmesh4.yaml ~/.cloudmesh/cloudmesh4.yamlz
                cms config decrype ~/.cloudmesh/cloudmesh4.yamlz ~/.cloudmesh/cloudmesh4.enc.yaml

        """

        pprint(arguments)

        m = Manager()
        e = EncryptFile(arguments.SOURCE, arguments.DESTINATION)
        if arguments.encrypt:
            e.encrypt()
            print("encrypt file")
            return ""

        elif arguments.decrypt:
            #if the file is existed
            if not os.path.exists(arguments.DESTINATION):
                os.system(r"touch {}".format(arguments.DESTINATION))  # create the file

            e.decrypt(arguments.SOURCE, arguments.DESTINATION)
            print("decrypt file")
            return ""



        return ""
