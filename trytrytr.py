import os


def tryme(filename):
    extension_sample_type_priority_pair = [
        ("baf.bw", "baf-bw"),
        ("bw", "bw"),
        ("roh.bed", "roh-bed")
    ]

    for extension, sample_type in extension_sample_type_priority_pair:
        if filename.endswith(f".{extension}"):
            return sample_type
    else:
        return os.path.splitext(filename)[1][1:]

test_files = [
    "some_directory/some_f.filebaf.bw",
    "some_directory/some_fi.le.tn.bw",
    "some_directory/some_f.ile.tns.bw",
    "some_directory/some_.file.baf.bw",
    "some_directory/some._f.ile.roh.bed",
    "some_directory/some_fil.e.txt"
]

for test_file in test_files:
    print(tryme(test_file), test_file, sep=": \t\t")
# extension_sample_type_mapping = {
#     "bw": "bw",
#     "baf.bw": "baf-bw",
#     "roh.bed": "roh-bed"
# }dfdff
# dsfjlk
#
# root, extension = os.path.splitext(filename)
#
# extension_dotless = extension[1:]
#
# if extension_dotless == "bw":
#     if filename.endswith(".baf.bw"):
#         extension_dotless = "baf.bw"
#
# elif filename.endswith(".roh.bed"):
#     extension_dotless = "roh.bed"

# return extension_sample_type_mapping.get(extension_dotless)
#