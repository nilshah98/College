def create_space_state_tree(candidates, target):
	res = []
	candidates.sort(reverse=True)
	remsum = sum(candidates)
	dfs(candidates,target,0,[],res, remsum)
	return res

def dfs(nums,target,index,path,res, remsum):
	if sum(path)>target or (remsum+sum(path))<target:
		print("Not possible",*path)
		return
	if sum(path)==target:
		res.append(path)
		return
	for i in range(index,len(nums)):
		dfs(nums,target,i+1,path+[nums[i]],res, remsum - nums[i])

print("Enter the elements")
elements = list(map(int, input().split()))
print("Enter target sum")
targetSum = int(input())

res = create_space_state_tree(elements,targetSum)
print("Accepted subsets")
for i in res:
	print(*i)