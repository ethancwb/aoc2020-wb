def day13a(input):
  time, busList = input.split('\n')
  time, idList = int(time), [int(x) for x in busList.split(',') if x != 'x']
  minWaitTime, timeIdx = float('inf'), -1
  for idx, waitTime in enumerate(map(lambda x: (time // x + 1) * x - time if time // x != 0 else 0, idList)):
    if waitTime < minWaitTime:
      minWaitTime = waitTime
      timeIdx = idList[idx]
  return minWaitTime * timeIdx


def day13b(input):
    _, busList = input.split('\n')
    buses = [int(x) for x in busList.split(',') if x != 'x']
    modulus = 1
    for b in buses:
        if b != 0:
            modulus *= b

    timestamp = 0
    for b in buses:
        if b != 0:
            timestamp += -buses.index(b) * (modulus // b) * \
                pow(modulus // b, -1, b)

    return timestamp % modulus


input = """1000511
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,19,x,x,x,23,x,x,x,x,x,x,x,353,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"""

print(day13a(input))
print(day13b(input))
