import os

"""
Each website you crawl is a separate project (folder). New folder = new project/
Each website you crawl you actually only have two files and that is the queue and the crawled files. And inside
these files are just a list of links.

The only link that we give the program is a homepage link. It needs a starting point.

Need two types of information. project name and base_url. we need this because we need to give it a starting point.
"""

# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url): #Need two types of information. project name and base_url. We need this because we need to give it a starting point.
    queue = os.path.join(project_name , 'queue.txt') #
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue): #This is saying does queue file exist already? If not, create it.
        write_file(queue, base_url) #base_url so when the program first starts, will have 1 url waiting list(homepage).
    if not os.path.isfile(crawled): #This is saying does crawled file exist already? If not, create it.
        write_file(crawled, '') #We pass it as an empty file because if we just go ahead nad make it and throw a url in there, the program will think we crawled this already.

# Create a new file
def write_file(path, data): #takes in file name and data you want to write to it.
    with open(path, 'w') as f: #
        f.write(data)
        f.close()



# Add data onto an existing file
def append_to_file(path, data): #calling this when you want to stick a new link to the end of the file
    with open(path, 'a') as file:
        file.write(data + '\n') #has each link on a new line


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read in a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f: #read text-file
        for line in f: #iterate through a file one line at a time
            results.add(line.replace('\n', '')) #removing /n because it was added in the append_to_file func.
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links): #sort links we gathered before we write them to the file
            f.write(l+"\n")
