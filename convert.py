import xml.etree.ElementTree as ET
import csv

# READ THE XML FILE
tree = ET.parse("Facility.xml")
root = tree.getroot()

# NEW DATA STRUCTURE
# properties_data_frame = [
#     {"property_id": 1, "Facility_Account_Number":2}
# ]
properties = []
new_columns = ["property_id", "account_number", "name", "address1", "city", "state_prov", "postal_code", "primary_contact_id"]
old_columns = ["Facility_ID", "Facility_Account_Number", "Facility_Name", "Service_Address_Full", "Service_Address_City",
"Service_Address_State", "Service_Address_Zip_Code", "Facility_Contact_Mgr_ID"]
count = 0
for property in root.iter("T_Facility"):
    property_obj = {}
    for i, column in enumerate(new_columns):
        if property.find(old_columns[i]) is not None:
            property_obj[column] = property.find(old_columns[i]).text
        else:
            property_obj[column] = "no data"

        # if property.find("Facility_Account_Number") is not None:
        #     property_obj["account_number"] = property.find("Facility_Account_Number").text
        # else:
        #     property_obj["account_number"] = None

        # if property.find("Facility_Name") is not None:
        #     property_obj["name"] = property.find("Facility_Name").text
        # else:
        #     property_obj["name"] = None


        # Now add the property dict to the properties list
    properties.append(property_obj)
print(properties)

"""
Convert the list of dictionaries to csv
"""
file = open("new.csv", "w")
writer = csv.writer(file)

writer.writerow(properties[0].keys())
for property in properties:
    writer.writerow(property.values())

file.close()
