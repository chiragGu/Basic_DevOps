

# Function to convert binary to decimal
def binaryToDecimal(n):
	num = n;
	dec_value = 0;

	base1 = 1;

	len1 = len(num);
	for i in range(len1 - 1, -1, -1):
		if (num[i] == '1'):
			dec_value += base1;
		base1 = base1 * 2;

	return dec_value;

def decimalToBinary(n):

    return bin(n).replace("0b","")



# Driver code
# Function to convert decimal to binary

# Driver Code
#num = "1010101111";
print(binaryToDecimal("10101011"));
print(decimalToBinary(8));
#decToBinary(17);
