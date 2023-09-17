class MemeExtensionProcessor:
    """
    Meme extension processor.
    """

    extensions = {
        'mp4': 'video',
        'mp3': 'audio',
        'jpeg': 'image'
    }

    @staticmethod
    def get_type(path):
        # Get file extension.
        ext = path.split('.')[-1]
        try:
            return MemeExtensionProcessor.extensions[ext]
        except KeyError:
            return None

