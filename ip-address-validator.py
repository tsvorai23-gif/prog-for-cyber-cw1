# B01888101 Tristan Svorai
# Lab exercise 4
# # Task 4
# 09/10/2026

"""This function validates that an ip adress has been entered by looking for . 4 parts numbers only and numbers between 0 and 255."""
def validate_ip(ip):
	ip = ip.strip()

	if "." not in ip or ip.count(".") != 3:
		return False

	parts = ip.split(".")
	if len(parts) != 4:
		return False

	for part in parts:
		if not part.isdigit():
			return False

		try:
			number = int(part)
		except ValueError:
			return False

		if number < 0 or number > 255:
			return False

	return True
"""This is the main function which asks for the ip adress input and informs the user wether the ip adress is valid or not, if not it loops the user untill a valid one is entered."""
def main():
	while True:
		ip_address = input("Enter an IP address: ")
		if validate_ip(ip_address):
			print("Valid IP address")
			break
		print("Invalid IP address. Please try again.")
	input ("Press enter to exit")

if __name__ == "__main__":
	main()
