import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

def emails(csv):
    email = []
    [email.append(col[3]) for col in csv_f]
    del email[0]
    return email

emails_out = open("emails.csv", "w")
emails_writer = csv.writer(emails_out)
data = emails(csv_f)

for item in data:
    emails_writer.writerow([item])

emails_out.close()
