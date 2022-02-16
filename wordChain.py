def longestStringChain(strings):
	
	strings.sort(key= lambda x: len(x)) 
	chainLengths = {string:1 for string in strings}
	sequence = {string:string for string in strings}
	maxLength, maxString = -float('inf'), None 
	
	for s in strings: 
		for i in range(len(s)): # omit character i 
			omitString= s[0:i] + s[i+1:]
			if chainLengths.get(omitString, 0): # if omitString exists in strings 
				if chainLengths.get(omitString)+1 > chainLengths[s]: 
					chainLengths[s] = chainLengths.get(omitString)+1
					sequence[s] = omitString 
		if maxLength < chainLengths[s]: 
			maxLength = chainLengths[s]
			maxString = s 
			
	
	 # get the sequence of strings
	s, res = maxString, []
	if s == sequence[s]: 
		return []
	while s != sequence[s]:
		res.append(s)
		s = sequence[s]
	res.append(s)
	return res 
