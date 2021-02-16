"""__init__ module"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
# list of valid models
models_dict = storage.valid_models()
