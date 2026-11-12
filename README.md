# Task 3 – IP Address Validator

## Student Details

Name: Tristan Svorai

Campus: New Collage Lanarkshire

Banner ID: b01888101

## Description

This program performs basic IPv4 address validation using a user-defined function called validate_ip().

The function accepts an IP address as a parameter and checks if it follows the basic structure of an IPv4 address.

The program uses string operations, conditional statements and a function to determine whether the entered IP address meets the required validation checks.

## Features

The program performs the following checks:

- Checks if the IP address contains dots.

- Checks that there are exactly three dots.

- Checks that the address contains four numbers (octets).

- Checks that each number is between 0 and 255.

- Returns True for an address that passes the checks.

- Returns False if the address fails validation.

## Example Inputs and Outputs

IP Address

Expected Result

192.168.1.10

Valid

192.168.1.300

Invalid

192.168.1

Invalid

192.168.one.10

Invalid

10.0.0.1

Valid

Note: This exercise performs basic IPv4 format validation rather than a complete network or IP address validation system.

## How to Run

### Requirements:

- Python 3 installed.

- Visual Studio Code or another Python-compatible editor.

### Instructions:

- Open the ip-address-validator branch.

- Download or clone the repository.

- Open the Python program in Visual Studio Code.

- Open the terminal.

- Run the program: "python ip_address_validator.py"

## Testing and Evidence

The program has been tested using:

- A correctly formatted IPv4 address.

- An address containing more than three dots.

- An address containing fewer than three dots.

- An address containing letters instead of numbers.

- An address containing a number greater than 255.

- An address containing negative numbers.

- An address containing unnecessary spaces.

Screenshots of the validation results are included in this branch.

## Files

- Python implementation.

- README.md – Task documentation.

- LICENSE – Repository licence.

- Testing screenshots.

