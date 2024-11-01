import shutil

# To delete Faiss After done
def deleteFiles(directory):
    try:
        shutil.rmtree(directory)
        print(f"Directory {directory} deleted successfully.")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")