times = 0
for i in range(5):
  ipt = input()
  sh, sm, eh, em = int(ipt[:2]),  int(ipt[3:5]),  int(ipt[6:8]),  int(ipt[9:11])
  time = (eh-sh)*60 +(em-sm)
  times += time
print(times)