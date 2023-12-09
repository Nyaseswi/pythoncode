def more_args(**kwargs):
    for i, j in kwargs.items():
      print('{}:{}'.format(i,j))
 
more_args(a=1, b=2)