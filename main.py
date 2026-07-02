from pathlib import Path
import os
from modules.pdf_tools import sort_pdf_by_last4
from tkinter import Tk, filedialog, messagebox




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
    os.startfile(output_pdf.parent)

    messagebox.showinfo(
        "Готово",
        f"Сортировка завершена!\n\n"
        f"Файл:\n{output_pdf.name}\n\n"
        f"Страниц: {count}"
    )


if __name__ == "__main__":
    main()