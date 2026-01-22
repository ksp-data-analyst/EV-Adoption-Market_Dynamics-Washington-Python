#!/usr/bin/env python3
"""
Script to upload Electric Vehicle Population Data CSV into SQLite database
"""

import csv
import sqlite3
import os

# Paths
csv_file = "/Users/kishansanjaypatil/Downloads/Kishan Patil (Data Analysis)/Electric_Vehicle_Analysis(Washington.DC)/Electric_Vehicle_Population_Data.csv"
db_file = "/Users/kishansanjaypatil/Downloads/Kishan Patil (Data Analysis)/Electric_Vehicle_Analysis(Washington.DC)/Data.db"

# Database table name
table_name = "electric_vehicle_analysis"

def create_database():
    """Create SQLite database and table"""
    # Remove existing database if it exists
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing database: {db_file}")
    
    # Connect to database (creates new one)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Create table with appropriate schema
    create_table_sql = f"""
    CREATE TABLE {table_name} (
        vin TEXT PRIMARY KEY,
        county TEXT,
        city TEXT,
        state TEXT,
        postal_code TEXT,
        model_year INTEGER,
        make TEXT,
        model TEXT,
        electric_vehicle_type TEXT,
        cafv_eligibility TEXT,
        electric_range INTEGER,
        base_msrp INTEGER,
        legislative_district INTEGER,
        dol_vehicle_id INTEGER,
        vehicle_location TEXT,
        electric_utility TEXT,
        census_tract TEXT
    )
    """
    
    cursor.execute(create_table_sql)
    conn.commit()
    print(f"Created table: {table_name}")
    
    return conn

def import_csv_data(conn, csv_file):
    """Import data from CSV file into database"""
    cursor = conn.cursor()
    
    row_count = 0
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        
        # Map CSV columns to database columns
        columns = [
            'vin', 'county', 'city', 'state', 'postal_code', 'model_year',
            'make', 'model', 'electric_vehicle_type', 'cafv_eligibility',
            'electric_range', 'base_msrp', 'legislative_district', 
            'dol_vehicle_id', 'vehicle_location', 'electric_utility', 'census_tract'
        ]
        
        insert_sql = f"""
        INSERT INTO {table_name} (
            vin, county, city, state, postal_code, model_year, make, model,
            electric_vehicle_type, cafv_eligibility, electric_range, base_msrp,
            legislative_district, dol_vehicle_id, vehicle_location, 
            electric_utility, census_tract
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        for row in csv_reader:
            try:
                # Handle empty strings and convert to appropriate types
                model_year = int(row['Model Year']) if row['Model Year'] else None
                electric_range = int(row['Electric Range']) if row['Electric Range'] else None
                base_msrp = int(row['Base MSRP']) if row['Base MSRP'] else None
                legislative_district = int(row['Legislative District']) if row['Legislative District'] else None
                dol_vehicle_id = int(row['DOL Vehicle ID']) if row['DOL Vehicle ID'] else None
                
                values = (
                    row['VIN (1-10)'],
                    row['County'] if row['County'] else None,
                    row['City'] if row['City'] else None,
                    row['State'] if row['State'] else None,
                    row['Postal Code'] if row['Postal Code'] else None,
                    model_year,
                    row['Make'],
                    row['Model'],
                    row['Electric Vehicle Type'] if row['Electric Vehicle Type'] else None,
                    row['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] if row['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] else None,
                    electric_range,
                    base_msrp,
                    legislative_district,
                    dol_vehicle_id,
                    row['Vehicle Location'] if row['Vehicle Location'] else None,
                    row['Electric Utility'] if row['Electric Utility'] else None,
                    row['2020 Census Tract'] if row['2020 Census Tract'] else None
                )
                
                cursor.execute(insert_sql, values)
                row_count += 1
                
                # Commit every 10000 rows for better performance
                if row_count % 10000 == 0:
                    conn.commit()
                    print(f"Imported {row_count} rows...")
                    
            except Exception as e:
                print(f"Error importing row {row_count + 1}: {e}")
                continue
    
    conn.commit()
    return row_count

def verify_data(conn):
    """Verify the imported data"""
    cursor = conn.cursor()
    
    # Get total count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_count = cursor.fetchone()[0]
    print(f"\nTotal rows in database: {total_count}")
    
    # Show sample data
    print("\nSample data (first 5 rows):")
    cursor.execute(f"SELECT vin, make, model, model_year, electric_vehicle_type FROM {table_name} LIMIT 5")
    for row in cursor.fetchall():
        print(f"  {row}")
    
    # Show distinct makes
    print("\nDistinct vehicle makes:")
    cursor.execute(f"SELECT DISTINCT make FROM {table_name} ORDER BY make")
    makes = cursor.fetchall()
    for make in makes[:10]:
        print(f"  {make[0]}")
    if len(makes) > 10:
        print(f"  ... and {len(makes) - 10} more")

def main():
    print("=" * 60)
    print("Electric Vehicle Data - CSV to SQLite Import")
    print("=" * 60)
    print(f"\nCSV File: {csv_file}")
    print(f"Database: {db_file}")
    print()
    
    # Create database and table
    conn = create_database()
    
    # Import data
    print("\nImporting data from CSV...")
    row_count = import_csv_data(conn, csv_file)
    print(f"\nSuccessfully imported {row_count} rows!")
    
    # Verify data
    print("\nVerifying imported data...")
    verify_data(conn)
    
    # Close connection
    conn.close()
    print(f"\nDatabase created successfully: {db_file}")
    print("=" * 60)

if __name__ == "__main__":
    main()

