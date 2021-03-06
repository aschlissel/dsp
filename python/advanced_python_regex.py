import csv
import collections

f = open('faculty.csv')
csv_f = csv.reader(f)

#Q1.
def different_degrees(csv_f):
    #create two lists to perform operations
    diff_degrees = []
    new_diff_degrees = []

    #append faculty column to list
    [diff_degrees.append(col[1]) for col in csv_f]

    #remove column heading
    del diff_degrees[0]

    #remove the periods in degrees to make degrees uniform
    diff_degrees = map(lambda diff_degrees: diff_degrees.replace(".", ""), diff_degrees)

    #separate multiple-degree strings in that list
    [new_diff_degrees.extend(item.split()) for item in diff_degrees]

    #count the number of degrees in each category
    diff_degrees_count = collections.Counter(new_diff_degrees)
    return diff_degrees_count


#Q2.

def titles(csv_f):

    #create list to perform operations
    prof_titles = []

    #append titles column to list
    [prof_titles.append(col[2]) for col in csv_f]

    #remove column heading
    del prof_titles[0]

    #change the typo 'is' to 'of'
    prof_titles = map(lambda prof_titles: prof_titles.replace("is ", "of "), prof_titles)

    #count title frequencies
    prof_titles_count = collections.Counter(prof_titles)
    return prof_titles_count


#Q3
def emails(csv_f):
    email = []
    [email.append(col[3]) for col in csv_f]
    del email[0]
    print email
    return 0
    

#Q4    
def email_domains(csv):

    #put emails in a list
    full_emails = emails(csv_f)

    #make lists to perform operations
    split_email = []
    duplicate_domains = []
    domains = []

    #separate email names from their domains
    [split_email.extend(item.split("@")) for item in full_emails]

    #make a list with only domains
    for item in split_email:
        if '.' in item:
            duplicate_domains.append(item)

    #remove duplicates from domain list by changing to a set
    domains_set = set(duplicate_domains)
    domains = list(domains_set)

    #find out how many different email domains in the list
    print "There are " + str(len(domains)) + " different email domains."
    print domains
    return 0
