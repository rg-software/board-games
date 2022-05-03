import pyexcel as p
from dotmap import DotMap

md_filename = "readme.md"
xlsx_name = "games.xlsx"
open_tag = "<!--GAMES_TABLE-->"
close_tag = "<!--GAMES_TABLE_END-->"
bgg_link = "<img src=https://cf.geekdo-static.com/icons/favicon2.ico width=20>"
wiki_link = """<img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Wikipedia's_W.svg" width=20>"""
games_page = "Games"

book = p.get_book(file_name=xlsx_name)
sheet = book[games_page]
cols = DotMap({name.replace(" ", ""): c for c, name in enumerate(sheet.row[0])})


r = "\n|Name|BGG Rating|Core LOC|GUI value|Extra players|Category|CS topics|\n"
r += "|---|---|---|---|---|---|---|\n"

for row in list(sheet.rows())[1:]:
    r += f"|[{bgg_link}]({row[cols.BGG]})[{wiki_link}]({row[cols.Wiki]})&nbsp;{row[cols.Name]}|"
    r += f"{row[cols.BGGRating]}|{row[cols.CoreLOC]}|{row[cols.GUIvalue]}|{row[cols.Extraplayers]}|"
    r += f"{row[cols.Category]}|{row[cols.CStopics]}|\n"


with open(md_filename, "r", encoding="utf-8") as f:
    mdfile = f.read()
    s_beg = mdfile[: mdfile.find(open_tag) + len(open_tag)]
    s_end = mdfile[mdfile.find(close_tag) :]


with open(md_filename, "wt", encoding="utf-8") as f:
    f.write(f"{s_beg}{r}\n{s_end}")
