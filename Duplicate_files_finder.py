import hashlib, os
 
def file_hash(filename):
  h_sha256 = hashlib.sha256()
  with open(filename,'rb') as f:
    chunk = 0
    while chunk != b'':
      chunk = f.read(1024) 
      h_sha256.update(chunk)
  return h_sha256.hexdigest()


def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))                                                                         
    return r


folder = input("\n Enter folder or directory path: ")
files=list_files(folder)
hd={'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855':'Empty File'}

if os.name == 'nt':        #check if OS is windows
    a='\\'
else:
    a='/'


os.mkdir(folder+a+"Duplicate_files")
f=open(folder+a+"Duplicate_files"+a+"Detailed_Log.txt",'a')
f.write("ORIGINAL FILE                                                                                                                                                                                                             DUPLICATE FILE\n\n\n")

p=0
d=0
for file in files:
  h=file_hash(file)
  p+=1
  print("Scanning files in this folder: ", p, end='\r')
  if h not in hd:
    hd[h]=file
  elif h in hd:
    d+=1
    f.write(str(d)+")  "+hd[h]+"                           IS SAME AS                        " + file+"\n\n")
    os.replace(file, folder+a+"Duplicate_files"+a+file.split(a)[-1])
    
f.close()    
#print (hd)
print("\n\n Total number of duplicate files found: ", d)
print('\n All duplicate files have been moved to',folder+a+'Duplicate_files folder')
