------------------------------------------------------------------------------------

[Google colab notebook link](https://colab.research.google.com/drive/1XRiQbkJ8RK09voKzAN4SFfKpIXJmGMlm?usp=sharing)

## basic read.md like file so that user can understand the program

### Warning

<div class="alert alert-block alert-warning">
<b>make sure you don't touch (modify,erase or other manipulations) the first code below unless untill you understand the code in python and posses goog grip over python</b>
</div>



there are 4 types covered in this program i.e.

1. Trapezoidal rule
2. simpson's 1/3 method
3. simpson's 3/8 method
4. Weedle's method


> comming to how to usee this,
the second cell, probably the last cell of program where it is written;


```python
# Trap(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# sim13(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# sim38(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# weedle(a=0,b=6,fn=("1/(1+(x**2))"),n=6)
```


> go to the cell, and remove the # sign with 'backspace'


### how to activate a perticular function

> say you want to use Trapazoid method, after erasing # sign , cell will look like this

```python

 Trap(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# sim13(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# sim38(a=0,b=6,fn=("1/(1+(x**2))"),n=6)

# weedle(a=0,b=6,fn=("1/(1+(x**2))"),n=6)
```

> once it looks like this, means other functions are in inactive mode and Trapazoid method function is in active mode

> so now you can change parameters you want to and 'Run' The cell,
<div class="alert alert-block alert-success">
    more on equation and parameters at <strong>ADD EQN</strong> section
</div>

<div class="alert alert-block alert-info">
To run the cell, you can use 'ctrl+Enter' (that is first press control key and hold it and press enter key) or You can use Run button on the upper side of the notebook
</div>

### ADD EQN

below are listed some common things that u need to take care

1. firstly before running cell, on ``Kernel`` select `Restart and Run All`.
2. while writing eqn strictly take care about brackets, use only `()` brackets and use more often than in literal maths, for example;
    
in maths you can write $ 1+1/x $ ;
but i strictly advice you to write it as `1+(1/x)` or more clearly `(1+(1/x))`

also some symbol changes with respect to maths are
$X^2$ is `x**2`
functions like sin,cos,log,exp are written as 

$cos x$ = `cos(x)`

$ln x$ = `log(x)`

$log_{10} x$ = `log(x,10)`

$log_{a} x$ = `log(x,a)`

$e^x$ = `exp(x)`

$e^{x^2}$ = `exp(x**2)`

$x^{1/2}$ = `sqrt(x)` = `x**(1/2)`

$x^{1/n}$ = `x**(1/n)`

$ sin^{-1} x$ = `arcsin(x)`

also one main thing
to multiply two variables or brackets you have to put * sign in between,

$RC$ is not eq to `RC`

$RC$ is not eq to `R*C`

$\displaystyle\frac{(x^2)(sin x)}{2x}$ is not eq to `(x**2)(sin(x))/(2x)`

$\displaystyle\frac{(x^2)(sin x)}{2x}$ is eq to `( (x**2)*(sin(x)) )/(2x)`

for your convienience here are some big functions or complex looking functions

$sin( exp(1+(x^{t/R^2C^2}) ))$ = `sin(exp(1+(x**(t/(R*C)))))`

$\log_{10}(\sin x^e)$ = `log(sin(x**e),10)`
