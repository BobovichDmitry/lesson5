from function import copy_file_or_folder
import os
import random
import string
import shutil
import uuid
from function import *


def test_copy_file_or_folder():
    name_what_copy = str(uuid.uuid4())
    os.mkdir(name_what_copy)
    name_new_copy = str(uuid.uuid4())
    copy_file_or_folder(name_what_copy, name_new_copy)
    assert os.path.exists(name_new_copy)
    os.rmdir(name_what_copy)
    os.rmdir(name_new_copy)


def test_add_money():
    assert add_money(500, 1000) == 1500


def test_buy_item():
    assert buy_item(300, 500) == 200


