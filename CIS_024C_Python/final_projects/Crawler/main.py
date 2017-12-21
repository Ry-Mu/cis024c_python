import os

"""
What this program will do, is basically going to go through all of the pages of a website and gather up all the links.
This will be useful for those looking to make a site map or a custom search engine. This is a core program.
"""

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


create_project_dir('thenewboston')