
# Linear Regression



## Loss Function

Quantifies the distance between the real and predicted values of the target. The most common loss function is the *Squared Error*.

$$\hat y^{(i)} = Prediction$$
$$y^{(i)} = Real Label$$
$$
\ell^{(i)}(w, b) \;=\; \frac{1}{2}\Bigl(\hat y^{(i)} - y^{(i)}\Bigr)^2
$$

To measure the quality of a model on the entire dataset of 𝑛 examples, we simply average (or equivalently, sum) the losses on the training set

$$
L(w, b) = \frac{1}{n}\sum_{i=1}^{n}{\ell^{(i)}(w, b)}
$$

$$
pro_{i=1}^{n}{}
$$

