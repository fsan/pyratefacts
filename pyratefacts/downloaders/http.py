import requests

from ..artifacts.artifact import Artifact

class HttpArtifact(Artifact):
    def __init__(self, *args, **kw):
        super(HttpArtifact, self).__init__(*args, **kw)

    def prepare(self, chunk_size=8192, verbose=False):
        # download
        local_filename = self.destiny
        total_downloaded = 0
        with requests.get(self.url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size): 
                    f.write(chunk)
                    total_downloaded += len(chunk)
                    if verbose:
                        print("Downloaded {} bytes to {}".format(total_downloaded, self.destiny))

        # do base class stuff (validate, etc.)
        super(HttpArtifact, self).prepare()