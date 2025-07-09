import time
print(time.ctime(0))          #converts seconds into string format
print(time.time())            #returns current seconds since epoch
                              #epoch=reference point
print(time.ctime(time.time()))
localtime=time.localtime() #fetches local time
formatedlocaltime=time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(formatedlocaltime)
utctime=time.gmtime()
print(utctime)
formatedutctime=time.strftime("%Y-%m-%d %H:%M:%S", utctime)
print(formatedutctime)
#strftime stands for str-string f-format and time=>time
#Time Functions
#strptime function
timestring="5 june 2025" #allows and string to be converted into time
stringtime=time.strptime(timestring,"%d %B %Y")
print(stringtime)
formatedstringtime=time.strftime("%Y-%m-%d %H:%M:%S", stringtime)
print(formatedstringtime)
#time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
tupletime=(2025,5,5,0,0,0,0,0,0)
time_tuple=time.asctime(tupletime)
print(time_tuple)