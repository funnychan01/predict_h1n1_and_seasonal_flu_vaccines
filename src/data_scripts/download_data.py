import pandas as pd  

url_train_feat = "https://drivendata-prod.s3.amazonaws.com/data/66/public/training_set_features.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCYSN7TAHVS%2F20250429%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250429T021900Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2b3256673fe72255ccab65917e3b0dd1cc969768ec9cd715805f9bc50e060abb"
url_train_label = "https://drivendata-prod.s3.amazonaws.com/data/66/public/training_set_labels.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCYSN7TAHVS%2F20250429%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250429T021900Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c22e352f721be86cce177aba869ebdd97c39b52bf3426ca9ce8b43c5af901b0d"
url_test_feat = "https://drivendata-prod.s3.amazonaws.com/data/66/public/test_set_features.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARVBOBDCYSN7TAHVS%2F20250429%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250429T021900Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c1d0159f61c082d4d4a0fbc352c2f22fcc85afa363df490542077e3fb8a3bf0"

file_name_train_feat = "training_set_features.csv"
file_name_train_label = "training_set_labels.csv"
file_name_test_feat = "test_set_features.csv"

project_data_path = "/Users/jackie/Documents/data_science/projects/predict_h1n1_and_seasonal_flu_vaccines/data/raw/"

# Input: URLs of datasets
data = pd.read_csv(url_train_feat)

# Output: Save the datasets to the project direcotry
data.to_csv(project_data_path+file_name_train_feat, index=False)

# Input: URLs of datasets
data = pd.read_csv(url_train_label)

# Output: Save the datasets to the project direcotry
data.to_csv(project_data_path+file_name_train_label, index=False)

# Input: URLs of datasets
data = pd.read_csv(url_test_feat)

# Output: Save the datasets to the project direcotry
data.to_csv(project_data_path+file_name_test_feat, index=False)