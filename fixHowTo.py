# import csv
# # Read the CSV file
# with open('out_openai_completion.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     data = list(reader)

# # Prepare the data and replace double quotes with a placeholder character
# prepared_data = []
# for row in data:
#     prepared_data.append({
#         'prompt': row['sub_prompt'].replace('"', '###QUOTE###'),
#         'completion': row['response_txt'].replace('"', '###QUOTE###')
#     })

# # Write the prepared data to a new CSV file
# with open('prepared_data.csv', 'w', newline='') as file:
#     fieldnames = ['prompt', 'completion']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(prepared_data)

# # Read the prepared CSV file and replace the placeholder with double quotes
# with open('prepared_data.csv', 'r') as file:
#     data = file.read()

# data = data.replace('###QUOTE###', '"')

# # Write the updated data back to the CSV file
# with open('prepared_data.csv', 'w') as file:
#     file.write(data)
