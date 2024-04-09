def topKFrequent(nums, k):
	dic = {}
	top = []
	for num in nums:
		if str(num) not in dic:
			dic[str(num)] = 1
		else:
			dic[str(num)] += 1
	sortedDic = (dict(sorted(dic.items(), key=lambda x: x[1])))
	for i in range(1,k+1):
		top.append(int(list(sortedDic.keys())[-i]))
	print(top)
	return top

topKFrequent([1,1,1,2,2,3], 2)