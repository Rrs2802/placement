def fun(arr, ss):
   for i in range(len(arr)):
       s = sum(ss[i:])
       arr[i] = chr(((ord(arr[i]) - 97 + s) % 26) + 97)
   return ''.join(arr)


s = input()
shifts = list(map(int, input().split()))
print(fun(list(s), shifts))
