import os
import shutil

from ..artifacts.artifact import Artifact

class FileArtifact(Artifact):
    def __init__(self, *args, **kw):
        super(FileArtifact, self).__init__(*args, **kw)

    def prepare(self):
        if not os.path.isfile(self.url):
            raise IOError("File {} does not exist".format(self.url))

        shutil.copyfile(src=self.url, dest=self.destiny)

        # do base class stuff (validate, etc.)
        super(FileArtifact, self).prepare()