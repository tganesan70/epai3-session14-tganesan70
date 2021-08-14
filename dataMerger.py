# Session-14 : Ganesan Thiagarajan
# 13-Aug-2021

import csv
from itertools import islice
from collections import namedtuple

#
# Create the namedtuple templates for parking various records and date format
#
date_of_record = namedtuple('date', 'day, month, year')
person_record = namedtuple('per_record', 'ssn,first_name,last_name,gender,language')
employment_record = namedtuple('emp_record', 'employer,department,employee_id,ssn')
update_record = namedtuple('upd_record', 'ssn,updated_date, updated_time,created_date, created_time')
vehicle_record = namedtuple('veh_record', 'ssn,vehicle_make,vehicle_model,model_year')
merged_record = namedtuple('merg_record','ssn,first_name, last_name, gender,language, \
                                              employer, department, employee_id, \
                                              updated_date, updated_time, created_date, created_time, \
                                              vehicle_make, vehicle_model, model_year')


def read_file(file_name):
    """
    Function: Read the CSV file which contains the records
    Params: file_name - to be read with fullpath
    Returns one row at a time as a lazy iterator
    """
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows


per_header_read = 1
per_records = []
per_records_count = 0
def read_personal_records(file_name):
    """
    Function: Read the CSV file which contains the personal records
    :param file_name:  Filename as a string with full path to read the personal details records
    :return: Number of records in the global list of personal records
    """
    global per_header_read
    global per_records_count

    for rec in read_file(file_name):
        if per_header_read == 1:
            per_header_read = 0
        else:
            per_records.append(person_record(*rec))
        per_records_count += 1
    return per_records_count-1

emp_header_read = 1
emp_records = []
emp_records_count = 0

def read_employment_records(file_name):
    """
    Function: Read the CSV file which contains the employment records
    :param file_name:  Filename as a string with full path to read the employment details records
    :return: Number of records in the global list of employment records
    """
    global emp_header_read
    global emp_records_count

    for rec in read_file(file_name):
        if emp_header_read == 1:
            emp_header_read = 0
        else:
            emp_records.append(employment_record(*rec))
        emp_records_count += 1
    return emp_records_count-1


veh_header_read = 1
veh_records = []
veh_records_count = 0

def read_vehicle_records(file_name):
    """
    Function: Read the CSV file which contains the vehicle records
    :param file_name:  Filename as a string with full path to read the vehicle details records
    :return: Number of records in the global list of vehicle records
    """
    global veh_header_read
    global veh_records_count

    for rec in read_file(file_name):
        if veh_header_read == 1:
            veh_header_read = 0
        else:
            veh_records.append(vehicle_record(*rec))
        veh_records_count += 1
    return veh_records_count-1

upd_header_read = 1
upd_records = []
upd_records_count = 0

def read_update_records(file_name):
    """
    Function: Read the CSV file which contains the update records
    :param file_name:  Filename as a string with full path to read the update details records
    :return: Number of records in the global list of update records
    """
    global upd_header_read
    global upd_records_count

    for rec in read_file(file_name):
        if upd_header_read == 1:
            upd_header_read = 0
        else:
            # Split the time and date and store it in proper format
            temp = rec[1].split("T")
            date_mm_yy_yyyy = [int(i) for i in temp[0].split("-")]
            date_updated = date_of_record(date_mm_yy_yyyy[2],date_mm_yy_yyyy[1], date_mm_yy_yyyy[0])    # Date as date object
            time_updated = temp[1]
            temp = rec[2].split("T")
            date_mm_yy_yyyy = [int(i) for i in temp[0].split("-")]
            date_created = date_of_record(date_mm_yy_yyyy[2],date_mm_yy_yyyy[1], date_mm_yy_yyyy[0])    # Date as date object
            time_created = temp[1]
            upd_records.append(update_record(rec[0],date_updated,time_updated,date_created,time_created))
        upd_records_count += 1
    return upd_records_count-1

def match_per_record(file_name, ssn):
    """
    Function: Read the CSV file which contains the employment records with matching ssn
    :param file_name:  Filename as a string with full path to read the employment details records
    :return: record that matches ssn in employment records
    """
    for per_rec in read_file(file_name):
        ssn_rec = per_rec[0]
        if ssn_rec != ssn:
            continue
        else:
            break
    #print(f'Matched ssn: {ssn} with the record ssn : {ssn_rec}')
    per_record = person_record(*per_rec)
    return per_record

def match_emp_record(file_name, ssn):
    """
    Function: Read the CSV file which contains the employment records with matching ssn
    :param file_name:  Filename as a string with full path to read the employment details records
    :return: record that matches ssn in employment records
    """
    for emp_rec in read_file(file_name):
        ssn_rec = emp_rec[-1]
        if ssn_rec != ssn:
            continue
        else:
            break
    #print(f'Matched ssn: {ssn} with the record ssn : {ssn_rec}')
    emp_record = employment_record(*emp_rec)
    return emp_record

def match_veh_record(file_name, ssn):
    """
    Function: Read the CSV file which contains vehicle records with matching ssn
    :param file:  Filename as a string with full path to read the vehicle details records
    :return: record that matches ssn in vehicle records
    """
    for veh_rec in read_file(file_name):
        ssn_rec = veh_rec[0]
        if ssn_rec != ssn:
            continue
        else:
            break
    #print(f'Matched ssn: {ssn} with the record ssn : {ssn_rec}')
    veh_record = vehicle_record(*veh_rec)
    return veh_record

def match_upd_record(file_name, ssn):
    """
    Function: Read the CSV file which contains update records with matching ssn
    :param file:  Filename as a string with full path to read the update details records
    :return: record that matches ssn in update records
    """
    for upd_rec in read_file(file_name):
        ssn_rec = upd_rec[0]
        if ssn_rec != ssn:
            continue
        else:
            break
    #print(f'Matched ssn: {ssn} with the record ssn : {ssn_rec}')
    temp = upd_rec[1].split("T")
    date_mm_yy_yyyy = [int(i) for i in temp[0].split("-")]
    date_updated = date_of_record(date_mm_yy_yyyy[2], date_mm_yy_yyyy[1], date_mm_yy_yyyy[0])  # Date as date object
    time_updated = temp[1]
    temp = upd_rec[2].split("T")
    date_mm_yy_yyyy = [int(i) for i in temp[0].split("-")]
    date_created = date_of_record(date_mm_yy_yyyy[2], date_mm_yy_yyyy[1], date_mm_yy_yyyy[0])  # Date as date object
    time_created = temp[1]
    upd_record = update_record(upd_rec[0], date_updated, time_updated, date_created, time_created)
    return upd_record

def create_merged_records(per_rec_file, emp_rec_file, upd_rec_file, veh_rec_file):
    """
    Function: To merge all the records for corresponding SSN stored across multiple files
    Paranms: 4 filenames for set of different parameters but with common SSN
    Returns: List of combined records (as namedtuples)
    """
    merged_records = []
    first_read = 1
    for per_rec in read_file(per_rec_file):
        if first_read == 1:    # Skip the header record
            first_read = 0
            continue
        per_record = person_record(*per_rec)
        ssn = per_record.ssn
        emp_record = match_emp_record(emp_rec_file, ssn)
        upd_record = match_upd_record(upd_rec_file, ssn)
        veh_record = match_veh_record(veh_rec_file, ssn)
        # Merge all data into new namedtuple with multiple columns
        merg_record = merged_record(per_record.ssn, per_record.first_name, per_record.last_name, per_record.gender, \
                                    per_record.language, \
                                    emp_record.employer, emp_record.department,emp_record.employee_id, \
                                    upd_record.updated_date, upd_record.updated_time, upd_record.created_date, \
                                    upd_record.created_time, \
                                    veh_record.vehicle_make, veh_record.vehicle_model, veh_record.model_year)
        merged_records.append(merg_record)
    return merged_records

def create_merged_records_with_expiry(per_rec_file, emp_rec_file, upd_rec_file, veh_rec_file, exp_yyyy, exp_mm, exp_dd):
    """
    Function: To merge all the records for corresponding SSN stored across multiple files with record expity cut-off
    Paranms: 4 filenames for set of different parameters but with common SSN
             Record expiry year, month and day as integer numbers in yyyy,mm and dd format
    Returns: List of combined records (as namedtuples)
    """
    merged_records = []
    first_read = 1
    for upd_rec in read_file(upd_rec_file):
        if first_read == 1:    # Skip the header record
            first_read = 0
            continue
        ssn = upd_rec[0]
        upd_record = match_upd_record(upd_rec_file, ssn)
        if upd_record.updated_date.year < exp_yyyy:
            continue
        elif upd_record.updated_date.month < exp_mm:
            continue
        elif upd_record.updated_date.day < exp_dd:
            continue
        # Merge the matching records
        per_record = match_per_record(per_rec_file, ssn)
        emp_record = match_emp_record(emp_rec_file, ssn)
        upd_record = match_upd_record(upd_rec_file, ssn)
        veh_record = match_veh_record(veh_rec_file, ssn)
        # Merge all data into new namedtuple with multiple columns
        merg_record = merged_record(per_record.ssn, per_record.first_name, per_record.last_name, per_record.gender, \
                                    per_record.language, \
                                    emp_record.employer, emp_record.department,emp_record.employee_id, \
                                    upd_record.updated_date, upd_record.updated_time, upd_record.created_date, \
                                    upd_record.created_time, \
                                    veh_record.vehicle_make, veh_record.vehicle_model, veh_record.model_year)
        merged_records.append(merg_record)
    return merged_records


def find_car_make_groups(merged_rec):
    mal_car_make_list = dict()
    fem_car_make_list = dict()
    for rec in merged_rec:
        gender = rec.gender
        make = rec.vehicle_make
        if gender == 'Male':
            if make in mal_car_make_list.keys():
                mal_car_make_list[make] += 1
            else:
                mal_car_make_list[make] = 1
        else:
            if make in fem_car_make_list.keys():
                fem_car_make_list[make] += 1
            else:
                fem_car_make_list[make] = 1
    # Find the largest car make group
    largest_male_car_make_group = max(mal_car_make_list.values())
    male_car_gr_name = [key for key in mal_car_make_list.keys() if mal_car_make_list[key] == largest_male_car_make_group]
    largest_female_car_make_group = max(fem_car_make_list.values())
    female_car_gr_name = [key for key in fem_car_make_list.keys() if fem_car_make_list[key] == largest_female_car_make_group]
    return male_car_gr_name, female_car_gr_name

# Test for read_file function()
#rows = read_file('personal_info.csv')
#for row in islice(rows, 5):
#    print(row)

# Goal-1 Test cases
print(f'*** Goal 1: Test cases ***')
per_rec_cnt = read_personal_records('personal_info.csv')
#print([per_records[i] for i in range(5)])
print(f'No. of records in Personal records: {per_rec_cnt}')
print(f'First, Second and Last record in the Personal records')
print(per_records[0],'\n', per_records[1],'\n',per_records[-1])

emp_rec_cnt = read_employment_records('employment.csv')
#print([emp_records[i] for i in range(5)])
print(f'No. of records in Employment records: {emp_rec_cnt}')
print(f'First, Second and Last record in the Employment records')
print(emp_records[0],'\n', emp_records[1],'\n',emp_records[-1])

veh_rec_cnt = read_vehicle_records('vehicles.csv')
#print([veh_records[i] for i in range(5)])
print(f'No. of records in Employment records: {veh_rec_cnt}')
print(f'First, Second and Last record in the Vehicle records')
print(veh_records[0],'\n', veh_records[1],'\n',veh_records[-1])

upd_rec_cnt = read_update_records('update_status.csv')
#print([upd_records[i] for i in range(5)])
print(f'No. of records in Employment records: {upd_rec_cnt}')
print(f'First, Second and Last record in the Update records')
print(upd_records[0],'\n', upd_records[1],'\n',upd_records[-1])

# test cases for Goal 2
print(f'*** Goal 2: Test cases ***')
mer_data = create_merged_records('personal_info.csv','employment.csv','update_status.csv','vehicles.csv')
#print([mer_data[i] for i in range(5)])
print(f'No. of records in merged date: {len(mer_data)}')
print(f'First, Second and Last record in the merged records')
print(mer_data[0],'\n', mer_data[1],'\n',mer_data[-1])

# test cases for Goal 3
print(f'*** Goal 3: Test case ***')
exp_yyyy = 2018
exp_mm = 1
exp_dd = 3
mer_data = create_merged_records_with_expiry('personal_info.csv','employment.csv',
                                                'update_status.csv','vehicles.csv', exp_yyyy, exp_mm, exp_dd)
print(f'No. of records beyond expiry date: {len(mer_data)}')
print(f'First, Second and Last record in the merged records')
print(mer_data[0],'\n', mer_data[1],'\n',mer_data[-1])

#test cases for Goal 4
print(f'*** Goal 4: Test case ***')
male_car_gr_name, female_car_gr_name = find_car_make_groups(mer_data)
print(f'Largest car make group(s) in Males : {male_car_gr_name}')
print(f'Largest car make group(s) in Females : {female_car_gr_name}')
