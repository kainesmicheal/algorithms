def search(main,pattern,prime,array,index):
    patLen = len(pattern)
    strLen = len(main)
    charIndex = 0
    patHash = 0
    strHash = 0
    h = 1
	    
    for i in range(0,patLen-1):
        h = (h*256) % prime
	
    for i in range(0,i<patLen):
        patHash = (256 * patHash + ord(pattern[i])) % prime;
        strHash = (256 * strHash + ord(main[i])) % prime;

    for i in range(0,i<=(strLen - patLen)):
        if(patHash == strHash):

            for charIndex in range(0, charIndex < patLen):
                if(main[i+charIndex] != pattern[charIndex]): 
                    break
			    
            if (charIndex == patLen):
                index = index + 1
                array[index] = i
		
        if (i < (strLen - patLen)):
            strHash = (256 * (strHash - ord(main[i])*h) + ord(main[i+patLen])) % prime; 
            if(strHash < 0):
                strHash += prime;
    return array
