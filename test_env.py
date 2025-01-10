import os


print("Cloud Name:", os.environ.get('CLOUDINARY_CLOUD_NAME'))
print("API Key:", os.environ.get('CLOUDINARY_API_KEY'))
print("API Secret:", os.environ.get('CLOUDINARY_API_SECRET'))