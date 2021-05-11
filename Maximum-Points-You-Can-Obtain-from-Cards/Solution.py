class Solution:

    def maxScore(self, cardPoints, k) -> int:

        window_size = len(cardPoints) - k
        rem_points = sum(cardPoints[window_size:])
        
        highest = rem_points

        for i in range(k):

            rem_points = rem_points - cardPoints[window_size + i] + cardPoints[i]
            highest = max(highest, rem_points)

        return highest


obj = Solution()
cardPoints = [96, 90, 41, 82, 39, 74, 64, 50, 30]
k = 8
print(obj.maxScore(cardPoints, k))
