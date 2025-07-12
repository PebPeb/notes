
# Multilayer Perceptrons (MLP)


A multilayer perceptron is stacking multiple layers on top of one another. With each layer feeding the layer on top of the other. The first `L - 1` layers are the representation and the final layer is the linear predictor.

![alt text](image.png)

Since the input layer does not preform any calculations in it the image above is depicting a two layer MLP. Every neuron influences every neuron of the layer below it.


$n =$ number of examples \
$d =$ number of input features \
$X \in \mathbb{R}^{n \times d}$

$h =$ number of hidden representations (units) \
$H \in \mathbb{R}^{n \times h}$

$H = XW^{(1)} + b^{(1)}$ \
$O = HW^{(2)} + b^{(2)}$

## Linear to Nonlinear

Going directly from one layer to another layer produces a affine function (linear relation ship). Going from one affine function to another affine function results in just a affine function which is a linear relationship. To avoid this a nonlinear *activation function $\sigma$* needs to be applied to each hidden layer unit after the affine transformation. The output is referred to as *activations*.


$H = \sigma(XW^{(1)} + b^{(1)})$ \
$O = HW^{(2)} + b^{(2)}$

## Activation Functions

Activation functions decide whether a neuron should be activated or not by calculating the weighted sum and adding bias to it.

### ReLU Function

The *rectified linear unit*


### Sigmoid Function



