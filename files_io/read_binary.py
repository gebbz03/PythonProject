with open('rbinary','rb') as fobj:
    binary_data=fobj.read()
    decoded_data=binary_data.decode('utf-8')
    print(decoded_data)