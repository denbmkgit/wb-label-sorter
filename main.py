from pathlib import Path

from modules.pdf_tools import sort_pdf_by_last4


DATA_FOLDER = Path("data")


def main():
    print("=" * 45)
    print("WB Label Sorter Pro v0.1")
    print("=" * 45)
    print()

    pdf_files = sorted(DATA_FOLDER.glob("*.pdf"))

    if not pdf_files:
        print("Положите PDF файл в папку data")
        return

    if len(pdf_files) > 1:
        print("В папке data должен быть только один PDF файл")
        return

    input_pdf = pdf_files[0]

    output_pdf = input_pdf.with_name(
        input_pdf.stem + "_sorted.pdf"
    )

    count = sort_pdf_by_last4(input_pdf, output_pdf)

    print(f"Файл: {input_pdf.name}")
    print(f"Страниц: {count}")
    print(f"Создан: {output_pdf.name}")
    print()
    print("=" * 45)


if __name__ == "__main__":
    main()