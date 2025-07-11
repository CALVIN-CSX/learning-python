#learning this module to learn how to move a file(013.move_a_file) using watchdog
import shutil
#print(help(shutil))
#shutil.copy("Move_me_shutil.txt", "you_copied_me.txt")#copies file
#shutil.copytree() #copies directory, same as filecopy
#shutil.move("Move_me_shutil.txt","Watchme/you_moved_me.txt")
#shutil.rmtree('mylocalpath/learning-python')
shutil.copystat("you_copied_me.txt","Watchme/you_moved_me.txt")#doesn't change content inside
#shutil.chown(path: 'you_copied_me.txt', user='learner') #only possible in linux
print(shutil.which("python"))
#shutil.make_archive()#makes archive
#shutil.unlink("Watchme/you_moved_me.txt")#unpackes archive







