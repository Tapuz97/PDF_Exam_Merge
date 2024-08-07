import os
import logging
from PyPDF2 import PdfMerger

# Set up logging
logging.basicConfig(
    filename='file_operations.log',  # Log file path
    level=logging.INFO,              # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

# Define paths
question_folder = "Q"
answer_folder = "A"
merged_folder = "Merged"

# Create Merged folder if it doesn't exist
os.makedirs(merged_folder, exist_ok=True)

# Rename PDF files in the given folder by appending a suffix.
def rename_files(folder, suffix):
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            base_name, _ = os.path.splitext(filename)
            new_name = f"{base_name}{suffix}.pdf"
            try:
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
                logging.info(f"Renamed {filename} to {new_name} in {folder}")
                print(f"Successfully renamed {filename} to {new_name} in {folder}.")
            except Exception as e:
                logging.error(f"Failed to rename {filename} in {folder}: {e}")
                print(f"Error: Failed to rename {filename} in {folder}. See log for details.")

# Merge corresponding Q and A PDFs and save them in the Merged folder.
def merge_pdf(q_folder, a_folder, merged_folder):
    q_files = sorted(os.listdir(q_folder))
    a_files = sorted(os.listdir(a_folder))

    # Create a set of base names for Q and A files to easily find matches
    q_base_names = {q_file.replace("Q.pdf", "") for q_file in q_files if q_file.endswith("Q.pdf")}
    a_base_names = {a_file.replace("A.pdf", "") for a_file in a_files if a_file.endswith("A.pdf")}

    # Find all unique base names
    all_base_names = q_base_names.union(a_base_names)

    for base_name in all_base_names:
        q_file = f"{base_name}Q.pdf"
        a_file = f"{base_name}A.pdf"
        
        q_path = os.path.join(q_folder, q_file)
        a_path = os.path.join(a_folder, a_file)

        try:
            if not os.path.exists(q_path):
                raise FileNotFoundError(f"Question file {q_file} is missing.")
            if not os.path.exists(a_path):
                raise FileNotFoundError(f"Answer file {a_file} is missing.")

            merger = PdfMerger()
            merger.append(q_path)
            merger.append(a_path)
            output_path = os.path.join(merged_folder, f"{base_name}.pdf")
            merger.write(output_path)
            merger.close()
            logging.info(f"Merged {q_file} and {a_file} into {output_path}")
            print(f"Successfully merged {q_file} and {a_file} into {output_path}.")

        except FileNotFoundError as e:
            logging.warning(e)
            print(f"Warning: {e}")
        except Exception as e:
            logging.error(f"Failed to merge {q_file} and {a_file}: {e}")
            print(f"Error: Failed to merge {q_file} and {a_file}. See log for details.")

# Step 1: Rename files in Q and A folders
rename_files(question_folder, "Q")
rename_files(answer_folder, "A")

# Step 2: Merge PDFs
merge_pdf(question_folder, answer_folder, merged_folder)
