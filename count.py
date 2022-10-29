def countDigits(n):
   ans = 0
   while (n):
      ans = ans + 1
      n = n // 10
   return ans
n = “45758”
print("Number of digits in the given number :", countDigits(n))
