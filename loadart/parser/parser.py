import json
import os

from urllib.parse import urlparse
from enum import Enum, unique

from ..artifacts import hash
from ..artifacts.ops import TeardownOp
from ..downloaders import HttpArtifact, FileArtifact
from ..manager.datafile import Datafile

@unique
class ArtifactOrigin(Enum):
    FILE = {'descriptor': 'file', 'class': FileArtifact}
    HTTP = {'descriptor': 'http', 'class': HttpArtifact}


class Parser():
    def _json_parse(self, filepath):
        with  open(filepath, 'r') as f:
            data = f.read()

        obj = json.loads(data)
        return obj

    def __init__(self, filepath):
        required_keys = ['name', 'url', 'destiny', 'origin']
        self.artifact_list = []

        json_dict = self._json_parse(filepath)
        self.datafile_filename = json_dict.get('datafile', None)

        for json_artifact in json_dict.get('artifacts', None):
            for k in required_keys:
                if k not in list(json_artifact.keys()):
                    raise KeyError("Required key {} not available.".format(k))

            destiny = json_artifact['destiny']
            if os.path.exists(destiny) and os.path.isdir(destiny):
                # no filename was provided, must get one
                url_obj = urlparse(json_artifact['url'])
                filename = os.path.basename(url_obj.path)
                filename = filename.replace(os.pathsep, '')
                destiny = os.path.join(destiny, filename)

            str_origin = str(json_artifact['origin']).lower()
            origin_options = {}
            for x in ArtifactOrigin:
                origin_options[x.value['descriptor']] = x.value['class']

            if str_origin in origin_options.keys():
                origin = origin_options[str_origin]
            else:
                raise LookupError("Invalid origin: {}. Valid options are: {}".format(str_origin, origin_options))

            str_teardown = str(json_artifact.get('teardown', 'none')).lower()
            if str_teardown in [x.value for x in TeardownOp]:
                teardown = TeardownOp(str_teardown)
            else:
                raise LookupError("Invalid teardown options: {}. Valid options are: {}".format(str_origin, [x.value for x in TeardownOp]))

            artifact = origin(
                name = json_artifact['name'],
                url = json_artifact['url'],
                destiny = destiny,
                uncompress = json_artifact.get('uncompress', False),
                uncompress_dir=json_artifact.get('uncompress_dir', None),
                hash_type = json_artifact.get('hash_type', None),
                digest = json_artifact.get('digest', None),
                teardown = teardown)

            self.artifact_list.append(artifact)
        
    def list_artifacts(self):
        return self.artifact_list

    def get_datafile(self):
        if self.datafile_filename:
            datafile = Datafile(self.datafile_filename)
        else:
            datafile = Datafile()
        return datafile

        
    