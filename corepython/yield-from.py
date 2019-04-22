
def average_gen():
    print('3')
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        print('5')
        count += 1
        total += new_num
        average = total/count

def proxy_gen():
    while True:
        print('2')
        yield from average_gen()

def main():
    print('1')
    calc_average = proxy_gen()
    next(calc_average)
    print('4')
    print(calc_average.send(10))
    print('2 done')
    print(calc_average.send(20))
    print(calc_average.send(30))

if __name__ == '__main__':
    main()
1
2
3
4
5
10.0
2 done
5
15.0
5
20.0
