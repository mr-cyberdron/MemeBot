import os

import pandas as pd
import numpy as np
import env

# @todo add function generate_tags()
class FileSystemDatabase:

    def process_database(self):
        meme_short_paths = self.get_db_memes_path_list()

        tags_file_path = env.root + env.tags_file
        tags_file = pd.read_csv(tags_file_path)
        tag_paths = list(tags_file['path'].to_numpy())
        # Get paths that not exist in db.
        file_paths_to_append = set(meme_short_paths).difference(set(tag_paths))

    '''
    Get shorty meme paths from folder.
    '''
    def get_db_memes_path_list(self):
        paths = []
        # Absolute root memes folder path.
        meme_dir = os.getcwd() + env.local_base_dir

        # Absolute meme types folder paths.
        dirs = [path for path in os.listdir(meme_dir) if os.path.isdir(meme_dir + path)]

        for dir in dirs:
            files = os.listdir(meme_dir + dir)
            for file in files:
                # Get meme db short path.
                db_file_path = (meme_dir + file).split('/')
                db_file_path = os.path.join('/', db_file_path[-3], db_file_path[-2], db_file_path[-1])
                paths.append(db_file_path)

        return paths

    def get_unprocessed_paths(self):
        # @todo move code here, write files to csv

        pass

