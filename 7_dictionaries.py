# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

month_conversions = {
    "Jan": "January",
    "Feb" : "Feburary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sept" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(month_conversions["Nov"])
#similarly
print(month_conversions.get("Dec"))
# print(month_conversions.get("luc"))
# will return none
print(month_conversions.get("luc", "not a valid key"))

month_conversions = {
   1: "January",
   2: "Feburary",
   3: "March",
   4: "April",
   5: "May",
   6: "June",
   7: "July",
   8: "August",
   9: "September",
   10: "October",
   11: "November",
   12: "December",
}

