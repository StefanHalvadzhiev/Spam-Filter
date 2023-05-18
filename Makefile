.PHONY: download_dataset
download_dataset:
	kaggle datasets download -d balaka18/email-spam-classification-dataset-csv
	tar -xf email-spam-classification-dataset-csv.zip
	del email-spam-classification-dataset-csv.zip
	if not exist data mkdir data
	move emails.csv data\