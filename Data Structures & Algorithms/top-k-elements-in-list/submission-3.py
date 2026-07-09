class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=set(nums)
        m=list(n)
        i=0
        j=0
        z=0
        w=0
        c=[]
        d=[]
        u=[]
        while(i<len(m)):
            s=0
            for j in range(0,len(nums)):
                if (m[i]==nums[j]):
                    s=s+1
            c.append(s)
            i=i+1
        r=dict(zip(m,c))
        p=dict(sorted(r.items(),key=lambda item: item[1], reverse=False))
        d=list(p.keys())
        d=d[::-1]
        print(d)
        while (w<k):
            u.append(d[w])
            w=w+1
        return u
        
         