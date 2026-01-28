# # @misc{example_misc, 
#     author = {Nachname, Vorname},
#     title = {Title}, 
#     year = {2000},
#     url = {https://www.example.com},
# }

# @article{example_article, 
#     author = {Nachname, Vorname},
#     title = {Title}, 
#     year = {2000},
#     doi = {10.1000/exampledoi},
# }

# @online{example_online, 
#     author = {Nachname, Vorname},
#     title = {Title}, 
#     url = {https://www.example.com},
#     urldate = {2000-01-01},
#     year = {2000},
# }

# @software{example_software, 
#     author = {Nachname, Vorname}, 
#     title = {Title}, 
#     year = {2000}, 
#     url = {https://www.example.com}
# }

# @thesis{example_thesis, 
#     author = {Nachname, Vorname}, 
#     title = {Title}, 
#     type = {Bachelorthesis}, 
#     school = {University XYZ}, 
#     year = {2000}, 
#     url = {https://www.example.com}
# }



import csv
from datetime import datetime



type_mapping = {
    "Forum": "online",
    "Webseite": "online",
    "Blog": "online",
    "Youtube": "online",
    "Presentation": "online",
    "Paper": "article",
    "Documentation": "manual",
    "Datasheet": "manual",
    "Github": "software",
    "Masterthesis": "thesis",
    "Bachelorthesis": "thesis",
    "PHD Thesis": "thesis",
    "Book": "book"
}

date = "28-jan-2026"
csv_file = f"references_{date}.csv"
bib_file = f"references_{date}.bib"


def convert_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return date_str

def format_bib_entry(row, bib_type):
    key = row.get("headline", "").strip() or "no_key"
    author = row.get("author", "").strip()
    title = row.get("title", "").strip()
    year = row.get("year", "").strip()
    url = row.get("url", "").strip()
    urldate = convert_date(row.get("urldate", "").strip())
    type_field = row.get("type", "").strip()
    school = row.get("school", "").strip()
    doi = row.get("doi", "").strip()

    if bib_type == "online":
        entry = f"@online{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}},\n" if urldate else ""
        entry += f"  year = {{{year}}}\n" if year else ""
        entry += "}\n\n"
    elif bib_type == "article":
        entry = f"@article{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n" if title else ""
        entry += f"  year = {{{year}}},\n" if year else ""
        if doi:
            entry += f"  doi = {{{doi}}},\n"
        elif url:
            entry += f"  url = {{{url}}},\n"
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"
    elif bib_type == "manual":
        entry = f"@manual{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  year = {{{year}}},\n" if year else ""
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"
    elif bib_type == "software":
        entry = f"@software{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  version = {{{type_field}}},\n" if type_field else ""
        entry += f"  year = {{{year}}},\n" if year else ""
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"
    elif bib_type == "thesis":
        entry = f"@thesis{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  type = {{{type_field}}},\n" if type_field else ""
        entry += f"  school = {{{school}}},\n" if school else ""
        entry += f"  year = {{{year}}},\n" if year else ""
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"
    elif bib_type == "book":
        entry = f"@thesis{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  year = {{{year}}},\n" if year else ""
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"
    else:
        entry = f"@misc{{{key},\n"
        entry += f"  author = {{{author}}},\n" if author else ""
        entry += f"  title = {{{title}}},\n"
        entry += f"  year = {{{year}}},\n" if year else ""
        entry += f"  url = {{{url}}},\n" if url else ""
        entry += f"  urldate = {{{urldate}}}\n" if urldate else ""
        entry += "}\n\n"

    return entry


entry_count = 0

with open(csv_file, newline="", encoding="utf-8") as csvfile, open(bib_file, "w", encoding="utf-8") as bib:
    reader = csv.DictReader(csvfile)
    for row in reader:
        typ = row.get("typ", "").strip()
        bib_type = type_mapping.get(typ, "misc")
        bib_entry = format_bib_entry(row, bib_type)
        bib.write(bib_entry)
        entry_count += 1

print(f"BibTeX-Datei '{bib_file}' erfolgreich erstellt.")
print(f"Anzahl erstellter Quellen: {entry_count}")
