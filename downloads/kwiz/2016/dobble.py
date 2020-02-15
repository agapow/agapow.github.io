from random import shuffle

SYMBOLS_PER_CARD = 5
row_cnt = 0

POSN_MATRIX = {k:[] for k in range (SYMBOLS_PER_CARD)}
N = SYMBOLS_PER_CARD - 1

# def rotate(l, n):
#     return l[-n:] + l[:-n]

def rearrange (r):
   global POSN_MATRIX
   while True:
      collision = False
      for i in range (SYMBOLS_PER_CARD):
         sym_i = r[i]
         if sym_i in POSN_MATRIX[i]:
            collision = True
            break
      if collision:
         shuffle (r)
      else:
         for i in range (SYMBOLS_PER_CARD):
            sym_i = r[i]
            POSN_MATRIX[i].append (sym_i)
         return r


def print_row (r):
   global row_cnt
   shuffle (r)
   print ('\t'.join ([chr(ord('A') + x) for x in r]))
   #print ("%s: %s" % (row_cnt+1, rearrange (r)))
   row_cnt += 1


for i in range (N):
   for j in range (N):
      row = []
      for k in range (N):
         row.append (((i*k + j) % N) * N + k)
      row.append (N * N + i)
      print_row (row)


for i in range (N):
   row = []
   for j in range (N):
      row.append (j * N + i)
   row.append (N*N + N)
   print_row (row)

row = []
for i in range (N+1):
   row.append (N*N + i)
print_row (row)
