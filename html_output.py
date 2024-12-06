def save_html_to_file(html_content, filename="output.html"):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LaTeX to HTML</title>
        <style>
            .fraction {{
                display: inline-block;
                vertical-align: middle;
            }}
            .numerator {{
                display: block;
                text-align: center;
            }}
            .denominator {{
                display: block;
                text-align: center;
                border-top: 1px solid black;
            }}
            sub {{
                font-size: smaller;
                vertical-align: sub;
            }}
            sup {{
                font-size: smaller;
                vertical-align: super;
            }}
        </style>
    </head>
    <body>
        <h1>Wynik konwersji LaTeX na HTML</h1>
        <p>{html_content}</p>
    </body>
    </html>
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_template)
    print(f"Plik został zapisany jako: {filename}")
