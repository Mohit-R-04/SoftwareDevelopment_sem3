# Hospital Management System

A comprehensive Hospital Management System built with Python and PySide6, featuring a modern UI and Oracle database integration. This system helps manage patients, doctors, appointments, and billing in a hospital setting.

## Features

- 📊 Interactive Dashboard
- 👨‍⚕️ Doctor Management
- 🏥 Patient Records
- 📅 Appointment Scheduling
- 💰 Billing and Payments
- 📱 QR Code Generation for Payments
- 📧 Email Notifications
- 📊 Real-time Statistics

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- Oracle Database XE (Express Edition)
- Git (for cloning the repository)

### Python Dependencies
```bash
PySide6>=6.0.0
oracledb
qrcode
pillow
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mohit-R-04/SoftwareDevelopment_sem3.git
cd SoftwareDevelopment_sem3
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Oracle Database:
   - Install Oracle Database XE
   - Run the SQL scripts in the `DB_executions` folder to create necessary tables and sequences
   - Create a database user with the following credentials (or modify in main.py):
     ```
     Username: hospital_user
     Password: mohit123
     DSN: localhost:1521/XE
     ```

4. Configure the application:
   - Update database credentials in `main.py` if necessary
   - Configure email settings in `send_mail.py` if you want to use email notifications

## Running the Application

1. Start the Oracle Database service

2. Run the main application:
```bash
python main.py
```

## Project Structure

- `main.py`: Main application file
- `dbHMS.py`: Database management and command pattern implementation
- `HMS.ui`: Qt Designer UI file
- `ui_HMS.py`: Generated UI Python code
- `send_mail.py`: Email notification functionality
- `DB_executions/`: SQL scripts for database setup
- `stock_png/`: Image assets for the UI

## Database Schema

The system uses the following main tables:
- Doctors
- Patients
- Appointments
- Medical Problems
- Billing Records

Refer to `schema diagram.png` for the complete database structure.

## Design Patterns Used

- Singleton Pattern: Database connection management
- Command Pattern: Database operations
- MVC Pattern: Overall application architecture

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- PySide6 for the modern UI components
- Oracle Database for reliable data storage
- QR Code generation for payment processing
