import pandas as pd
import Facility.xml from Facility.xml

"""
Input: string (the location of the xml file to be converted)
Output: string (the location of the new csv file)
        OR
        none (the function opens up the new file)
"""

read_file = pd.read_csv(Facility.xml)
