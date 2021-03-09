import requests
import json

# a tuple since we will not need to change this
cat_t = ('users', 'posts', 'albums', 'photos')

def cleanup(**kwargs): # or def cleanup(category='users', id=0)
    '''
    clean up incoming data
    Expects 'category' and 'id' as keyword arguments
    'category' must be a string that matches values in cat_t
    'id' must be an integer 1-8 inclusive
    '''
    # check we have the expected arguments
    if 'category' in kwargs and kwargs['category'] in cat_t:
        category = kwargs['category'].lower() # force it to lower case
    else:
        category = 'users'
    if 'id' in kwargs: # check we have the expected keyword argument
        try: # catch exceptions when we try to cast the value as an integer
            id = int( float(kwargs['id']) ) # cannot just use int()
            if id not in range(1,9): # stop before 9
                id = 1 # set a sensible default
        except Exception as err:
            print(err) # we are not obliged to print anything
            id = 1 # set a sensible default
        finally: # we do not have to use finally - it can be left out
            pass # pass is useful if we need to have a block that does nothing
    else: # if no argument called 'id' was provided, use sensible defaults
        id = 1
    data = {'category':category, 'id':id} # build a dictionary
    return data

def get_data(category, id):
    # print(category, id)
    url = 'https://jsonplaceholder.typicode.com'
    param = category
    id = id
    full_path = '{}/{}/{}'.format(url, param, id)
    j = 'no data'
    try:
        res = requests.get(full_path)
        j = res.json() # we just want the json data
    except Exception as err:
        print('Something went wrong. ', err)
    finally:
        return j

if __name__ == '__main__':
    # use our sanitize module to clean up some data
    # ask the user for a category and an id
    which_cat = input('which category? ')
    which_id  = input('which id (1-8)? ')

    cleaned = cleanup(category=which_cat, id = which_id)
    # print(cleaned)

    # make a request and return the json
    data = get_data(category = cleaned['category'], id = cleaned['id'])
    print(data)
    # append this to a text file
    data_str = json.dumps(data)
    fout = open('data.txt', 'at')
    fout.write(data_str)
    fout.close()