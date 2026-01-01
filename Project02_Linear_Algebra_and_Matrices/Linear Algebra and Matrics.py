## The Social Graph & Interest Profiler
import stat_funcs as sf
'''
Network Density: How "connected" are our users?
User Similarity: Who should we recommend as a "friend" based on their interests?
'''

# Phase 1: DATA Architecture....

user_interest = [[1,1,0,1],
                 [1,0,0,0],
                 [0,1,1,0],
                 [1,1,1,1]]
user_friendship = [[0,1,0,1],
                   [1,0,1,0],
                   [0,1,0,1],
                   [1,0,1,0]]


# Phase 2: Technical Requirements

## done in stat_funcs.py module and also imported here.

# Phase 3: Industry Style Deliverables...

print("--- SOCIAL ANALYTICS REPORT ---")
print(f"1. Trending Interests Score: {sf.get_popular_interests(user_interest)}")
print(f"2. Connection Status (User 0 & 2): {sf.is_connected(user_friendship,0,2)}")
print(f"3. Recommendation for User 1: User {sf.find_soulmate(1,user_interest)[0]} (Distance: {sf.find_soulmate(1,user_interest)[1]})")
print("-" * 31)

'''
--- SOCIAL ANALYTICS REPORT ---
1. Trending Interests Score: [3, 3, 2, 2]
2. Connection Status (User 0 & 2): False
3. Recommendation for User 1: User 0 (Distance: 1.41)
-------------------------------
'''
