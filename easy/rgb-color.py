from typing import List
import bisect

class Solution:
    doubles = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
    def similarRGB(self, color: str) -> str:
        s="#"
        for i in range(1, 7, 2):
            
            x = int(color[i:i+2], 16)
            idx = bisect.bisect_left(self.doubles, x)
            if idx==0:
                s += "00"  
            else:
                a = x - self.doubles[idx-1]
                b = self.doubles[idx]-x
                if a<=b:
                    s += '{:02x}'.format(self.doubles[idx-1]) 
                else:
                    s += '{:02x}'.format(self.doubles[idx]) 
        return s
    
s = Solution()
print(s.similarRGB("#09f166")) # "#11ee66"
print(s.similarRGB("#000000")) # "#000000"