def square_it(func):
    '''
    this function takes another function as an argument
    then square the result of the other function
    '''
    def inner_fn(*args, **kwargs):
        # we could do some work on the args and kwargs if we wanted
        result = func(*args, **kwargs)
        return result * result # i.e. the square
    return inner_fn

@square_it # here we add a decorator function to our function
def mean(nums):
    '''
    find the mean of a bunch of numbers
    '''
    how_many = len(nums)
    total = 0
    for num in nums:
        total += num
    average = total/how_many
    return average

if __name__ == '__main__':
   print( mean( (1,2,3,4,5) ) ) # 3.0
