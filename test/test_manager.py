import pytest

import os
import pyratefacts as L
from pyratefacts.manager import Manager

def test_manager_setup():
    m = Manager(os.path.join('test','res','test_manager_assets_1.json'))
    assert m

def test_manager_download():
    m = Manager(os.path.join('test','res','test_manager_assets_1.json'))
    result = m.prepare_all()
    m.save_datafile()
    assert result == True

def test_manager_status_read():
    m = Manager(os.path.join('test','res','test_manager_assets_1.json'))
    for a in m.artifact_list:
        assert a.available == True
