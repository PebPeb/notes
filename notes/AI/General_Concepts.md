

## Training

### Gradients

The gradient is used by the model to make changes during the *Backwardpass*. This is computed using the loss of the model, and then applied using a optimizer.

A simple example of using *gradients* in Pytorch.

``` python

```


### Parameters

**Batch Size**

When talking about *Batch Size* this refers to the number of training examples processed by the model in a single forward and backward pass before the model's weights are updated.

Practically when using Pytorch this would be the time before applying the gradient.


**Epochs**

*Epochs* are just the number of times the model has ran through the entire data set.