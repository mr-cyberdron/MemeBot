import os
import pandas as pd
import env
from MemeProcessor.TagProcessor import TagProcessor as tag_processor
from MemeProcessor.MemeExtensionProcessor import MemeExtensionProcessor as meme_ext_processor
import re

class FileSystemDatabase:
    """
    Csv db processor.
    """

    @staticmethod
    def process_database():
        # Upload new memes to csv database.
        meme_short_paths = FileSystemDatabase.get_db_memes_path_list()
        meme_short_paths_to_append = FileSystemDatabase.get_unprocessed_paths(meme_short_paths)
        FileSystemDatabase.append_unprocessed_paths(meme_short_paths_to_append)

    @staticmethod
    def get_db_memes_path_list():
        # Get shorty meme paths from folder.
        paths = []
        # Absolute root memes folder path.
        meme_dir = os.path.join(env.root, env.local_base_dir)
        # Absolute meme types folder paths.
        dirs = [path for path in os.listdir(meme_dir) if os.path.isdir(os.path.join(meme_dir, path))]
        for dir in dirs:
            files = os.listdir(os.path.join(meme_dir, dir))
            for file in files:
                # Get meme db short path.
                delimiters = r'[/,\\]'
                db_file_path = re.split(delimiters, (meme_dir + file))
                db_file_path = os.path.join('/', db_file_path[-3], db_file_path[-2], db_file_path[-1])
                db_file_path = db_file_path.replace("\\", "/")
                paths.append(db_file_path)

        return paths

    @staticmethod
    def get_unprocessed_paths(meme_short_paths):
        # Get memes paths that not exist in csv db.
        tags_file_path = os.path.join(env.root, env.tags_file)
        tags_file = pd.read_csv(tags_file_path)
        tag_paths = list(tags_file['path'].to_numpy())
        # Get paths that not exist in db.
        return set(meme_short_paths).difference(set(tag_paths))

    @staticmethod
    def append_unprocessed_paths(unprocessed_paths):
        # Load unprocessed memes to csv db.
        csv_path = os.path.join(env.root, env.tags_file)
        meme_csv = pd.read_csv(csv_path)
        meme_rows = {
            'path': [],
            'tags': [],
            'type': []
        }
        for unprocessed_path in unprocessed_paths:
            # Create csv row.
            meme_type = meme_ext_processor.get_type(unprocessed_path)
            if meme_type is None:
                # Skip iteration if meme type not found.
                continue
            meme_rows['path'].append(unprocessed_path)
            meme_rows['tags'].append(tag_processor.generate(unprocessed_path))
            meme_rows['type'].append(meme_type)

        new_memes_df = pd.DataFrame(data=meme_rows)
        memes_appended_base = pd.concat([meme_csv, new_memes_df], ignore_index=True, axis=0)
        # Write appended base to csv file.
        memes_appended_base.to_csv(csv_path, index=False)
