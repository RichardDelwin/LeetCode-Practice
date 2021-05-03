from heapq import heappop, heappush, heapify

class Solution:
    
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key= lambda x:x[1])
        heap = []
        heapify(heap)
        
        get_inverted = lambda a, b: [a*-1,b]
        
        tot_duration = 0
        for course in courses:
            
            if tot_duration + course[0] <= course[1]:
                
                tot_duration += course[0]
                heappush(heap, get_inverted(course[0], course[1]))
            
            else:
                if len(heap) > 0:
                    if heap[0][0]*-1>course[0]:
                        ele = heappop(heap)
                        
                        tot_duration -= ele[0]*-1 
                        tot_duration += course[0]
                        
                        heappush(heap, get_inverted(course[0], course[1]))
        
        return len(heap)
        