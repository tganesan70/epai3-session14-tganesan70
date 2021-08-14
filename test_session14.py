##########################################################################
# pytest script for Session13 assignment
#
# Ganesan Thiagarajan, 06th Aug 2021
##########################################################################
#
import Parking
import inspect
import os
import re
from math import isclose


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Parking, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_violation_rec1():
    """
    Check for creation of non-empty records
    """
    violation_recs = Parking.create_record_generator('nyc_parking_tickets_extract.csv')
    assert len(violation_recs) > 0, "Error in creating the records"


def test_violation_rec2():
    """
    Check for correct number of records being created
    :return:
    """
    violation_recs = Parking.create_record_generator('nyc_parking_tickets_extract.csv')
    line_count = -1  # Skip the header
    with open('nyc_parking_tickets_extract.csv', encoding='utf8', errors='ignore') as f:
        for line in f:
            line_count += 1
    assert len(violation_recs) == line_count, "Error in creating correct number of records"

def test_violation_rec3():
    """
    Check for correct format for the records being created
    :return:
    """
    violation_recs = Parking.create_record_generator('nyc_parking_tickets_extract.csv')
    assert type(violation_recs[0].veh_make) is str, "Wrong data type for vehicle make"
    assert type(violation_recs[0].violation_code) is int, "Wrong data type for violation code"
    assert type(violation_recs[1].issue_date) is Parking.date_of_record, "Wrong data type for date"
    assert type(violation_recs[1].veh_type) is str, "Wrong data type for vehicle type"
    assert type(violation_recs[1].plate_no) is str, "Wrong data type for vehicle plate number"
    assert type(violation_recs[1].plate_state) is str, "Wrong data type for vehicle plate state"
    assert type(violation_recs[1].plate_type) is str, "Wrong data type for vehicle plate type"

# Goal 2 Solution
def test_violation_rec4():
    """
    Check for number of violations statistics for a given car make
    :return:
    """
    car_make = 'HONDA'
    violation_recs = Parking.create_record_generator('nyc_parking_tickets_extract.csv')
    num_violations1 = Parking.find_violation_stats_from_records(violation_recs, car_make)
    assert num_violations1 == 106, "No, of violation is wrong as per records"
    car_make = 'CHEVR'
    num_violations1 = Parking.find_violation_stats_from_records(violation_recs, car_make)
    assert num_violations1 == 76, "No, of violation is wrong as per records"

def test_violation_rec5():
    car_make = 'HONDA'
    num_violations2 = Parking.find_violation_stats_from_file('nyc_parking_tickets_extract.csv', car_make)
    assert num_violations2 == 106, "No, of violation is wrong as per records"
    car_make = 'CHEVR'
    num_violations2 = Parking.find_violation_stats_from_file('nyc_parking_tickets_extract.csv', car_make)
    assert num_violations2 == 76, "No, of violation is wrong as per records"

def test_violation_rec6():
    """
    Check the validity of both approaches
    :return:
    """
    car_make = 'HONDA'
    violation_recs = Parking.create_record_generator('nyc_parking_tickets_extract.csv')
    num_violations1 = Parking.find_violation_stats_from_records(violation_recs, car_make)
    num_violations2 = Parking.find_violation_stats_from_file('nyc_parking_tickets_extract.csv', car_make)
    assert num_violations2 == num_violations1, "No, of violation not matching in file and records "

# End of test_session13
