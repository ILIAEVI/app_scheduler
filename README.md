# App Scheduler using Django Rest Framework

This project is a Django-based application scheduler that manages application start times in a 24-hour cycle. The system ensures that applications are "on" for 16 hours and "off" for the next 8 hours. The application exposes a REST API to manage and monitor clients and their scheduling statuses.

## Features

- **Time-Based Scheduling**: Automatically schedules applications based on their start time, ensuring they run for 16 hours and remain off for 8 hours within a 24-hour period.
- **REST API**: Provides API endpoints for managing clients and retrieving their scheduling statuses.
- **Custom Logic**: Implements custom logic to calculate whether an application should be running based on the current time.

## Technologies Used

- **Python**
- **Django**
- **Django Rest Framework**
- **PostgreSQL**

