from collections import defaultdict, deque

def day10a(input):
  numList = sorted(list(map(lambda x: int(x), input.split('\n'))))
  diffs = defaultdict(int)
  prev = 0
  for n in numList:
    diffs[n - prev] += 1
    prev = n
  diffs[3] += 1
  return diffs[1] * diffs[3]

def day10b(input):
  numList = sorted(list(map(lambda x: int(x), input.split('\n'))))
  n = len(numList)
  dp = [0] * (n - 1) + [1]

  for i in reversed(range(n)):
    for j in range(i+1, n):
      if numList[j] - numList[i] > 3:
        break
      dp[i] += dp[j]

  res = 0
  for i in range(n):
    if numList[i] > 3: break
    res += dp[i]
  return res

input = """73
114
100
122
10
141
89
70
134
2
116
30
123
81
104
42
142
26
15
92
56
60
3
151
11
129
167
76
18
78
32
110
8
119
164
143
87
4
9
107
130
19
52
84
55
69
71
83
165
72
156
41
40
1
61
158
27
31
155
25
93
166
59
108
98
149
124
65
77
88
46
14
64
39
140
95
113
54
66
137
101
22
82
21
131
109
45
150
94
36
20
33
49
146
157
99
7
53
161
115
127
152
128"""
print(day10a(input))
print(day10b(input))