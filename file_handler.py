# This module will handle file operations.

import os
import os.path as osp
import time


def ensure_directory_exists(directory):
    """
    Ensure that the specified directory exists.
    """
    if not osp.exists(directory):
        os.makedirs(directory)


def open_log_and_data_files(output):
    """
    Open log and data files for writing.
    """
    now_time = time.strftime("%Y-%m-%d")
    logfile = open(osp.join(output, f"{now_time}.log"), "a+", encoding="utf-8")
    datafile = open(osp.join(output, f"{now_time}.txt"), "a+", encoding="utf-8")
    return logfile, datafile


def write_to_file(file, data):
    """
    Write data to a file.
    """
    file.writelines(data)
