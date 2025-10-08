Basic Filtering Commands:
Displaying File Contents:
How would you display the entire content of a file named report.txt?
How would you display only the first 5 lines of log.txt?
How would you display only the last 10 lines of data.csv?
Searching for Patterns:
How would you find all lines containing the word "error" (case-sensitive) in syslog?
How would you find all lines containing "warning" or "critical" (case-insensitive) in app.log?
How would you search for lines that do not contain the string "success" in output.txt?
How would you search for lines starting with "User" in auth.log?
Sorting and Uniqueness:
How would you sort the lines of names.txt alphabetically?
How would you sort numbers.txt numerically in descending order?
How would you display only the unique lines from duplicates.log?
How would you count the occurrences of each unique line in access.log?
Combining Filters (Piping):
Chaining Commands:
How would you display the first 20 lines of large_file.txt and then search for the word "important" within those lines?
How would you list all files in the current directory, sort them by size, and then display only the top 5 largest files?
How would you find all running processes owned by the user "john", and then count how many such processes exist?
Processing Text:
How would you extract the second column (assuming space-separated) from data.tsv and then sort the extracted values?
How would you replace all occurrences of "old_value" with "new_value" in config.ini and display the result (without saving it to a new file)?
How would you count the number of words in document.txt?
Advanced Filtering Concepts:
Regular Expressions:
How would you search for lines containing an IP address pattern in network.log?
How would you extract all email addresses from contacts.txt?
awk and sed:
Using awk, how would you print the first and third fields of data.csv, assuming a comma delimiter?
Using sed, how would you delete all lines containing the word "debug" from debug.log?
Scenario-Based Questions:
You have a log file (server.log) that contains entries with timestamps, log levels (INFO, WARN, ERROR), and messages. How would you:
Filter for all "ERROR" messages from a specific date?
Count the number of "WARN" messages in the entire file?
Extract only the message content of "INFO" level entries?
You have a list of users in /etc/passwd. How would you:
Display only the usernames (first field)?
Find users with a specific shell (e.g., /bin/bash)?
Count the total number of users on the system?
