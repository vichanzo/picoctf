# https://www.geeksforgeeks.org/program-to-perform-a-letter-frequency-attack-on-a-monoalphabetic-substitution-cipher/

# Python3 program for the above approach 

# Function to decrypt a monoalphabetic 
# substitution cipher using the letter 
# frequency attack 
def printString(S, N):
	
	# Stores final 5 possible deciphered 
	# plaintext 
	plaintext = [None] * 5
	
	# Store the frequency of each letter in 
	# cipher text 
	freq = [0] * 26
	
	# Stores the frequency of each letter 
	# in cipher text in descending order 
	freqSorted = [None] * 26
	
	# Store which alphabet is used already 
	used = [0] * 26
	
	# Traverse the string S 
	for i in range(N):
		if S[i] != ' ':
			freq[ord(S[i]) - 65] += 1
			
	# Copy the frequency array		 
	for i in range(26):
		freqSorted[i] = freq[i]
		
	# Stores the string formed from 
	# concatenating the english letters 
	# in the decreasing frequency in the 
	# english language	 
	T = "ZGSOCXPQUYHMILERVTBWNAFJDK"
	
	# Sort the array in descending order 
	freqSorted.sort(reverse = True)
	
	# Iterate over the range [0, 5] 
	for i in range(5):
		ch = -1
		
		# Iterate over the range [0, 26] 
		for j in range(26):
			if freqSorted[i] == freq[j] and used[j] == 0:
				used[j] = 1
				ch = j
				break
			
		if ch == -1:
			break
		
		# Store the numerical equivalent of letter
		# at ith index of array letter_frequency 
		x = ord(T[i]) - 65
		
		# Calculate the probable shift used 
		# in monoalphabetic cipher 
		x = x - ch
		
		# Temporary string to generate one 
		# plaintext at a time 
		curr = ""
		
		# Generate the probable ith plaintext 
		# string using the shift calculated above 
		for k in range(N):
			
			# Insert whitespaces as it is 
			if S[k] == ' ':
				curr += " "
				continue
			
			# Shift the kth letter of the 
			# cipher by x 
			y = ord(S[k]) - 65
			y += x
			
			if y < 0:
				y += 26
			if y > 25:
				y -= 26
			
			# Add the kth calculated/shifted 
			# letter to temporary string	 
			curr += chr(y + 65)
			
		plaintext[i] = curr
	
	# Print the generated 5 possible plaintexts	 
	for i in range(5):
		print(plaintext[i])

# Driver code

# Given string 
S = "B TJNQMF NFTTBHF"
N = len(S)

# Function Call 
printString(S, N)

# This code is contributed by Parth Manchanda

