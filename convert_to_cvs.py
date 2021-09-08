import xml.etree.ElementTree as ET


"""
Input: string (the location of the xml file to be converted)
Output: string (the location of the new csv file)
        OR
        none (the function opens up the new file)
"""

# read_file = pd.read_csv(Facility.xml)
tree = ET.parse("Facility.xml")
root = tree.getroot()

property_ids = {}
count = 0
for property in root.iter("T_Facility"):
    # print(property)
    for id in property.iter("Facility_ID"):
        print(id.text)
