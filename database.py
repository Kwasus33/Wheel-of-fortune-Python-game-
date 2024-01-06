from Utilities import read_from_csv, read_from_json
import os.path


class FilePathNotFound(FileNotFoundError):
    pass


class FilePathIsDirectory(IsADirectoryError):
    pass


class Database():
    def __init__(self) -> None:
        """
        Creates instance of Database
        """

    def load_from_file(self, path: str) -> list:
        """
        Depending on file extension, redirects to proper function
        Returns list of values read from file
        Raises FileNotFoundError if path is invalid or file does not exist
        Raises PermissionError if user cannot open the file
        Raises IsADirectoryError if path leads to directory not file
        """
        ext = os.path.splitext(path)[:-1]
        try:
            with open(path, 'r') as file_handle:
                if ext == 'json':
                    words = read_from_json(file_handle)
                else:
                    words = read_from_csv(file_handle)
            return words
        except FileNotFoundError:
            raise FilePathNotFound("Could not open file")
        except PermissionError:
            msg = 'You do not have permission to open the file'
            raise PermissionError(msg)
        except IsADirectoryError:
            raise FilePathIsDirectory('Can only work on files')
