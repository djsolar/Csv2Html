import csv
import os


def write_csv():
	with open('names.csv', 'w') as csvfile:
		fieldnames = ['first_name', 'last_name']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
		writer.writerow({})
		writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
		writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def read_csv(path):
	with open(path) as csvfile:
		reader = csv.reader(csvfile)
		is_header = True
		html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>table</title>
    <style>
        body {
            padding: 0;
            margin: 0;
            font: normal 12px/24px "\5FAE\8F6F\96C5\9ED1";
            color: #444;
        }

        table {
            width: 500px;
            border: 0;
            margin: 60px auto 0;
            text-align: center;
            border-collapse: collapse;
            border-spacing: 0;
        }

        table th {
            background: #0090D7;
            font-weight: normal;
            line-height: 30px;
            font-size: 14px;
            color: #FFF;
        }

        table tr:nth-child(odd) {
            background: #F4F4F4;
        }

        table td:nth-child(even) {
            color: #C00;
        }

        table tr:hover {
            background: #73B1E0;
            color: #FFF;
        }

        table td, table th {
            border: 1px solid #EEE;
        }
    </style>
</head>
<body>
<div id="wrapper">"""
		for row in reader:
			if len(row) == 0:
				is_header = True
				html += "</table>"
			else:
				if is_header:
					is_header = False
					html += "<table border='1'> <thead><tr>"
					for header in row:
						html += "<th>" + header + "</th>"
					html += "</tr></thead>"
				else:
					html += "<tbody><tr>"
					for row_content in row:
						html += "<td>" + row_content + "</td>"
					html += "</tr></tbody>"
		html += "</table> </div> </body> </html>"
		return html


def write_html_file(html, path):
	with open(path, "w") as htmlFile:
		htmlFile.write(html)


def transfer_csv_html(path):
	html = read_csv(path)
	dir_name, filename = os.path.split(path)
	html_path = dir_name + os.sep + os.path.splitext(filename)[0] + ".html"
	write_html_file(html, html_path)
	return html_path

