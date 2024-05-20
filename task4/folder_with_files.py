"""
============================================ №4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

"""

import os
import time

directory = [
    '~/Desktop/test_folder',
]
n = 10


def delete_old_files(directory, n):
    current_time = time.time()
    point_time = current_time - n * 24 * 60 * 60

    for dirpath, dirnames, filenames in os.walk(os.path.expanduser(directory)):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                file_mtime = os.path.getmtime(filepath)
                if file_mtime < point_time:
                    try:
                        os.remove(filepath)
                    except OSError as e:
                        print(f"Error deleting {filepath}: {e}")


delete_old_files(directory, n)
