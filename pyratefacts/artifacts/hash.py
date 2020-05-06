import hashlib
from enum import Enum, unique

def hash_digest(filename, hash_algorithm):
    if hash_algorithm not in hashlib.algorithms_available:
        raise ModuleNotFoundError("Requested hash '{}' is not available. Available algorithms are: ".format(hash_algorithm, hashlib.algorithms_available))

    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    m = hashlib.new(hash_algorithm)
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            m.update(data)
    
    return m.hexdigest().lower()

def available_algorithms():
    return hashlib.algorithms_available