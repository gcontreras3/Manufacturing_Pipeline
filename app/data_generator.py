import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

def generate_machine_data(rows: int = 100) -> str:
    data_dir = Path("../data")
    data_dir.mkdir(exist_ok=True)
    
    file_path = data_dir / "machine_data.csv"

    machine_ids = ["M-100", "M-200", "M-300", "M-400"]
    start_time = datetime.now()

    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "machine_id",
            "timestamp",
            "temperature",
            "pressure",
            "cycle_time",
            "status",
        ])

        for i in range(rows):
            machine_id = random.choice(machine_ids)
            timestamp = start_time + timedelta(minutes=i)
            temperature = round(random.uniform(65.0, 95.0), 2)
            pressure = round(random.uniform(20.0, 50.0), 2)
            cycle_time = round(random.uniform(1.0, 5.0), 2)
            status = random.choice(["OK", "OK", "OK", "WARNING"])

            writer.writerow([
                machine_id,
                timestamp.isoformat(),
                temperature,
                pressure,
                cycle_time,
                status,
            ])

    return str(file_path)