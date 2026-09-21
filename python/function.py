def sum(a,b, *args, **kwargs):
    sum = a + b
    for i in args:
        sum += i
    print(sum)

    print(kwargs)
    for k,v in kwargs.items():
        sum += v
    print(sum)

sum(2, 3, 4, 10, 11, d=10, x=20, y=1)

def info(**kwargs):
    for k , v in kwargs.items():
        print(k , "=", v)

info(Name = "Ayush Pun", Roll_No = "10", TP_No = "NPI000325", )