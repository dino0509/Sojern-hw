import sys

if len(sys.argv) != 3:
    print("Please provide 2 version numbers to compare")
    print("Example: python3 script.py 1.1 1.2")
    sys.exit(1)

def versionCompare(v1, v2):
	print("Comparing versions :", v1, "and", v2)
	if v1 == v2:
		return 0

	v1Parts = v1.split(".")
	v2Parts = v2.split(".")
	# check for invalid version numbers, for example 1.2..4 and 1.10. etc
	if('' in v1Parts or '' in v2Parts):
		print("Invalid version number provided")
		sys.exit(1)

	l1 = len(v1Parts)
	l2 = len(v2Parts)
	minParts = min(l1, l2)
	i = 0
	while i < minParts:
		if int(v1Parts[i]) > int(v2Parts[i]):
			return 1
		elif int(v1Parts[i]) < int(v2Parts[i]):
			return -1
		else:
			i += 1
	if l1 > l2:
		return 1
	else:
		return -1

print(versionCompare(sys.argv[1], sys.argv[2]))

# Test Cases:
#print(versionCompare("1.1", "0.1"))
#print(versionCompare("1.1", "1.2"))
#print(versionCompare("1.2", "1.2.9.9.9.9"))
#print(versionCompare("1.3", "1.2.9.9.9.9"))
#print(versionCompare("1.3", "1.3.4"))
#print(versionCompare("1.3.4", "1.10"))
#print(versionCompare("1.10", "1.10."))
