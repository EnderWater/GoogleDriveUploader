from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

googleAuthenticator = GoogleAuth()
drive = GoogleDrive(googleAuthenticator)

googleFolder = '1zLxyOsxYqPM4oK5Jwn2FCJQGGp43pnDp'
# Put the path to the upload file here:
upload_file = ''

gfile = drive.CreateFile({'parents': [{'id': googleFolder}], 'title': 'main.py'})
gfile.SetContentFile(upload_file)
gfile.Upload()
