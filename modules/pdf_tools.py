import re
from pathlib import Path

import fitz


def extract_wb_number(page) -> str | None:
    """
    Извлекает номер WB со страницы PDF.
    """
    text = page.get_text()
    digits = re.findall(r"\d+", text)

    if len(digits) >= 2:
        wb_number = digits[-2] + digits[-1]

        if len(wb_number) >= 10:
            return wb_number

    return None


def sort_pdf_by_last4(input_pdf: Path, output_pdf: Path) -> int:
    """
    Сортирует PDF по последним четырём цифрам номера WB.

    Возвращает количество обработанных страниц.
    """

    source = fitz.open(input_pdf)
    result = fitz.open()

    pages = []

    for page_index in range(len(source)):
        page = source[page_index]

        wb_number = extract_wb_number(page)

        if wb_number is None:
            continue

        pages.append(
            (
                int(wb_number[-4:]),
                wb_number,
                page_index,
            )
        )

    pages.sort()

    for _, _, page_index in pages:
        result.insert_pdf(
            source,
            from_page=page_index,
            to_page=page_index,
        )

    result.save(
        output_pdf,
        garbage=4,
        deflate=True,
        clean=True,
    )

    result.close()
    source.close()

    return len(pages)