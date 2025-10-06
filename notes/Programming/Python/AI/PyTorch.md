
**NOTE SOME TEXT IS PULLED DIRECTLY FROM PYTORCH [DOCUMENTATION](https://docs.pytorch.org/tutorials)**

# PyTorch

To define a neural network in PyTorch, we create a class that inherits from [nn.Module](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)

Below are a few examples of some of the options PyTorch allows for inheritance.

``` python
class NeuralNetwork(nn.Module):
  ...
class Encoder(nn.Module):
  ...
class Decoder(nn.Module):
  ...
class Discriminator(nn.Module):
  ...

```

## Tensors
Tensors are a specialized data structure that are very similar to arrays and matrices. In PyTorch, we use tensors to encode the inputs and outputs of a model, as well as the model’s parameters.

