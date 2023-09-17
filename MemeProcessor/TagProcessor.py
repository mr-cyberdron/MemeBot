from MemeProcessor.MemeExtensionProcessor import MemeExtensionProcessor

class TagProcessor:
    """
    Meme tags processor.
    """

    @staticmethod
    def generate(path):
        # Generate meme tags.
        file_name_tags_mass = TagProcessor.get_filename_tags(path)
        tagsLine = ','.join(file_name_tags_mass)
        return tagsLine

    @staticmethod
    def get_filename_tags(path: str):
        processed_filename = path.split('/')[-1]
        ext_list = list(MemeExtensionProcessor.extensions.keys())
        for ext_to_replace in ext_list:
            processed_filename = processed_filename.replace('.'+ext_to_replace,'')
        return [processed_filename, "textTag"]

