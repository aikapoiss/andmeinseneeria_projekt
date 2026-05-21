#!/usr/bin/env python3
"""
Data collection script for TfL BikePoint API

Usage:
    python scripts/collect_data.py

This script fetches the current state of all BikePoint stations
and saves the snapshot to data/raw/ directory.
"""

import json
import os
from datetime import datetime


def main():
    """
    Main data collection function
    """
    print("Data collection script - TfL BikePoint API")
    print("============================================")
    print()
    print("TODO: Implement API data collection")
    print()
    print("Steps to implement:")
    print("1. Load configuration from config/settings.yaml")
    print("2. Create API client (src/collectors/bike_api.py)")
    print("3. Fetch all BikePoint stations")
    print("4. Save snapshot to data/raw/ with timestamp")
    print("5. Implement error handling and retries")
    print("6. Schedule periodic collection (src/scripts/schedule_collector.py)")
    print()
    print("Example API call:")
    print("  requests.get('https://api.tfl.gov.uk/BikePoint')")
    print()


if __name__ == "__main__":
    main()
