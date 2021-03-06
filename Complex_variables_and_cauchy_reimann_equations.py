
# Importing necessary libraries

import sympy as sp
import numpy as np
import math
import cmath

"""##Part 1: Complex Variables

"""

#Accessing Real and Imaginary Parts
z1 = 3 + 2j
print(z1.real)
print(z1.imag)

#Using Sympy
print(sp.re(z1))
print(sp.im(z1))

#Calculating the Conjugate of a Complex Number
z2 = 3 + 2j
print(z2.conjugate())
print(sp.conjugate(z2))  #Using Sympy

#Complex Numbers Arithmetic

z1 = 2 + 3j
z2 = 4 + 5j
print(z1 + z2) #Addition
print(z1 - z2) #Subtraction

# z1*z2 = (x1*x2-y1*y2)+(x1*y2+x2*y1)i
print(z1 * z2) #Multiplication

print(z1 /z2) #Division
print(z1**2)  #Exponent

print(abs(z1)) #Magnitude, |z1|

"""###Extracting the Root of a Complex Number

A fourth-degree polynomial $x^4 + 1$, which can be written as an equation $x^4 = -1$, has four complex roots:

$$z_0 = -√2/2 + (√2/2)i$$
$$z_1 = -√2/2 - (√2/2)i$$
$$z_2 = √2/2 + (√2/2)i$$
$$z_3 = √2/2 - (√2/2)i$$

The mathematical formula for finding all complex roots takes advantage of the trigonometric form of complex numbers:

$$z_{k}=r\left(\cos \left(\varphi+\frac{2 \pi k}{n}\right)+j \sin \left(\varphi+\frac{2 \pi k}{n}\right)\right)$$
"""

print(np.roots([1, 0, 0, 0, 1]))  # Coefficients of the polynomial x**4 + 1

print(math.sqrt(1)) #produces error

print(cmath.sqrt(1))

"""###Task 1: Find the three solutions of the equation, $x^3+1=0$"""

print(np.roots([1, 0, 0, 1]))

"""###Converting Between Cartesian and Polar Form

Cartesian Form	$$z = x + yi$$

Polar Form $$
z=x+i y=r(\cos \phi+i \sin \phi)=r e^{i \phi}
$$

$$r=|z|=\sqrt(x^2+y^2)$$

$$
\phi=\tan ^{-1}\left(\frac{y}{x}\right)
$$
"""

z0 = 3 + 2j
angle=math.atan(z0.imag / z0.real)
radius=abs(z0)
print(radius,angle)
radius1, angle1 = cmath.polar(z0)
print(radius1,angle1)
print(cmath.isclose(radius, radius1))
print(cmath.isclose(angle, angle1))

"""###Task 2: Find the equivalent polar form of $z=34+27i$, and convert it back to cartesian form to see if they are equal.

*Hint: You may want to look into `cmath.rect()`, to convert back.*
"""

z1 = 34 + 27j
angle=math.atan(z1.imag / z1.real)
radius=abs(z1)
print(radius,angle)
radius1, angle1 = cmath.polar(z1)
print(radius1,angle1)
print(cmath.isclose(radius, radius1))
print(cmath.isclose(angle, angle1))

print(cmath.rect(radius, radius1))
print(cmath.rect(angle, angle1))

"""##Part 2: Cauchy-Reimann Equations

Given that a function $f$ can be expressed as such,
$$
f(z) = u(x, y) + iv(x, y)
$$

and if a derivative of $f$ exists at $z_0 = (x_0, y_0),$ then the
first-order partial derivatives of the component functions of
$f$, which are $u$ and $v$, must satisfy a pair of equations known
as the Cauchy-Riemann equations.

Let us first take the following:
$$
z_0 = x_0 + iy_0 , $$   
$$∆z = ∆x + i∆y,$$

and,
$$∆w = f(z_0 + ∆z) − f(z_0)$$

Now, assuming that the following derivative exists:
$$
f^{\prime}\left(z_{0}\right)=\lim _{\Delta z \rightarrow 0} \frac{\Delta w}{\Delta z}
$$

Isolating each of the real and imaginary limit components and then finding out their first-order partial derivatives with respect to $x$ then gives us:

$$
\begin{aligned}
\lim _{(\Delta x, \Delta y) \rightarrow(0,0)}\left(R e \frac{\Delta w}{\Delta z}\right) &=\lim _{\Delta x \rightarrow 0} \frac{u\left(x_{0}+\Delta x, y_{0}\right)-u\left(x_{0}, y_{0}\right)}{\Delta x} \\
&=u_{x}\left(x_{0}, y_{0}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
\lim _{(\Delta x, \Delta y) \rightarrow(0,0)}\left(\operatorname{Im} \frac{\Delta w}{\Delta z}\right) &=\lim _{\Delta x \rightarrow 0} \frac{v\left(x_{0}+\Delta x, y_{0}\right)-v\left(x_{0}, y_{0}\right)}{\Delta x} \\
&=v_{x}\left(x_{0}, y_{0}\right)
\end{aligned}
$$

On substituting the previous two equations, we get:

$$f'(z_0) = u_x(x_0, y_0) + iv_x(x_0, y_0) $$

On finding the partial first-derivatives of $u$ and $v$ with respect to $y$,
we get:

$$
\begin{aligned}
\lim _{(\Delta x, \Delta y) \rightarrow(0,0)}\left(R e \frac{\Delta w}{\Delta z}\right) &=\lim _{\Delta y \rightarrow 0} \frac{v\left(x_{0}+\Delta y, y_{0}\right)-v\left(x_{0}, y_{0}\right)}{\Delta y} \\
&=v_{y}\left(x_{0}, y_{0}\right)
\end{aligned}
$$
and
$$
\begin{aligned}
\lim _{(\Delta x, \Delta y) \rightarrow(0,0)}\left(\operatorname{Im} \frac{\Delta w}{\Delta z}\right) &=\lim _{\Delta y \rightarrow 0} \frac{u\left(x_{0}+\Delta y, y_{0}\right)-u\left(x_{0}, y_{0}\right)}{\Delta y} \\
&=v_{y}\left(x_{0}, y_{0}\right)
\end{aligned}
$$

Hence, the equations abides as such:

$$f'(z_0) = −i[u_y(x_0, y_0) + iv_y(x_0, y_0)]$$

By individually equating the real parts and imaginary parts of each
of these two equations of $f'(z_0)$, we get the Cauchy-Riemann equations:

$$u_x(x_0, y_0) = v_y(x_0, y_0) $$
and $$u_y(x_0, y_0) = −v_x(x_0, y_0)$$



###Task 3: Complete the code below:

For this example, we will use a $f(z)$ to find it's Cauchy-Reimann Equations, and thus determining whether it is differentiable or not.



*Hint: You will need `Sympy` to solve this problem. To learn more about `Sympy`, click [here](https://pianofisica.hatenablog.com/entry/2020/05/12/173000#Complex-number)*.
"""

def CR_Equations(f):
  

  
  u= sp.re(f)
  v= sp.im(f)

  u_x= sp.diff(u,x)
  u_y= sp.diff(u,y)
  v_x= sp.diff(v,x)
  v_y= sp.diff(v,y)

  print("f = "+str(f))
  print("u = "+str(u))
  print("v = "+str(v))
  print("u_x = "+str(u_x))
  print("u_y = "+str(u_y))
  print("v_x = "+str(v_x))
  print("v_y = "+str(v_y))

  if (u_x==v_y and u_y== -v_x) :
    return "The function f = "+str(f)+" satisfies the Cauchy–Riemann Equations and is differentiable at z = z0 ∈ C."
  else:
    return "The function f = "+str(f)+" does not satisfy the Cauchy–Riemann Equations, so f is nowhere differentiable."

"""###3.1. Use Cauchy-Riemann equations to prove that $f(z)=z^2$ is differentiable at $z=z_0∈ C.$

###3.2. Use Cauchy-Riemann equations to show that $f(z)=\bar{z}$ is nowhere differentiable.

"""

z = sp.symbols('z', complex=True)
x = sp.symbols('x', real=True)
y = sp.symbols('y', real=True)

z = (x+sp.I*y)

print(CR_Equations(z ** 2))
print(CR_Equations(sp.conjugate(z)))
