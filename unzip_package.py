import sys
import os
import zipfile
from xml.dom import minidom

def parse_xml(path):
    dom = minidom.parse(path)
    child = dom.getElementsByTagName('assemblyIdentity')
    for items in child:
        print 'Name: ', items.getAttribute('name')
        print 'Version: ', items.getAttribute('version')
        print 'PublicKeyToken: ', items.getAttribute('publicKeyToken')
    
    child = dom.getElementsByTagName('supportedOS')
    for items in child:
        print 'Id: ', items.getAttribute('Id')
    
def read_dir(dest_path):
    dir_list = []
    file_list = []
    for files in os.listdir(dest_path):
        if files.endswith('.xml'):
        	parse_xml(os.path.join(dest_path,files))        
    for root, folders, files in os.walk(dest_path):
        dir_list.extend(folders)
        file_list.extend(files)
    for dirs in dir_list:print 'folder: ', dirs
    for files in file_list:print 'file: ', files
    
def extract_file(file_name):
    extract_to = os.path.dirname(os.path.abspath(file_name))+ '/' +os.path.splitext(file_name)[0]
    if zipfile.is_zipfile(file_name) and file_name.upper().endswith('.ZIP'):
        zf = zipfile.ZipFile(file_name, 'r')
        zf.extractall(extract_to)
        read_dir(extract_to)
        zf.close()

if __name__ == '__main__':
    try:
        extract_file('new.zip')
    except Exception, e:
        print e.__str__()
