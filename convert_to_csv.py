import xml.etree.ElementTree as ET
import csv

"""
Input: string (the location of the xml file to be converted)
Output: string (the location of the new csv file)
        OR
        none (the function opens up the new file)
"""

# read_file = pd.read_csv(Facility.xml)
tree = ET.parse("Facility.xml")
root = tree.getroot()

properties_data_frame = {
    "property_id":[],
    "account_number":[],
    "name":[],
    "address1":[],
    "city":[],
    "state_prov":[],
    "postal_code":[],
    "primary_contact_id":[]
}
count = 0
for property in root.iter("T_Facility"):

    properties_data_frame["property_id"].append(property.find("Facility_ID").text)

    if property.find("Facility_Account_Number") is not None:
        properties_data_frame["account_number"].append(property.find("Facility_Account_Number").text)
    else:
        properties_data_frame["account_number"].append(None)

    if property.find("Facility_Name") is not None:
        properties_data_frame["name"].append(property.find("Facility_Name").text)
    else:
        properties_data_frame["name"].append(None)
# print(properties_data_frame["account_number"])

"""
Covert the dictionary
"""
file = open("new.csv", "w")
writer = csv.writer(file)

# for header in properties_data_frame.keys:
writer.writerow(properties_data_frame.keys())
for column in properties_data_frame.values():
    writer.writerow(column)
# writer.writerow(properties_data_frame["property_id"])
# writer.writerow(properties_data_frame["account_number"])

file.close()
# df = pd.DataFrame(properties_data_frame, columns = [
#     "property_id", "account_number", "name", "address1", "city", "state_prov",
#     "postal_code", "primary_contact_id"])

# print(df)
