import copy
import os
import pickle

class Datafile():
    def __init__(self, filename=None):
        self.filename = filename
        if filename:
            if os.path.exists(filename) and os.path.isfile(filename):
                with open(filename, 'rb') as f:
                    loaded = pickle.load(f)
                for k,v in loaded.items():
                    self.__dict__[k] = v
            else:
                self.save()
                # raise IOError("Datafile {} not found or is directory name".format(filename))
        else:
            self.artifact_list = []

    def save(self, artifact_list=None):
        if artifact_list:
            self.artifact_list = copy.deepcopy(artifact_list)

        export_dict = {}
        for k,v in self.__dict__.items():
            # todo: add condition to save
            if not callable(self.__dict__[k]):
                export_dict[k] = v

        with open(self.filename, 'wb') as f:
            pickle.dump(export_dict, f)