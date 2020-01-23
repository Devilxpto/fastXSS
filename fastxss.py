import sys
import urllib.request, urllib.parse
import time
import multiprocessing as mp

file = open(sys.argv[1])

input_url = input("URL to test: (example: https://www.website.com/?=) ")

def multiprocessing_func(line):

	url = input_url + urllib.parse.quote(line)
	result = urllib.request.urlopen(url).getcode()
	print(f"XSS tested: {line}")
	print(f"URL tested: {url}\n")
	print(f"Response status is: {result}\n\n")
	time.sleep(0.1)

processes = []

starttime = time.time()
for line in file:
	print("Adding Process to the list")
    processes.append(mp.Process(target=connect_to_dev, args=[line]))

print("Spawning the Process")
for p in processes:
    p.start()

print("Joining the finished process to the main truck")
for p in processes:
    p.join()

endtime = time.time()

duration = (endtime - starttime)/60

print(f"Processed in {duration} minutes")