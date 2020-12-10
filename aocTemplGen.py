import sys
import os

def fileStr(dayNum):
  return f"""
def day{dayNum}a(input):
  pass

def day{dayNum}b(input):
  pass

input=\"\"\"
\"\"\"
print(day{dayNum}a(input))
print(day{dayNum}b(input))"""

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception('needs a file prefix, e.g "python aocTemplGen.py 1" with create file with name "day1.py"')
  dayNum = sys.argv[1]
  with open(f'day{dayNum}.py', 'w') as file:
    file.write(fileStr(dayNum))
  print("file created")
