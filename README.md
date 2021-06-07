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
this data set and outputs erfers to andnot logical oprator

