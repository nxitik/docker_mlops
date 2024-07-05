import os

# Define the six folders
FOLDERS = [
    'data_upload_to_s3',
    'data_extract_from_s3',
    'model_training',
    'model_accuracy',
    'model_deploy_to_flask',
    'dockerize_flask_using_swagger'
]

def create_folders(base_directory='.'):
    """
    Create six folders in the specified base directory.
    
    Parameters:
    base_directory (str): The base directory where folders will be created. Default is current directory.
    """
    for folder in FOLDERS:
        folder_path = os.path.join(base_directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        else:
            print(f"Folder already exists: {folder_path}")



if __name__ == "__main__":
    # Example usage
    create_folders()

