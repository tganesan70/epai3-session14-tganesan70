# Session 14 Readme file 
# Assignment details:

# Data base merger
For this project you have 4 files containing information about persons.
Each file contains a key, SSN, which uniquely identifies a person.
This key is present in all four files.
The files are:
    1. personal_info.csv - personal information such as name, gender, etc. (one row per person)
    2. vehicles.csv - what vehicle people own (one row per person)
    3. employment.csv - where a person is employed (one row per person)
    4. update_status.csv - when the person's data was created and last updated

You are guaranteed that the same SSN value is present in every file, 
and that it only appears once per file.

In addition, the files are all sorted by SSN, i.e. the SSN values appear in 
the same order in each file.

# Goal 1
Your first task is to create iterators for each of the four files that 
contained cleaned up data, of the correct type (e.g. string, int, date, etc), 
and represented by a named tuple.

For now these four iterators are just separate, independent iterators.

# Goal 2
Create a single iterable that combines all the columns from all the iterators.
The iterable should yield named tuples containing all the columns. 
Make sure that the SSN's across the files match!
All the files are guaranteed to be in SSN sort order, and every SSN is unique, 
and every SSN appears in every file.
Make sure the SSN is not repeated 4 times - one time per row is enough!

# Goal 3
Next, you want to identify any stale records, where stale simply means the 
record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). 
Create an iterator that only contains current records (i.e. not stale) based on 
the last_updated field from the status_update file.

# Goal 4
Find the largest group of car makes for each gender.
Possibly more than one such group per gender exists (equal sizes).`

# Solution  for Goal 1
Use the CSV reader to read the rows (with a header row) and create a lazy iterator
to yield one row at a time. Then the rows are read and the split into fields. These
fields are filled into various parameters entry in a namedtuple. The namedtuple is 
saved in a global list. This is repeated for all 4 files.

# Solution  for Goal 2
The personal details record file is read and the SSN is taken as a token to find records from 
other files. The corresponding matching record is returned by a lazy iterator function. These
records are merged using a namedtuple and the saved in a list. This combined list is returned.

# Solution for Goal 3
The updated details record file is read and the SSN is taken as a token to find records from 
other files if the date of update is later than the expiry date given as input. 
The corresponding matching record is returned by a lazy iterator function. These
records are merged using a namedtuple and the saved in a list. This combined list is returned.


# Solution for Goal 4
The merged records list is taken as the input. For each entry, depending on the gender
of the person, car make statistics are computed by counting them and making a dictionary
for each car make category. This is done for males and females separately. Finally, the
car make group with maximum count is seletced for the male groups and female groups
from the dictionary. Optionally, the dictionary can be stored globally for other statistics
computation. 

# Test cases
### Goal 1: The 4 data files are read and namedtuple records are created as a structured data
### Goal 2: The 4 data files are read and namedtuple records are created merged as single data record
### Goal 3: Creation of merged data records but with dates after expiry date
### Goal 4: Find the largest car maker group among males and females from the merged data records
