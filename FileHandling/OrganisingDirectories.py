import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS" : ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', 'm4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4', '.mkv'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

def pickDirectory(value):

    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

print(pickDirectory('.mp3'))

def organizeDirectory():

    for item in os.scandir():


        filepath = Path(item)

        filetype = filepath.suffix.lower()  # .suffix returns the file extension
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)

        if directoryPath.is_dir() is False:
            directoryPath.mkdir()
        filepath.rename((directoryPath.joinpath(filepath)))

targetDir = "C\\Users\\aparida\\OneDrive\\Code\\Coding\\Pyhton\\Course Files\\Python_Automation_Files\\Exercise Files\\OrganizeMe"

organizeDirectory()

