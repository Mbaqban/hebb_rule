# Hebb_rule
implementation of Hebb_rule algorithm in python


## Installation

its script dont need installation

## Usage

```python

Dataset = [
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
]
Outputs = [
    -1,
    1,
    -1,
    -1
]


andnot_net = HebbRule(
    dataset=Dataset,
    outputs=Outputs
)

andnot_net.train()
andnot_net.get_info()
andnot_net.test()

```
this data set and outputs refers to andnot logical oprator <br>
NOTE : the outputs must be bipolar

![image](https://user-images.githubusercontent.com/32582182/120983187-b58afb80-c78e-11eb-9cde-305450f48be4.png)
