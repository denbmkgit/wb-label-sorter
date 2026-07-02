from pathlib import Path
from modules.pdf_tools import sort_pdf_by_last4
from tkinter import Tk, filedialog




def main():
    print("=" * 45)
    print("WB Label Sorter Pro v0.1")
    print("=" * 45)
    print()

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    filename = filedialog.askopenfilename(
        title="Выберите PDF с этикетками WB",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not filename:
        print("Файл не выбран.")
        return

    input_pdf = Path(filename)

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