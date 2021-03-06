import csv

with open("balne.csv") as file:
    beach_status_reader = csv.DictReader(file, delimiter=",", quotechar='"')
    bathing_by_campaign = {}

    for row in beach_status_reader:
        print(row)
        print(row["numero_boletim"])
        campaign = row["numero_boletim"]
        bathing = row["categoria"]

        if campaign not in bathing_by_campaign:
            bathing_by_campaign[campaign] = {
                "Própria": 0,
                "Imprópria": 0,
                "Muito Boa": 0,
                "Indisponível": 0,
                "Satisfatória": 0,
            }
            bathing_by_campaign[campaign][bathing] += 1

with open("report_por_campanha_dicionarios.csv", "w") as file:
    # os valores a serem escritos devem ser dicionários
    header = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]

    writer = csv.DictWriter(file, fieldnames=header)

    for campaing, bathing in bathing_by_campaign.items():

        row = {"Campanha": campaign, **bathing}

        writer.writerow(row)
