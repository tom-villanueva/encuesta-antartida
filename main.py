import pandas as pd

FILE_NAME = 'RESULTADOS.xlsx'
pd.set_option("display.max_rows", None)

def main():
	data = pd.read_excel(FILE_NAME)
	print(data.dtypes)
	print(data['edad'].value_counts())
	print(data['ocupacion'].value_counts())


if __name__ == '__main__':
	main()