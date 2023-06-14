import boto3

# Provide your AWS access key ID and secret access key
access_key_id = 'AKIAUZLCID74EGN6CUFJ'
secret_access_key = 'Hk8cF5xadsNK+LBqbVvwLvx1PreyKyzaXe3ItX+g'
region_name = 'ap-southeast-2'


# Create a session with your credentials
def aws(self):
    session = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region_name
    )

    # Create an S3 client using the session
    s3 = session.client('s3')

    # Specify the bucket name and file key
    bucket_name = 'transportsit1'
    file_key = 'employeeDetails.txt'

    # Download the file to a local path
    local_path = './Utils1/anu.txt'
    s3.download_file(bucket_name, file_key, local_path)

    # Read the contents of the file
    with open(local_path, 'r') as file:
        file_contents = file.read()

    # Print the file contents
    print("*********AWS S3 File Content is as below******* \n", file_contents)
