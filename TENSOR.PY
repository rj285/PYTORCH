import torch

# t1 = torch.tensor(4.)
# # print(t1) #tensor(4.)
# # print(type(t1)) #<class 'torch.Tensor'>

# #vector
# t2 = torch.tensor([1.,2,3,4])
# # print(t2) #tensor([1., 2., 3., 4.])
# # print(t2.shape) #torch.Size([4])
# # print(type(t2)) #<class 'torch.Tensor'>
# # print(type(t2.shape)) #<class 'torch.Size'>

# #matrix
# t3 = torch.tensor([[1.,2],[4,5],[9,10]])
# # print(t3)
# '''
# tensor([[ 1.,  2.],
#         [ 4.,  5.],
#         [ 9., 10.]])
# '''
# # print(t3.shape) #torch.Size([3, 2])
# # print(type(t3)) #<class 'torch.Tensor'>


# #3d array

# t4 = torch.tensor([[11,12,13],[14,15,16],[17,18,19],[20,21,22],])
# # print(t4)
# '''
# tensor([[11, 12, 13],
#         [14, 15, 16],
#         [17, 18, 19],
#         [20, 21, 22]])
# '''
# # print(t4.shape) #torch.Size([4, 3])
# # print(type(t4)) #<class 'torch.Tensor'>


# x = torch.tensor(3.)
# w = torch.tensor(4., requires_grad=True)
# b = torch.tensor(5.,requires_grad=True)

# y = w * x + b

# #comute derivatives
# y.backward()
# print(type(y))#<class 'torch.Tensor'>

#access gradients
# print('dy/dw:', w.grad)
# print('dy/db:', b.grad)
'''
dy/dw: tensor(3.)
dy/db: tensor(1.)
'''
# print(type(w.grad)) #<class 'torch.Tensor'>
# print(type(b.grad)) #<class 'torch.Tensor'>

a = torch.tensor([[1.,2],[3,4]], requires_grad=True)
b = torch.tensor([[5.,6],[7,8]], requires_grad=True)
z = torch.sum(a * b)

z.backward()
print('dy/dw:', a.grad)
print('dy/db:', b.grad)
'''
dy/dw: tensor([[5., 6.],[7., 8.]])
dy/db: tensor([[1., 2.],[3., 4.]])
'''

#random value generating
# r = torch.randn((3, 4, 5))
# print(r)
'''
tensor([[[ 1.0215, -0.2940, -0.8350,  2.7115, -0.1668],
         [-0.0090,  1.4592,  0.3788,  0.1860, -1.0641],
         [-0.2355,  0.0061, -0.2435, -1.0073,  1.4479],
         [ 1.5299, -0.3532, -0.8290,  0.1177, -1.1926]],

        [[ 1.4344,  1.1483,  0.3849,  0.5089, -0.3484],
         [-1.1279,  0.3558, -1.0895, -0.0543, -0.0971],
         [ 2.1336,  0.7224, -0.6732,  0.7358, -0.9227],
         [-0.1474,  0.1157,  0.3571, -0.8325, -0.3784]],

        [[-2.4057,  0.6411, -1.2857, -0.2787,  1.1688],
         [-0.7361,  0.0762,  1.0614,  0.4815, -0.4599],
         [-0.5772,  0.3191,  0.6088,  0.1732,  0.6010],
         [-1.1759,  0.7810,  0.1566, -1.7782,  0.6612]]])
'''

# t = torch.zeros([3,3])
# print(t)
'''
tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])
'''

# s = torch.full((3,3),100)
# print(s)
'''
tensor([[100, 100, 100],
        [100, 100, 100],
        [100, 100, 100]])
'''

# o = torch.ones([3,3])
# print(o)
'''
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
'''