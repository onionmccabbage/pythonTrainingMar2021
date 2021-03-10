from localWeather import LocalWeather

def main():
    '''
    invoke the LocalWeather class to create instances of local weather reports
    '''
    w_edi = LocalWeather('Edinburgh', 'uk', 'rainy', -3.7)
    w_gal = LocalWeather('Galway', 'ie', 'humid', 5)
    w_kt = LocalWeather('Kingston', 'jm', 'sunny', 32)
    w_default = LocalWeather('Begonia', '__', True)
  
    print(w_edi)
    print(w_gal)
    print(w_kt)
    print(w_default)

if __name__ == '__main__':
    main()

