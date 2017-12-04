import csv


def write_csv():
    with open('names.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def read_csv():
    with open('names.csv') as csvfile:
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


def write_html_file(html):
    with open("index.html", "w") as htmlFile:
        htmlFile.write(html)


if __name__ == '__main__':
    html = read_csv()
    write_html_file(html)
