# GOAL OF THIS SOFTWARE: scrape from a CSV into a batch of md files
## w the right CSV, you can run this script in Terminal with ```python make_crops.py``` and score markdown files per row!
### reuse & recycle & have a nice day

## run with:
## $ python builder.py
## don't use python3, it has probs w these old libs ;_;

import csv # csv deciphering module
# opens file to work from (only read not write (rb not wb))
with open('dexdata.csv', 'rb') as csvfile:
    # b/c this is hecka raw data...
    pulpy_data = csv.DictReader(csvfile, delimiter=',', quotechar='\"')
    # want a way to populate this from the csv header! less errors
    headers = ['name', 'myKey', 'category'] # manual entry for now
    # this needs to count down for the row count (while)

    for row in pulpy_data:
        # gotta assign fields to vars for later
        title = row['name']
        count = row['myKey']
        description = row['category']
       
        # formatting filename, from the data.title
        img_file_name = title.replace(' ','_') # b/c filesystem
        md_file_name = title.lower().replace(' ','-') # b/c filesystem
        
        # creating img asset path
        featuredimage = '/assets/{}.png'.format(img_file_name)
        
        # create .md to write row data into
        f = open('{}.md'.format(md_file_name), 'w')
        f.write('---\n') # formatting req
        # f.write('Close to generating data file for {} ...'.format(md_file_name))
        f.write('templateKey: blog-post\n')
        f.write('featuredpost: false\n')
        f.write('featuredimage: {}\n'.format(featuredimage))
        f.write('title: {}\n'.format(title))
        f.write('description: {}\n'.format(description))
        f.write('testfield: {}\n'.format(count))
        f.write('---') # formatting req
        f.close() # python saves file on close()