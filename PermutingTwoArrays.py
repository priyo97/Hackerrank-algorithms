def main():
    
    t = int(input())
    
    while t:
        
        n,k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        flag = [0]*n
        
        for i in range(n):
            c = 9999999999
            idx = -1
            for j in range(n):
                
                if a[i]+ b[j] >= k and b[j] < c and not flag[j]:
                    c = b[j]
                    idx = j
            
            if idx == -1:
                print("NO")
                break
            else:
                flag[idx] = 1
        
        else:
            print("YES")
    
            
        t -= 1
        
main()
