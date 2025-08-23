class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits[:]:
            for basket in baskets[:]:
                if fruit <= basket:
                    fruits.remove(fruit)
                    baskets.remove(basket)
                    break
                
        return len(fruits)
