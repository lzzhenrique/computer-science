# import csv

# with open("balneabilidade.csv") as file:
#     beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
#     header, *data = beach_status_reader

# print(data)

# ENTENDENDO "DESCONSTRUCAO" EM PY

# a, b = "CD"

# print(a)
# print(b)

# head, *tail = [1, 2, 3]
# print(head)
# print(tail)


import csv

with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

bathing_by_campaign = {}
for row in data:
    campaing = row[6]
    bathing = row[2]
    print(bathing)
    if campaing not in bathing_by_campaign:
        bathing_by_campaign[campaing] = {
            "Própria": 0,
            "Imprópria": 0,
            "Muito Boa": 0,
            "Indisponível": 0,
            "Satisfatória": 0,
        }
    bathing_by_campaign[campaing][bathing] += 1

with open("report_por_campanha.csv", "w") as file:
    writer = csv.writer(file)

    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    writer.writerow(headers)

    for campaing, bathing in bathing_by_campaign.items():
        row = [campaing, *bathing.values()]
        writer.writerow(row)
