price = {'a':23, 'b':40, 'c':67}

def service_price():
    service = input('서비스 종류를 입력하세요. a/b/c: ')
    value_added = input('부가세를 포함합니까? y/n :')
    if value_added == 'y' :
        result = price[service] * 1.1
    elif value_added == 'n' :
        result = price[service]
    else:
        pass
    print(round(result,1),'만 원입니다.')

service_price()