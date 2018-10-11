import csv
import xlrd


def xlsx_reader(path):
    rb = xlrd.open_workbook(path, formatting_info=False)
    sheet = rb.sheet_by_index(0)
    return [sheet.row_values(i) for i in range(sheet.nrows)]

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for line in data:
            writer.writerow(line)


if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    # 1) записываем в файл output.csv содержимой словаря data
    print(data)
    out_file = "output.csv"
    csv_writer(data, out_file)

    # 2) получает данные из файле ddata.xlsx
    # записывает эти данные в файл
    in_file = 'ddata.xlsx'
    out_file = "output_1.csv"

    data = xlsx_reader(in_file)
    csv_writer(data, out_file)
