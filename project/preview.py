from flask import current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from preview_generator.manager import PreviewManager

@login_required
def generate_preview(file_path, name):

    cache_path = os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), "template")
    file_to_preview_path = file_path

    
    manager = PreviewManager(cache_path, create_folder= True)
    path_to_preview_image = manager.get_jpeg_preview(file_to_preview_path)
    print("File_path: ", file_path, "| name: ", name, "| path_to: ", path_to_preview_image)
    # Delete ".stl" from the filename
    # new_name = name[:-4] + '.jpeg'
    os.rename(path_to_preview_image, os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), "template", name))
    return os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), "template", name)