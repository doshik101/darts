x=int(input("Enter the number of games: "));
for i in range(x):
    n=int(input("Enter the number of sectors "));
    k=int(input("Enter the black sector number "));
    max=-100;
    print("Enter the ", n, " sectors");
    if (k == -1):
       A = list(map(int, input().split()));
       for i in range(n):
           sum = 0;
           for j in range(n):
               d=i+j;
               if d > n-1:
                   d=d-n;
               sum = sum + A[d];
               if sum > max:
                    max=sum;
       print(max);
    else:
        A = list(map(int, input().split()));
        A[k]=min(A);
        if A[k]>0:
            A[k]=0;
        for i in range(n):
            sum = 0;
            for j in range(n):
                d = i + j;
                if d > n - 1:
                    d = d - n;
                sum = sum + A[d];
                if sum > max:
                    max = sum;
        print(max);
