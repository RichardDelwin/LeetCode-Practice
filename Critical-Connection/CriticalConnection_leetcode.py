from typing import List


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
	d = {}
	for connection in connections:
		
		if connection[0] in d:
			d[connection[0]].append(connection[1])
		else:
			d[connection[0]] = [connection[1]]

		if connection[1] in d:
			d[connection[1]].append(connection[0])
		else:
			d[connection[1]] = [connection[0]]
		
	print(d)
	
	critical  = []
	
	for key, val in d.items():
		
		if len(val)==1 and [val[0], key] not in critical:
			critical.append([key, val[0]])
	
	return critical



if __name__ == "__main__":

	n = 4
	l = [[0,1],[1,2],[2,0],[1,3]]

	sol = criticalConnections(n, l)
	print(sol)