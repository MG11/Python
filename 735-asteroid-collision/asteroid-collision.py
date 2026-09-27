class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        output = []
        for a in asteroids:
            appenda = True
            while output and output[-1] > 0 and a < 0:
                if abs(a) > output[-1]:
                    output.pop()
                elif abs(a) == output[-1]:
                    output.pop()
                    appenda = False
                    break
                elif output and abs(a) < output[-1]:
                    appenda = False
                    break
            output.append(a) if appenda else None
        return output
