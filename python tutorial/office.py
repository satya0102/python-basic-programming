def solve():
    # Read input
    N, M = map(int, input().split())
    
    # Create friendship graph
    friends = {i: [] for i in range(N)}
    
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    
    # Read the target rostering value
    K = int(input())
    
    # Day 1 all employees work from the office
    current_day = [1] * N  # 1 means WFO, 0 means WFH
    
    total_rostering = N  # On day 1, all employees work from office
    days = 1  # We've already done Day 1
    
    # Simulate the days
    while total_rostering < K:
        next_day = []
        
        # Calculate the attendance for the next day based on today's attendance
        for i in range(N):
            # Count how many of the friends worked from office
            friends_wfo = sum(1 for f in friends[i] if current_day[f] == 1)
            
            if current_day[i] == 1:  # WFO today
                if friends_wfo == 3:
                    next_day.append(1)  # Stay WFO
                else:
                    next_day.append(0)  # Work from home
            else:  # WFH today
                if friends_wfo < 3:
                    next_day.append(1)  # Work from office
                else:
                    next_day.append(0)  # Stay WFH
        
        # Update current day and calculate the rostering value
        current_day = next_day
        total_rostering += sum(current_day)
        days += 1
    
    # Output the number of days
    print(days)

