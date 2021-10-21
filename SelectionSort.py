def sortNum(x):
    Min=0
    num=0
    
    for i in range(len(x)):
        Min=x[i]
        for j in range (len(x)):
            if (j>i):
                if (x[j]<Min):
                    Min= x[j]
                    num=j
        if (Min != x[i]) :
            x[num]=x[i]
            x[i]=Min

    return x


def main():
    a=[1232323,232,1212,121234, -2, 0 ,- 1000000000000000, 10000000000000000000]

    print(sortNum(a))

if __name__ == "__main__":
    main()


    

    
