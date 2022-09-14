import oci
import os

config = oci.config.from_file(
    "C:/Users/ivvasque/.oci/config",
    "OCICLI"
)

ident = oci.identity.IdentityClient(config)
user = ident.get_user(config["user"]).data

object_storage = oci.object_storage.ObjectStorageClient(config)
bucket = object_storage.get_bucket("idcci5ks1puo", "oci-bionexo-demo")
namespace = object_storage.get_namespace().data
print("namespace = "+namespace)

""""
Read File
"""

bucket_name = bucket.data.name
file = object_storage.get_object(namespace,bucket_name,"BionexoFileDemo.txt")


print(bucket_name)
print(file.data.text)

object_response = file.data


""""
Read File in subfolders
"""

bucket_name2 = bucket.data.name
file2 = object_storage.get_object(namespace,bucket_name2,"ERP/Plannexo/ReadingFilesInSubfoldersOCI.txt")


print(bucket_name2)
print(file2.data.text)

object_response = file2.data

""""
Write File
"""
text2='Este contenido es relevante en espanol'
object_storage.put_object(namespace, bucket_name, "Demo.txt", text2)

""""
Write File In Subfolders
"""
text3='We are going to create and Write a file in subfolders in OCI Object Storage'
object_storage.put_object(namespace, bucket_name, "ERP/Plannexo/CreateandWriteFile.txt", text3)


"""
Download File from OCI Specific Bucket
"""

destination_path = "C:/Users/ivvasque/Documents/Oracle/Customers/BIONEXO/PythonSDK/"
file_path = os.path.join(destination_path, "biofiloexample.txt")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'wb') as f:
    f.write(object_response.content)
print("Finish Downloading file")

"""
Download File from OCI Specific Bucket in Subfolders
"""

fileToDownloadObj = object_storage.get_object(namespace,bucket_name,"ERP/Plannexo/CreateandWriteFile.txt")
object_responseObjToDownload = fileToDownloadObj.data

destination_path2 = "C:/Users/ivvasque/Documents/Oracle/Customers/BIONEXO/PythonSDK/"
file_path2 = os.path.join(destination_path2, "FileDownloaded.txt")
os.makedirs(os.path.dirname(file_path2), exist_ok=True)
with open(file_path2, 'wb') as f:
    f.write(object_responseObjToDownload.content)
print("Finish Downloading file From Subfolder in Object Storage")


"""
Uploading File from OCI Specific Bucket
"""
with open(file_path,'rb') as f:
    objName = os.path.basename(file_path)
    object_storage.put_object(namespace, bucket_name, objName, f)

print("Finish Uploading file")


"""
Uploading File from OCI Specific Bucket with subfolders
"""
file_origin_path = "C:/Users/ivvasque/Documents/Oracle/Customers/BIONEXO/PythonSDK/"
file_pathObjToUpload = os.path.join(file_origin_path, "Benefits Slide.pptx")

with open(file_pathObjToUpload,'rb') as f:
    objFileUpload = os.path.basename(file_pathObjToUpload)
    object_storage.put_object(namespace, bucket_name, "ERP/Plannexo/"+objFileUpload, f)

print("Finish Uploading file in subfolders")