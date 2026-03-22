import psycopg2
import polars as pl

def get_connection():
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host="host.docker.internal",
        port="5432",
        dbname="manufacturing_pipline",
        user="ivan",
        password=""
    )
    return conn

def insert_metrics(df: pl.DataFrame) -> None:
        conn = get_connection()
        cur = conn.cursor()

        insert_query = """
        INSERT INTO machine_metrics (
            machine_id,
            avg_temp,
            max_temp,
            max_pressure,
            avg_cycle_time,
            anomaly
        )
        VALUES (%s, %s, %s, %s, %s, %s);
        """

        for row in df.iter_rows(named=True):
            cur.execute(
                insert_query,
                (
                    row["machine_id"],
                    row["avg_temp"],
                    row["max_temp"],
                    row["max_pressure"],
                    row["avg_cycle_time"],
                    row["anomaly"]
                ),
            )

        conn.commit()
        cur.close()
        conn.close()