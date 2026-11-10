# B01888101 Tristan Svorai
# Lab exercise 5
# # Task 3
# 20/10/2026

"""Dictionary containing event information."""
event = {"username": "admin", "ip_address": "192.168.10.15", "event_type": "login", "severity_risk": "high"}

#This function displays the event information in a readable format
def display_event_info(event):
    """Display event information."""
    print("Event Information:")
    for key, value in event.items():
        print(f"{key}: {value}")

#main function to run the program
def main():
    """Main function to run the program."""
    display_event_info(event)
    print(f"Total number of key-value pairs: {len(event)}")

if __name__ == "__main__":
    main()

#adding a feild to the dictionary called status
event["status"] = "active"

#updating the severity_risk field to medium
event["severity_risk"] = "medium"

#display remaing keys and values in the dictionary
for key, value in event.items():
    print(f"{key}: {value}")

#display total number of key-value pairs in the dictionary
print(f"Total number of key-value pairs: {len(event)}")