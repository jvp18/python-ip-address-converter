# Bit converter to decimal for IP Addresses

# Assumes a valid IPv4 address in binary format:
# 32 bits divided into four 8-bit octets

# Prompt the user for a binary IP address
ip_address = input("Enter IP address: ")

# Store the converted octets
converted_ip_address = []

# Initialise the binary place value and octet total
total_bit = 0

# We set the initial bit as 128 since we know the value of the first bit in an octet is 128
initial_bit = 128

# Iterate through each character in the IP address
for bit in ip_address:
    if bit == '1':
        # Add the current binary place value to the octet total
        total_bit += int(initial_bit)
        # Move to the next binary place value (128, 64, 32, 16...)
        initial_bit /= 2
    elif bit == '0':
        total_bit += 0
        initial_bit /= 2

    else:
        # Append the completed octet and its separator
        converted_ip_address.append(str(total_bit))
        converted_ip_address.append('.')
        # Reset values for the next octet
        initial_bit = 128
        total_bit = 0

# # Append the final octet (which has no trailing separator)
converted_ip_address.append(str(total_bit))

# Join the converted octets into a single IP address string
converted_ip_address = "".join(converted_ip_address)

# Display the converted IP address
print(converted_ip_address)
