import csv

# Open the csv file
with open('professors.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  # Initialize a counter to keep track of the row number
  row_number = 0
  
  # Initialize a list to store the html code
  html_code = []
  html_code.append('<table><table style="width: 80%;" cellpadding="5" cellspacing="0" class="gridtable dataTable no-footer" id="DataTables_Table_0">')
  html_code.append('<!-- initializing rows -->')
  html_code.append('<tr>')
  html_code.append('  <th>Name</th>')
  html_code.append('  <th>Email</th>')
  html_code.append('  <th>Office</th>')
  html_code.append('  <th>Department</th>')
  html_code.append('  <th>Research Interest</th>')
  html_code.append('  <th>Hiring</th>')
  html_code.append('</tr>')
  # Iterate over the rows in the csv file
  for row in csv_reader:
    # Skip the first row, which contains the headers
    if row_number == 0:
      row_number += 1
      continue
    
    # Assign the values from the csv file to variables
    name = row[0]
    email = row[1]
    office = row[2]
    department = row[3]
    research_interest = row[4]
    website = row[5]
    hiring_description = row[6]
    hiring_website = row[7]
    
    # Determine whether the professor is hiring
    if hiring_description and hiring_website:
      hiring_html = f'<td valign="top"><a href="{hiring_website}" class="new-window"><b>Available:<br>   {hiring_description}</b></a></td>'
    elif hiring_description:
      hiring_html = f'<td valign="top"><a href="mailto:{email}" class="new-window"><b>Available:<br>   {hiring_description}</b></a></td>'
    else:
      hiring_html = '<td valign="top">No Positions</td>'
    
    # Determine whether the row should have the "odd" or "even" class
    if row_number % 2 == 0:
      row_class = "even"
    else:
      row_class = "odd"
    
    # Create the html code for the row
    html = f'<tr role="row" class="{row_class}">\n'
    html += f'  <td valign="top" class="sorting_1"><a href="{website}" class="new-window"><b>{name}</b></a></td>\n'
    html += f'  <td valign="top"><a href="mailto:{email}"><b>{email}</b></a></td>\n'
    html += f'  <td valign="top">{office}</td>\n'
    html += f'  <td valign="top">{department}</td>\n'
    html += f'  <td valign="top">{research_interest}</td>\n'
    html += hiring_html + '\n'
    html += '</tr>'
    
    # Add the html code to the list
    html_code.append(html)
    
    # Increment the row number
    row_number += 1

# Open a file to save the html code to
html_code.append('</table>')
with open('professors.html', 'w') as out_file:
  # Write the html code to the file
  for html in html_code:
    out_file.write(html)
    out_file.write('\n')