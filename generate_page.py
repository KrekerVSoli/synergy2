def generate_html_page(org_name, org_info, official_font="Arial"):
    extra_fonts = [
        "Georgia",
        "'Times New Roman', Times, serif",
        "'Courier New', Courier, monospace",
        "'Comic Sans MS', cursive",
        "'Verdana', Geneva, sans-serif",
        "Open Sans"
    ]

    all_fonts = [official_font] + extra_fonts

    html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{org_name}</title>
    <style>
        body {{
            font-family: {official_font}, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        .font-options {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
        }}
        .font-sample {{
            margin: 15px 0;
            padding: 12px;
            border-left: 5px solid #3498db;
            background: #fafafa;
        }}
        .font-name {{
            font-weight: bold;
            color: #2980b9;
            display: block;
            margin-bottom: 6px;
        }}
        /* Класс для каждого шрифта — чтобы реально применить его к тексту */
        {''.join(
            f'.font-{i} {{ font-family: {f}, sans-serif; }}'
            for i, f in enumerate(all_fonts)
        )}
    </style>
</head>
<body>
    <div class="container">
        <h1>{org_name}</h1>
        <p>{org_info}</p>

        <div class="font-options">
            <h2>Варианты шрифтов</h2>
            <p>Ниже представлены 6 вариантов шрифтов, включая официальный:</p>
            {''.join(
                f'''<div class="font-sample">
                    <span class="font-name">{f}</span>
                    <span class="font-{i}">Пример текста, чтобы показать, как выглядит этот шрифт: Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span>
                </div>'''
                for i, f in enumerate(all_fonts)
            )}
        </div>
    </div>
</body>
</html>
"""
    return html_content


if __name__ == "__main__":
    organization_name = "Синергия"
    organization_info = (
        "Полное название: Автономная некоммерческая организация высшего образования «Московский университет „Синергия“» Год основания: 1995 (историю ведут с 1988 года — тогда был создан Институт экономики и финансов, позже преобразованный в бизнес-школу)."
    )
    official_font = "Arial" 

    html_page = generate_html_page(organization_name, organization_info, official_font)

    output_filename = "organization_page.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_page)

    print(f"HTML-страница успешно сгенерирована: {output_filename}")
