def main():
    
    t = int(input())
    
    while t:
        
        s = input()
        n = len(s)
        
        count = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                count += 1
                
        print(count)
        
        t -= 1
        
main()
