import cloudinary
import cloudinary.uploader
from io import BytesIO
from PIL import Image

cloudinary.config( 
    cloud_name = "dzroteq7m", 
    api_key = "933156664919953", 
    api_secret = "DDGHMTaSxF3YlC3YYcwdZkPNiZs",
    secure=True
)

def getImage(image):
    try:
        pil_image = Image.open(BytesIO(image))
        buffer = BytesIO()
        pil_image.save(buffer, format="JPEG")
        buffer.seek(0)
        
        upload_result = cloudinary.uploader.upload(buffer, resource_type="image")

        return upload_result["secure_url"]
    
    except Exception as e:
        print("Error in getImage:", str(e))
        return None
