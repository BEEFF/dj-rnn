import torch

# Uninitilised 5x3 matrix
x = torch.empty(5, 3)
#print(x)

#5x3 randomly initialised matrix
x = torch.rand(5, 3)
#print(x)

# Construct a matrix filled zeros and of dtype long:
x = torch.zeros(5, 3, dtype=torch.long)
#print(x)

#Construct a tensor directly from data:
x = torch.tensor([5.5, 3])
#print(x)

x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

# get size
print(x.size())

y = torch.rand(5, 3)
print(x + y)


x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())