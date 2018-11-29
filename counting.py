def showfilename(link):
    txt = link.split('/')
    return txt[-1]

url = "http://www.google.com/a.txt"
print(showfilename(url))

''' url should be array, need to store the filenames to array and count it '''