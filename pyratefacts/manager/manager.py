from ..parser import Parser

from copy import deepcopy

class Manager():
    def __init__(self, filepath):
        self._parser = Parser(filepath)
        self.artifact_list = self._parser.list_artifacts()
        self.load_datafile()

    def prepare_all(self):
        valid_state = True
        for artifact in self.artifact_list:
            if not artifact.available:
                artifact.prepare()
            valid_state = valid_state and artifact.available
        return valid_state

    def prepare_single(self, artifact_name):
        for artifact in self.artifact_list:
            if artifact.name == artifact_name:
                if not artifact.available:
                    artifact.prepare()
            return artifact.available
    
    def load_datafile(self):
        # override self.artifact_list with content from datafile
        self.datafile = self._parser.get_datafile()
        datafile = deepcopy(self.datafile)

        if hasattr(datafile, 'artifact_list'):
            for a in datafile.artifact_list:
                for b in self.artifact_list:
                    if a.name == b.name:
                        for k,v in a.__dict__.items():
                            b.__dict__[k] = v

        # todo: there doesnt seem to be a case where there will be files in pkl that werent before in config
        # but if necessary, should implement it

    def save_datafile(self):
        self.datafile.save(self.artifact_list)