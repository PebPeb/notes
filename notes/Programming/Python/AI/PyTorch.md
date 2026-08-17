
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

## Captum

### Feature Attribution

This is what tells you what caused the model to make the desision that it made. Explaining the output in terms of individual input features.

- Which words in this input question were the most significant in deciding the answer?
- Which pixels in this input image drove the model's classification of the image?
- Which features of the input data were most significant to my regression model's prediction?

### Layer Attribution

Explains activity of hidden layser in terms of individual input features.

