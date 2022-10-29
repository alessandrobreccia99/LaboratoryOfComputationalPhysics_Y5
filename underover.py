def overflow():
    x=0
    y=1
    try:
      while(x!=y):
          y=2*y
          x=y/2
    except:
      print("The last number before overflow is ", x)
      
def underflow():
    x=0.0
    y=1.0
    while(y!=0):
          x=y
          y=y/2
    print("The last number before underflow is ", x)
    
underflow()
overflow()
