from data_generator import generate_machine_data
from processor import process_data
from db import insert_metrics

def main():
    # Step 1: Generate data
    file_path = generate_machine_data(200)

    # Step 2: Process data
    results = process_data(file_path)


    print("\nProcessed Machine Metrics:\n")
    print(results)

    insert_metrics(results)
    print("\nMetrics inserted into PostgreSQL successfully.")

if __name__ == "__main__":
    main()