import os
import csv
import hashlib

#Create an md5 hash of files at filepath
def fileHash(filepath, blocksize=4096):
    md5 = hashlib.md5()
    with open(filepath, 'rb') as fp:
        while 1:
            data = fp.read(blocksize)
            if data:
                md5.update(data)
            else:
                break
    return md5.hexdigest()

#Recursively hash all Java files in direcotry path
def dirHash(dirpath):
    files = []
    for root, dirs, filenames in os.walk(dirpath):
        for f in filenames:
            if(f.endswith('.java')):
                files.append(os.path.relpath(os.path.join(root, f), dirpath))

    hashes = []
    for f in files:
        hashes.append(fileHash(os.path.join(dirpath, f)))

    return hashes

#Compares two hash lists
def compare(hash1, hash2):
    return frozenset(hash1) == frozenset(hash2)

#Saves hash list as csv at given path
def saveChecksum(path, hash):
    filename = os.path.join(path, 'checksum.csv') 
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(hash)

#checks source code against build
def isCorrectBuild(src_path, build_path):
    #Get build hash
    build_files = os.path.join(build_path, 'checksum.csv') 
    with open(build_files) as csvfile:
         reader = csv.reader(csvfile)
         build_hash = list(reader)[0]

    src_hash = dirHash(src_path)
    return compare(build_hash, src_hash)
