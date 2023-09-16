from os import listdir
from os.path import isfile, join
import env
class FileSystemDatabase:

    def __init__(self):
        pass

    def generate_file(self):
        audio_paths = listdir(env.audio_dir)
        video_paths = listdir(env.video_dir)

        return audio_paths



a = FileSystemDatabase
b = a.generate_file
input(b)