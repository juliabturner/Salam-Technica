import requests
import pandas as pd
import csv
from google.cloud import bigquery
import jwt

def convert():
    import PyPDF2
    # creating a pdf file object
    pdfFileObj = open('tax1.pdf', 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    # extracting text from page
    print(pageObj.extractText())
    # closing the pdf file object
    pdfFileObj.close()


def get_url():
    search_url = "https://projects.propublica.org/nonprofits/api/v2/search.json"
    URL = 'https://projects.propublica.org/nonprofits/api/v2/organizations/:{}.json'
    name = 'Wal Mart'
    # "Wal Mart" returns the Wal-Mart foundation
    # "Walmart" returns WALMART INC ASSOCIATES HEALTH AND WELFARE PLAN
    PARAMS = {'q': name}

    # sending get request and saving the response as response object
    search_result = requests.get(url=search_url, params=PARAMS).json()
    # Obtain ein number
    ein = search_result['organizations'][0]['ein']

    form = requests.get(url=URL.format(ein), ).json()
    print(form)
    # Obtain URL of tax file
    pdf_url = form['filings_with_data'][0]['pdf_url']
    print(pdf_url)
    # PDF is scanned, not able to parse :(
    # Another approach would be to download XML files from https://s3.amazonaws.com/irs-form-990/index_2013.json
    # If pdf is parsable, we convert to text file next


# MAIN
# p = pdf()
# p.convert()

# We'll be using artificial data to substitute
# Read and convert to csv from tx
black_list = ["ACT for America", "Center for Security Policy", "Family Security Matters","Middle East Forum",
              "Society of Americans for National Existence","Jihad Watch","Foundation for Defense of Democracies",
              "Global Faith Institute Inc","Conservative Forum of Silicon Valley"]
white_list = ["Islamic Relief Canada","Muslim Advocates","Council On American-Islamic Relations", "American-Arab Anti-Discrimination Committee", "Muslim Legal Fund Of America"]

output = pd.read_csv(r'C:\Users\nhung\PycharmProjects\salam\company3.txt')
output= output.to_csv(r'C:\Users\nhung\PycharmProjects\salam\company3.csv', index=None)


with open('company3.csv','r+') as csvinput:
    writer = csv.writer(csvinput, lineterminator='\n')
    reader = csv.reader(csvinput)
    all = []

    for row in reader:
        print(row)
        if row[0] in black_list:
            row.append("FALSE")
            all.append(row)
        elif row[0] in white_list:
            row.append("TRUE")
            all.append(row)
    csvinput.truncate(0)
    writer.writerows(all)

client = bigquery.Client()
table_id = "technica-293603.technica_dataset.technica_table"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open('company1.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
source_file.close()
job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)
