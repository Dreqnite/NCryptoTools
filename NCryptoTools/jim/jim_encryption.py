"""
Module for functions which are related to cryptography and hashing.
"""
import os
import hashlib
import binascii


class Hasher:
    """
    Performs data hashing with needed algorithm, salt size and amount of rounds.
    """
    def __init__(self, data, salt_bytes=b'', salt_size=16, algorithm='sha256', rounds=100000):
        """
        Constructor.
        @param data: data to be hashed.
        @param salt_bytes: salt.
        @param salt_size: size of salt to be generated.
        @param algorithm: algorithm which hashes data (e.g. SHA256).
        @param rounds: amount of hashing rounds.
        """
        self._data_bytes = data.encode()
        self._salt_size = salt_size if len(salt_bytes) == 0 else len(salt_bytes)
        self._salt_bytes = self.generate_salt() if len(salt_bytes) == 0 else salt_bytes
        self._algorithm = algorithm
        self._rounds = rounds

    @property
    def data_bytes(self):
        """
        Gets initial data as bytes.
        @return: initial data as bytes.
        """
        return self._data_bytes

    @property
    def salt_size(self):
        """
        Gets salt size.
        @return: salt size.
        """
        return self._salt_size

    @property
    def salt_bytes(self):
        """
        Gets salt bytes.
        @return: salt bytes.
        """
        return self._salt_bytes

    @property
    def algorithm(self):
        """
        Gets used hashing algorithm name.
        @return: hashing algorithm name.
        """
        return self._algorithm

    @property
    def rounds(self):
        """
        Gets amount of rounds.
        @return: amount of rounds.
        """
        return self._rounds

    def generate_salt(self):
        """
        Generates random salt of needed length. It's highly recommended to use
        salt of size 16 or more.
        @return: salt of needed size.
        """
        return os.urandom(self._salt_size)

    def set_salt_size(self, new_size):
        """
        Sets new salt size. By default salt size is 16.
        @param new_size: new salt size.
        @return: None.
        """
        self._salt_size = new_size

    def set_algorithm(self, new_algorithm):
        """
        Sets new hashing algorithm which should be used to hash data.
        @param new_algorithm: hashing algorithm name.
        @return: None
        """
        self._algorithm = new_algorithm

    def set_rounds(self, new_rounds):
        """
        Sets new amount of rounds to be executed in the process of hashing.
        @param new_rounds: new amount of hashing rounds.
        @return: None.
        """
        self._rounds = new_rounds

    def hash(self):
        """
        Generates hash from the input data.
        @return: hashed data.
        """
        hashed_data = hashlib.pbkdf2_hmac(self._algorithm,
                                          self._data_bytes,
                                          self._salt_bytes,
                                          self._rounds)
        return binascii.hexlify(hashed_data)
