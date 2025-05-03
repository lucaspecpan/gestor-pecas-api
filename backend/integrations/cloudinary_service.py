# backend/integrations/cloudinary_service.py
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
import base64

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)

def upload_image(base64_file, filename):
    header, encoded = base64_file.split(",", 1)
    decoded_file = base64.b64decode(encoded)
    result = cloudinary.uploader.upload(decoded_file, public_id=filename)
    return result