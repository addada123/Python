def fbv(n)->int:
    low = 0
    high = n
    answer = 0
    mid = (high + low) / 2
    while low <= high and answer <= n:
        if(mid != 4 or mid != 5):
            low = mid + 1
        elif(mid == 4 or mid == 5):
            answer = mid + 1
            high = mid - 1
    return answer

print(fbv(5))