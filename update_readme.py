import datetime
import os
from dateutil import relativedelta
from lxml import etree

def daily_readme(birthday):
    """Calculate uptime since birth"""
    diff = relativedelta.relativedelta(datetime.datetime.today(), birthday)
    return '{} years, {} months, {} days'.format(
        diff.years, diff.months, diff.days)

def svg_overwrite(filename, age_data):
    """Update SVG with dynamic uptime."""
    tree = etree.parse(filename)
    root = tree.getroot()

    def find_and_replace(element_id, new_text):
        element = root.find(f".//*[@id='{element_id}']")
        if element is not None:
            element.text = str(new_text)

    find_and_replace('age_data', age_data)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    # Calculate uptime
    age_data = daily_readme(datetime.datetime(2002, 7, 30))  # Replace with your actual birthdate
    # Update SVG
    svg_overwrite('assets/dark_mode.svg', age_data)
