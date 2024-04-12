#!/usr/bin/python3

import sys
def print_chart(data_points):
    max_val = max(data_points);
    st_ = max_val
    while(st_):
        for each in data_points:
            if(each >= st_):
                print("\u2588",end="");
            else:
                print(" ",end="");
            print(" ",end="")
        print("\n",end="")
        st_-=1;


if __name__ == "__main__":
    print(sys.argv)
    data_ = sys.argv[1]
    print_chart([int(x) for x in data_.split(",")])
