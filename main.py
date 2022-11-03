import os

# Get the list of all files and directories
path = "/home/signum/"  # path to the directorie that contains the plots
dir_list = os.listdir(path)

# Remove .plotting files from dir_list
dir_list = filter(lambda s: not s.endswith(".plotting"), dir_list)

splitted_dir_list = [file.split("_") for file in dir_list]

# Convert strings to ints
splitted_dir_list = [
    [int(file_part) for file_part in file_parts] for file_parts in splitted_dir_list
]

# sort splitted_dir_list by starting nonce
splitted_dir_list.sort(key=lambda nonce: nonce[1])

previous_file_parts = [0, 0, 0]
for file_parts in splitted_dir_list:

    if previous_file_parts[1] + previous_file_parts[2] > file_parts[1]:

        print("Faulty Plot!")
        print(f"File: {previous_file_parts}")
        print(f"File: {file_parts}")
        print("Are overlapping")

    previous_file_parts[0] = file_parts[0]
    previous_file_parts[1] = file_parts[1]
    previous_file_parts[2] = file_parts[2]


account_id_list = [splitted_file_list[0] for splitted_file_list in splitted_dir_list]

# Check if all Plot files have the same accountid
if not (
    not account_id_list
    or account_id_list.count(account_id_list[0]) == len(account_id_list)
):
    print("Not All Account IDs are the same")
