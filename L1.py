
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)

        if x > y:
            nums1, nums2, x, y = nums2, nums1, y, x
        low = 0
        high = x
        while low <= high:
            px = (low + high) // 2
            py = (x + y + 1) // 2 - px

            maxleftX = float('-inf') if px == 0 else nums1[px - 1]
            maxleftY = float('-inf') if py == 0 else nums2[py - 1]
            minrightX = float('inf') if px == x else nums1[px]
            minrightY = float('inf') if py == y else nums2[py]

            if maxleftX <= minrightY and maxleftY <= minrightX:
                if (x + y) % 2 == 0:
                    return (max(maxleftX, maxleftY) + min(minrightX, minrightY)) / 2
                else:
                    return max(maxleftX, maxleftY)
            elif maxleftX > minrightY:
                high = px - 1
            else:
                low = px + 1
        return 0
