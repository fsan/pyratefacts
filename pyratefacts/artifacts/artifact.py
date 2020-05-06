import os
import shutil
from enum import Enum, unique

from . import hash
from .ops import TeardownOp
from .uncompress import uncompress

class Artifact():
    def __init__(self,
                 name : str,
                 url : str,
                 destiny: str,
                 uncompress : bool = False,
                 uncompress_dir : str = None,
                 hash_type : str = None,
                 digest : str = None,
                 teardown : TeardownOp = None):

        self.name = name
        self.url = url
        self.destiny = destiny
        self.available = False
        self.uncompress = uncompress
        if self.uncompress:
            if not uncompress_dir:
                raise AttributeError("If uncompress flag is checked, must inform uncompress_dir")
            self.uncompress_dir = uncompress_dir

        if hash_type:
            if not digest:
                raise AttributeError("If hash_type is set, digest must be informed")

            self.hash_type = hash_type
            if isinstance(digest, str):
                digest = digest.lower()
            self.digest = digest

        self.teardown_op = teardown
    
    def prepare(self):
        # validate
        if not self.validate():
            raise Exception("Validation failed for artifact {}".format(self.name))

        # uncompress
        if hasattr(self, 'uncompress') and self.uncompress:
            uncompress(self.destiny, self.uncompress_dir)

        # tear-down
        self.teardown()

        self.available = True
        return self.available

    def validate(self):
        if hasattr(self, 'hash_type'):
            hash_type = self.hash_type
            digest = hash.hash_digest(self.destiny, hash_type)
            if digest == self.digest:
                return True
            else:
                return False
        else:
            return True

        return False
    
    def teardown(self):
        if hasattr(self, 'teardown_op') and self.teardown_op:
            if self.teardown_op == TeardownOp.NONE:
                pass
            elif self.teardown_op == TeardownOp.CLEAR_DESTINY:
                if os.path.exists(self.destiny):
                    if os.path.isdir(self.destiny):
                        shutil.rmtree(self.destiny)
                    else:
                        os.remove(self.destiny)
                pass
            else:
                raise AttributeError("Invalid teardown operation selected: {}".format(self.teardown))
