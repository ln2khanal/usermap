import shutil
import tempfile
import time
import uuid


FILE_UPLOAD_DIR = '/tmp/'


def __validate_extension(source, extension):
    """
    checks if the source ends with extension or not
    :returns boolean value
    """
    return source.lower().endswith(extension.lower())


def handle_uploaded_file(source):
    """
    saves an uploaded file to filesystem and returns its path after saving.
    """
    file_name_ext = source.name.rsplit('.', 1)
    file_name = str(uuid.uuid4())
    if len(file_name_ext) == 2:
        file_name = "%s.%s" % (file_name, file_name_ext[1])
    fd, file_path = tempfile.mkstemp(prefix="%s_" % int(time.time()), suffix=file_name, dir=FILE_UPLOAD_DIR)
    with open(file_path, 'wb') as destination:
        shutil.copyfileobj(source, destination)
    return file_path


def validate_file(source):
    """
    validates if the source file is valid or not
    """
    valid_extension = __validate_extension(source, '.xlsx')

    return valid_extension
