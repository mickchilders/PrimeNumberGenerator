import timeit

square = 1
root = 1
nextadd = 1
num = 2
count = 0

while 1:
  start = timeit.default_timer()
  num += 1    
  factor = False  
  if num > square:
    nextadd += 2
    root +=1
    square += nextadd
  for i in range(2,num):
    if num % i == 0:
      factor = True
      break
  if factor == False:
    end = timeit.default_timer()
    elapsed = end - start
    elapsedstr = "  Elapsed Time: {0:5.3f} sec".format(elapsed)
    count +=1
    print(count, num, elapsedstr)