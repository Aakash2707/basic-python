def sin(x,n=10):
   s=0
   for a in range(1,n+1):
      s+=(((-1)**(a+1))*(x**(2*a-1)))/facTay(a)
   return s


def facTay(n):
   s=1
   n=2*n-1
   for x in range(1,n+1):
      s*=x
   return s
