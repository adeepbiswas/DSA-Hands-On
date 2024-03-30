"""
Logic -

To move the biggest disk to the final position-
1. move all the smaller disks to a temporary third location
2. move the biggest disk to the required destination
3. move all the smaller disks from the temporary location to the final destination (on top of the largest disk already moved there)

Pseudo Code-

Parameters - 
n - number of disks to be moved
src - source location
dst - destination location
tmp - temporary location

hanoi(n, src, dst, tmp):
    if n == 0:
        return
    else:
        hanoi(n-1, src, tmp, dst)
        move(disk n, src, dst)
        hanoi(n-1, tmp, dst, src)
        
Time Complexity- O(2^n) 
Space Complexity- O(1)

Referrence -

1. https://www.youtube.com/watch?v=YstLjLCGmgg
2. https://www.geeksforgeeks.org/time-complexity-analysis-tower-hanoi-recursion/?ref=next_article

"""

def hanoi(n:int, src:str, dst:str, tmp:str) -> None:
    if n == 0:
        return
    else:
        hanoi(n-1, src, tmp, dst)
        print(f'moving disk {n} from {src} to {dst}')
        hanoi(n-1, tmp, dst, src)
        

hanoi(2, 'Tower A','Tower B','Tower C')