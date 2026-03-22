import polars as pl
import numpy as np

def process_data(file_path: str) -> pl.DataFrame:
    # Load the data (CSV)
    df = pl.read_csv(file_path)

    # Basic cleaning (remove nulls just in case)
    df = df.drop_nulls()

    # Convert columns to proper data types (saftey)
    df = df.with_columns([
        pl.col("temperature").cast(pl.Float64),
        pl.col("pressure").cast(pl.Float64),
        pl.col("cycle_time").cast(pl.Float64),
    ])

    # Group by machine and calculate metrics
    grouped = df.group_by("machine_id").agg([
        pl.col("temperature").mean().alias("avg_temp"),
        pl.col("temperature").max().alias("max_temp"),
        pl.col("pressure").max().alias("max_pressure"),
        pl.col("cycle_time").mean().alias("avg_cycle_time"),
    ])

    # Convert to numpy for anomaly detection
    temps = grouped["avg_temp"].to_numpy()

    mean_temp = np.mean(temps)
    std_temp = np.std(temps)

    # Flag anomalies (simple z-score logic)
    anomaly_flags = []
    for temp in temps:
        if abs(temp - mean_temp) > 2 * std_temp:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)

    # Add anomaly column
    grouped = grouped.with_columns(
        pl.Series("anomaly", anomaly_flags)
    )

    return grouped