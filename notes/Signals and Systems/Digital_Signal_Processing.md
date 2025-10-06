# Digital Signal Processing

## Examples

### Digital FIR 

$$y[n]=A*x[n] + B*x[n-1]$$

``` python
A = 10
B = 10
curSample = 0
prevSample = 0

...

def newSample(sample):
  prevSample = curSample
  curSample = sample

  y = A * curSample + B * prevSample
  return y
```

$$y[n]=A*x[n] + B*x[n-1]$$

Z-transform

$$\Zeta\{y[n]\}=\Zeta\{A*x[n] + B*x[n-1]\}$$
$$Y(z)=A*X(z) + B*z^{-1}X(z)$$
$$Y(z)=X(z)(A + B*z^{-1})$$

Transfer function

$$H(z)=\frac{Y(z)}{X(z)}=A + B*z^{-1}$$
$$H(z)=A + B*z^{-1}$$
$$H(z)=\frac{Az + B}{z}$$


### Digital IIR 

$$y[n]=A*x[n] + B*x[n-1] + y[n-1]$$

``` python
A = 10
B = 10
curSample = 0
prevSample = 0
prevY = 0
curY = 0
...

def newSample(sample):
  prevSample = curSample
  curSample = sample
  prevY = curY

  curY = A * curSample + B * prevSample + prevY
  return curY
```

$$y[n]=A*x[n] + B*x[n-1] + y[n-1]$$

Z-transform

$$y[n] - y[n-1]=A*x[n] + B*x[n-1]$$
$$\Zeta\{y[n] - y[n-1]\}=\Zeta\{A*x[n] + B*x[n-1]\}$$
$$Y(z)-z^{-1}Y(z)=A*X(z) + B*z^{-1}X(z)$$
$$Y(z)(1-z^{-1})=X(z)(A + B*z^{-1})$$

Transfer function

$$H(z)=\frac{Y(z)}{X(z)}=\frac{A + B*z^{-1}}{1-z^{-1}}$$
$$H(z)=\frac{A + B*z^{-1}}{1-z^{-1}}$$
$$H(z)=\frac{Az + B}{z-1}$$

