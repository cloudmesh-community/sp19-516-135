class Manager(object):

    def __init__(self):
        print("init {name}".format(name=self.__class__.__name__))

    def list(self, parameter):
        print("list", parameter)



    def list (cloud=None ,format = None):
        pass

    def list (source=None ,dir=None, format=None):
        pass

    def list (source=None ,format=None, username=None):
        pass

    def list (names=None, format=None, source =None):
        pass

    def load (filename=None, format=None):
        pass

    def add (name=None, source=None):
        pass

    def add (name=None, source=None):
        pass

    def add (name=None, source=None):
        pass

    def get (name=None, format=None):
        pass

    def default (select=None):
        pass

    def delete (names=None, dryrun=False):

        if names == "all":
            pass
        else:
            pass
        pass

    def delete (names=None, cloud=None, dryrun=False):
        pass

    def upload (names=None, cloud=None, dryrun=False):
        pass

    def upload (names=None, vms=None, dryrun=False):
        pass

    def group_upload (group=None, cloud=None, dryrun=False):
        pass

    def group_add (group=None, cloud=None, dryrun=False):
        pass

    def group_add (file=None):
        pass

    def group_delete (group=None, names = None, dryrun=False):
        pass

    def group_list (group=None, format=None):
        pass

    def group_export(group=None, filename=None):
        pass