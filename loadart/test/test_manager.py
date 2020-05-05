import pytest

import os
import loadart as L
from loadart.manager import Manager

def test_manager_setup():
    root = os.path.dirname(L.__file__)
    m = Manager(os.path.join(root, 'test','res','test_manager_assets_1.json'))
    assert m

def test_manager_download():
    root = os.path.dirname(L.__file__)
    m = Manager(os.path.join(root, 'test','res','test_manager_assets_1.json'))
    result = m.prepare_all()
    m.save_datafile()
    assert result == True

def test_manager_status_read():
    root = os.path.dirname(L.__file__)
    m = Manager(os.path.join(root, 'test','res','test_manager_assets_1.json'))
    for a in m.artifact_list:
        assert a.available == True
