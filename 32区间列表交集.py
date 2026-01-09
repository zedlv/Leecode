#区间列表交集
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        list = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            stard = max(firstList[i][0],secondList[i][0])
            end =  min(firstList[i][1],secondList[i][1])
            if stard <= end:
                list.append([stard,end])
            if firstList[i][1] < secondList[i][1]:
                i += 1
            else:
                j += 1
        return list

        