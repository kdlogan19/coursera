'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. '''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = {}
hourlist = []
for lines in handle:
    if lines.startswith('From'):
        words = lines.split()
        #print(words)
        if (len(words)>4):
            hours = words[5].split(':')
            #print(hours)
            hourlist.append(hours[0])


for hour in hourlist:
  result[hour] = result.get(hour,0) + 1

#print(result)
result = sorted([(k,v) for (k,v) in count.items()])
for x in result:
  print(x[0], x[1])
 

