def rectangleIncircle(w,h,r):
    if 2*r>= (w*w + h*h)**.5:
        
        return True
    else:
        return False
w=float(input("ENTER WIDTH OF RECTANGLE:"))
h=float(input("Enter Height of Rectangle:"))
r=float(input("Enter Radius of Circle:"))
print(rectangleIncircle(w,h,r))
