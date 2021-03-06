class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num.sort()
        return num[(len(num)-1)/2]

class SolutionMoore:
	def majorityElement(self, num):
		count=0
		current = None
		for n in num:
			if count == 0:
				current = n
				count += 1
			elif current == n:
				count += 1
			else:
				count -= 1
		return current

x = [4,5,1,2,1,1,1,3]
s = SolutionMoore()
print(s.majorityElement(x))