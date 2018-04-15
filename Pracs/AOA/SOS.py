def combination_sum(candidates, target):
	res = []
	candidates.sort(reverse=True)
	remsum = sum(candidates)
	dfs(candidates,target,0,[],res, remsum)
	return res

def dfs(nums,target,index,path,res, remsum):
	print(path)
	if sum(path)>target or (remsum+sum(path))<target:
		return
	if sum(path)==target:
		res.append(path)
		return
	for i in range(index,len(nums)):
		dfs(nums,target,i+1,path+[nums[i]],res, remsum - nums[i])

# print("Enter the elements")
elements = list(map(int, input().split()))
# print("Enter target sum")
targetSum = int(input())

res = combination_sum(elements,targetSum)
print(res)