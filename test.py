my_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
matchers = ['abc','def']
matching = [s for s in my_list if any(xs in s for xs in matchers)]
print(matching)
