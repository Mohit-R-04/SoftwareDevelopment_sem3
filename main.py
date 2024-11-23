# Inbuilt modules
import datetime
from datetime import date
import sys
import sys
import io
import qrcode
import re

from PySide6 import QtCore
from PySide6.QtCore import QDate, Qt, QTimer, QPointF
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QCompleter,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QMessageBox, QDialog, QLabel,
    QWidget, QGraphicsScene, QVBoxLayout,
    QGraphicsPixmapItem, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QPixmap, QImage

# User-defined modules
import send_mail
from ui_HMS import Ui_MainWindow  # This is your auto-generated UI class
from dbHMS import *

class HMSApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize the UI components defined in ui_HMS.py
        self.setWindowTitle("Hospital Management System")
        self.managepatientsrecords.setCurrentIndex(4)
        self._DB_USER = "hospital_user"
        self._DB_PASSWORD = "mohit123"
        self._DB_DSN = "localhost:1521/XE"
        self.db_manager = DatabaseManager.get_instance(user=self._DB_USER, password=self._DB_PASSWORD, dsn=self._DB_DSN)

        # Fetch and set up initial data for problems
        probs_select_command = SelectCommand("SELECT * FROM medical_problems")
        self.problems_tuple = probs_select_command.execute(self.db_manager)

        self.set_up_dashboard()
        self.ui_essentials()
        self.essential_runs()

    def ui_essentials(self):
        self.dashboard.clicked.connect(self.switch_to_dashboard)
        self.dashboard_expand.clicked.connect(self.switch_to_dashboard)
        self.appointment.clicked.connect(self.switch_to_appointment)
        self.appointment_expand.clicked.connect(self.switch_to_appointment)
        self.doctorentry.clicked.connect(self.switch_to_doctor)
        self.doctorentry_expand.clicked.connect(self.switch_to_doctor)
        self.patientrecord.clicked.connect(self.switch_to_patient)
        self.patientrecord_expand.clicked.connect(self.switch_to_patient)
        self.billing.clicked.connect(self.switch_to_billing)
        self.billing_expand.clicked.connect(self.switch_to_billing)
        self.iconname.setHidden(True)

        # close db connection if exist
        self.exit.clicked.connect(self.close_db_connection)
        self.exit_expand.clicked.connect(self.close_db_connection)

        gender = ["male", "female", "others"]
        completergender = QCompleter(gender)
        completergender.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.bookappointment_tabentry_gender.setCompleter(completergender)

        prob_list = [tup[1] for tup in self.problems_tuple]
        completerproblems = QCompleter(prob_list)
        completerproblems.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.bookappointment_tabentry_medicalcondition.setCompleter(completerproblems)
        self.bookappointment_tabentry_appointmentdate.setDate(QDate.currentDate())

    def set_up_dashboard(self):
        # Set up the QGraphicsScene and assign it to the graphics view
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)  # graphicsView is from your UI

        # Load the PNG image
        pixmap = QPixmap("animation.png")
        
        # Scale the pixmap to zoom it (for example, scale it to 1.5 times the original size)
        scaled_pixmap = pixmap.scaled(pixmap.width() * 0.8, pixmap.height() * 1.5, Qt.KeepAspectRatio)

        # Create a QGraphicsPixmapItem with the scaled image
        self.pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
        self.scene.addItem(self.pixmap_item)

        # Apply shadow effect to the image
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setOffset(5, 5)  # Shadow offset
        shadow_effect.setBlurRadius(10)  # Shadow blur radius
        shadow_effect.setColor(Qt.black)  # Shadow color
        self.pixmap_item.setGraphicsEffect(shadow_effect)

        # Center the image in the view
        self.center_image()
        self.dashboard_refresh()

    def dashboard_refresh(self):
        # display information
        active_user_command = SelectCommand(f"select count(*) from patient where status = 'Y'")
        active_users = active_user_command.execute(self.db_manager)[0][0]
        available_doc_command = SelectCommand("select count(*) from doctor where status = 'A'")
        working_doc_command = SelectCommand("select count(*) from doctor where status = 'NA'")
        available_doc = available_doc_command.execute(self.db_manager)[0][0]
        working_doc = working_doc_command.execute(self.db_manager)[0][0]
        self.lcdNumber_patient_count.display(active_users)
        self.lcdNumber_available_doctors.display(available_doc)
        self.lcdNumber_notavailable_doctors.display(working_doc)


    def center_image(self):
        # Center the pixmap item within the view
        view_rect = self.graphicsView.viewport().rect()
        scene_pos = self.graphicsView.mapToScene(view_rect.center())
        
        # Position image at center
        self.pixmap_item.setPos(scene_pos.x() - self.pixmap_item.boundingRect().width() / 2,
                                scene_pos.y() - self.pixmap_item.boundingRect().height() / 2)

    def essential_runs(self):
        self.bookappointment_tabentry_button.clicked.connect(self.book_appointment)
        self.appointment.clicked.connect(self.refresh_appointment_records)
        self.appointment_expand.clicked.connect(self.refresh_appointment_records)
        self.bookappointment_tabcancel_searchbutton.clicked.connect(self.search_appointment_cancel)
        self.bookappointment_tabcompleted_searchbutton.clicked.connect(self.search_appointment_completed)
        self.bookappointment_tabcancel_buttondelete.clicked.connect(self.delete_appointment)

        self.doctorentry.clicked.connect(self.refresh_doctor_records)
        self.doctorentry_expand.clicked.connect(self.refresh_doctor_records)
        self.doctorsavailablity_tabadddoc_button.clicked.connect(self.add_doctor)
        self.doctorsavailablity_tabdeletedoc_deletebutton.clicked.connect(self.delete_doctor)
        self.doctorsavailablity_tabavailable_marknotavailablebutton.clicked.connect(self.mark_doc_notavailable)
        self.doctorsavailablity_tabnotavailable_markavailablebutton.clicked.connect(self.mark_doc_available)
        self.doctorsavailablity_tabworking_searchbutton.clicked.connect(self.search_working_doctors)
        self.doctorsavailablity_tabnotavailable_searchbutton.clicked.connect(self.search_not_available_doctors)
        self.doctorsavailablity_tabavailable_searchbutton.clicked.connect(self.search_available_doctors)
        self.doctorsavailablity_tabdeletedoc_searchbutton.clicked.connect(self.search_delete_doctor)

        self.patientrecord.clicked.connect(self.refresh_patient_records)
        self.patientrecord_expand.clicked.connect(self.refresh_patient_records)
        self.managepatientsrecords_tabrecords_searchbutton.clicked.connect(self.search_patient_t1)
        self.managepatientsrecords_tabrecords_searchbutton_past.clicked.connect(self.search_patient_t2)
        self.managepatientsrecords_tabdelete_searchbutton.clicked.connect(self.search_patient_t3)
        self.managepatientsrecords_tabdelete_deletebutton.clicked.connect(self.delete_patient)
        self.managepatientsrecords_tabdelete_deletebutton.clicked.connect(self.refresh_patient_records)

        self.billing.clicked.connect(self.refresh_billing_records)
        self.billing_expand.clicked.connect(self.refresh_billing_records)
        self.billing_search_button.clicked.connect(self.search_billing)
        self.billing_pay.clicked.connect(self.make_payment)
        self.billing_data.clicked.connect(self.get_data)
        
    def close_db_connection(self):
        if self.db_manager.connection:
            self.db_manager.connection.close()

    def switch_to_dashboard(self):
        self.managepatientsrecords.setCurrentIndex(4)

    def switch_to_appointment(self):
        self.managepatientsrecords.setCurrentIndex(2)
    
    def switch_to_doctor(self):
        self.managepatientsrecords.setCurrentIndex(0)

    def switch_to_patient(self):
        self.managepatientsrecords.setCurrentIndex(1)

    def switch_to_billing(self):
        self.managepatientsrecords.setCurrentIndex(3)

    def is_valid_domain(self, email):
        # Regex pattern to allow emails that contain '@' and end with valid domains and subdomains (e.g., '.com', '.in', '.edu.in')
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
        return re.match(pattern, email) is not None

    def book_appointment(self):
        with DatabaseManager.get_instance(user=self._DB_USER, password=self._DB_PASSWORD, dsn=self._DB_DSN) as db_manager:
            self.bookappointment_tabentry_dispprob.clear()
            name = self.bookappointment_tabentry_name.text()
            dob_unformatted = self.bookappointment_tabentry_dob.date()
            dob = dob_unformatted.toString("yyyy-MM-dd")
            gender = self.bookappointment_tabentry_gender.text()
            medical_condition = self.bookappointment_tabentry_medicalcondition.text()
            email = self.bookappointment_tabentry_contact.text()
            appointment_date_unformatted = self.bookappointment_tabentry_appointmentdate.date()
            appointment_date = appointment_date_unformatted.toString("yyyy-MM-dd")
            house_no = self.bookappointment_tabentry_houseno.text()
            city = self.bookappointment_tabentry_city.text()
            state = self.bookappointment_tabentry_state.text()
            problems = [i[1] for i in self.problems_tuple]
            if not (name and email and gender and medical_condition and appointment_date and house_no and city and state):
                self.bookappointment_tabentry_dispprob.setText("All fields are required")
                return
            if medical_condition not in problems:
                self.bookappointment_tabentry_dispprob.setText("Enter proper Medical condition")
                return
            if gender not in ["male","female","others"]:
                self.bookappointment_tabentry_dispprob.setText("Enter proper gender")
                return
            if self.is_valid_domain(email) == False:
                self.bookappointment_tabentry_dispprob.setText("Enter proper email")
                return 
            doctor_select_command = SelectCommand(f"SELECT doctor_id, name FROM doctor where specialization = '{medical_condition}' and status = 'A'")
            doctor_tuple = doctor_select_command.execute(db_manager)
            if doctor_tuple:
                doctors = [tup[1] for tup in doctor_tuple]
            else:
                doctors = None
            if doctors == None:
                send_mail.Send("sorry ! Your appointment has been Rejected 🥲", email, name, "not assigned" , appointment_date,"not assigned",medical_condition)
                QMessageBox.warning(self, "Warning", "Sorry! Your appointment has been rejected!", QMessageBox.Ok)
            else:
                insert_into_patient = InsertCommand(f"INSERT INTO patient (NAME, DOB, GENDER, MEDICAL_CONDITION, STATUS) VALUES ('{name}', TO_DATE('{dob}','YYYY-MM-DD'), '{gender}', '{medical_condition}', 'Y')")
                insert_into_patient.execute(db_manager)
                select_id = SelectCommand("SELECT patient_seq.CURRVAL FROM DUAL")
                id = select_id.execute(db_manager)
                id = f"P{id[0][0]}" # without this id will be like [(2,)] instead of P2
                insert_into_patient_contact = InsertCommand(f"insert into patient_contact values ('{id}','{email}')")
                insert_into_patient_address = InsertCommand(f"insert into patient_address values ('{id}','{house_no}','{city}','{state}')")
                insert_into_patient_contact.execute(db_manager)
                insert_into_patient_address.execute(db_manager)
                insert_into_appointment = InsertCommand(f"insert into appointment (PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, STATUS) values ('{id}','{doctor_tuple[0][0]}',TO_DATE('{appointment_date}','YYYY-MM-DD'),'Y')")
                insert_into_appointment.execute(db_manager)
                alter_doctor = UpdateCommand(f"update doctor set status = 'W' where doctor_id = '{doctor_tuple[0][0]}'")
                alter_doctor.execute(db_manager)
                self.refresh_doctor_records()
                QMessageBox.information(self, "Success", "Appointment booked successfully.", QMessageBox.Ok)
                send_mail.Send("Your appointment has been booked successfully! 😊",email, name, id, appointment_date, doctor_tuple[0][1],medical_condition)
                self.bookappointment_tabentry_name.clear()
                self.bookappointment_tabentry_gender.clear()
                self.bookappointment_tabentry_medicalcondition.clear()
                self.bookappointment_tabentry_contact.clear()
                self.bookappointment_tabentry_houseno.clear()
                self.bookappointment_tabentry_city.clear()
                self.bookappointment_tabentry_state.clear()
                self.refresh_appointment_records()

    def refresh_doctor_records(self):
        self._refresh_doctor(self.doctorsavailablity_tabnotavailable_view,'NA')
        self._refresh_doctor(self.doctorsavailablity_tabavailable_view,'A')
        self._refresh_doctor(self.doctorsavailablity_tabworking_searchview, 'W')
        self._refresh_doctor(self.doctorsavailablity_tabdeletedoc_view,condition=None)
        self.set_up_dashboard()

    def _refresh_doctor(self,a,condition):
        a.setColumnCount(0)
        a.setColumnCount(4)
        a.setHorizontalHeaderLabels(["id","Doctor Name","Specialization","Contact"])
        a.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if condition:
            docselect = f"""
            SELECT d.doctor_id, d.Name, d.specialization, dc.contact
            FROM doctor d
            INNER JOIN doctor_contact dc ON d.doctor_id = dc.doctor_id
            WHERE d.status = '{condition}'
            """
        else:
            docselect = f"""
            SELECT d.doctor_id, d.Name, d.specialization, dc.contact
            FROM doctor d
            INNER JOIN doctor_contact dc ON d.doctor_id = dc.doctor_id
            """
        selectcommand = SelectCommand(docselect)
        doctor_records = selectcommand.execute(self.db_manager)
        a.setRowCount(len(doctor_records))
        for row_index, (id, name, specialization, phone) in enumerate(doctor_records):
            a.setItem(row_index, 0, QTableWidgetItem(id))
            a.setItem(row_index, 1, QTableWidgetItem(name))
            a.setItem(row_index, 2, QTableWidgetItem(specialization))
            a.setItem(row_index, 3, QTableWidgetItem(phone))
        
    def _search_doctor(self, table_widget, search_text=None):
        """
        Searches for doctors based on user input in doctor ID or name and displays
        the results in the specified table widget. Allows filtering by doctor status.
        """
        if not search_text:
            self.refresh_doctor_records()
            return
        search_text = search_text.lower()
        query = f'''
            SELECT d.doctor_id, d.name, d.specialization, dc.contact
            FROM doctor d
            INNER JOIN doctor_contact dc ON d.doctor_id = dc.doctor_id
            WHERE (LOWER(d.name) LIKE '%' || '{search_text}' || '%' 
                OR LOWER(d.doctor_id) LIKE '%' || '{search_text}' || '%')
        '''
        
        select_command = SelectCommand(query)
        doctor_records = select_command.execute(self.db_manager)

        table_widget.setColumnCount(0)
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(["id", "Doctor Name", "Specialization", "Contact"]) 
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Display the results in the specified table widget
        table_widget.setRowCount(len(doctor_records))
        for row_index, (id, name, specialization, contact) in enumerate(doctor_records):
            table_widget.setItem(row_index, 0, QTableWidgetItem(id))
            table_widget.setItem(row_index, 1, QTableWidgetItem(name))
            table_widget.setItem(row_index, 2, QTableWidgetItem(specialization))
            table_widget.setItem(row_index, 3, QTableWidgetItem(contact))

    def search_working_doctors(self):
        text = self.doctorsavailablity_tabworking_searchentry.text()
        self._search_doctor(self.doctorsavailablity_tabworking_searchview, text)

    def search_not_available_doctors(self):
        text = self.doctorsavailablity_tabnotavailable_searchentry.text()
        self._search_doctor(self.doctorsavailablity_tabnotavailable_view, text)

    def search_available_doctors(self):
        text = self.doctorsavailablity_tabavailable_searchentry.text()
        self._search_doctor(self.doctorsavailablity_tabavailable_view, text)

    def search_delete_doctor(self):
        text = self.doctorsavailablity_tabdeletedoc_searchentry.text()
        self._search_doctor(self.doctorsavailablity_tabdeletedoc_view, text)

    def add_doctor(self):
        contact = self.doctorsavailablity_tabadddoc_contact.text()
        name = self.doctorsavailablity_tabadddoc_name.text()
        department = self.doctorsavailablity_tabadddoc_dept.text()
        house_no = self.doctorsavailablity_tabadddoc_houseno.text()
        state = self.doctorsavailablity_tabadddoc_state.text()
        salary = self.doctorsavailablity_tabadddoc_salary.text()
        city = self.doctorsavailablity_tabadddoc_city.text()
        #check all values are available
        if not (name and department and contact and house_no and city and state and salary):
            self.doctorsavailablity_tabadddoc_dispprob.setText("All fields are required")
        insertdoc = InsertCommand(f"insert into doctor (name, specialization, status) values ('{name}', '{department}', 'A')")
        insertdoc.execute(self.db_manager)
        select_id = SelectCommand("SELECT doctor_seq.CURRVAL FROM DUAL")
        id = select_id.execute(self.db_manager)
        id = f"D{id[0][0]}"
        insertdoc_contact = InsertCommand(f"insert into doctor_contact values ('{id}','{contact}')")
        insertdoc_address = InsertCommand(f"insert into doctor_address values ('{id}','{house_no}','{city}','{state}')")
        insertdoc_contact.execute(self.db_manager)
        insertdoc_address.execute(self.db_manager)
        self.refresh_doctor_records()

    def _change_doc_status(self, table_widget, status):
        table_name = 'doctor'
        selected_row = table_widget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row.",
                                QMessageBox.Ok)
            if QMessageBox.Ok:
                return
            return
        record_id = table_widget.item(selected_row, 0).text()
        update_status = UpdateCommand(f"update {table_name} set status = '{status}' where doctor_id = '{record_id}'")
        update_status.execute(self.db_manager)
        self.refresh_doctor_records()


    def mark_doc_notavailable(self):
        self._change_doc_status(self.doctorsavailablity_tabavailable_view, 'NA')
        
    def mark_doc_available(self):
        self._change_doc_status(self.doctorsavailablity_tabnotavailable_view, 'A')

    def _refresh_patient(self, a, condition=None):
        a.setColumnCount(0)
        a.setColumnCount(4)
        a.setHorizontalHeaderLabels(["id", "Patient Name", "medical_condition", "Allotted Doctor"])
        a.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Corrected SQL query (removed semicolon at the end)
        if condition is None:
            patientselect = '''
            SELECT 
                p.PATIENT_ID,
                p.NAME AS PATIENT_NAME,
                p.MEDICAL_CONDITION,
                d.NAME AS ALLOTTED_DOCTOR
            FROM 
                PATIENT p
            JOIN 
                APPOINTMENT a ON p.PATIENT_ID = a.PATIENT_ID
            JOIN 
                DOCTOR d ON a.DOCTOR_ID = d.DOCTOR_ID
            WHERE 
                a.STATUS = 'Y'
            '''
        else:
            patientselect = f'''
            SELECT 
                p.PATIENT_ID,
                p.NAME AS PATIENT_NAME,
                p.MEDICAL_CONDITION,
                d.NAME AS ALLOTTED_DOCTOR
            FROM 
                PATIENT p
            JOIN 
                APPOINTMENT a ON p.PATIENT_ID = a.PATIENT_ID
            JOIN 
                DOCTOR d ON a.DOCTOR_ID = d.DOCTOR_ID
            WHERE 
                a.STATUS = '{condition}' and 
                p.STATUS = '{condition}'
            '''
        
        # Execute the select command
        selectcommand = SelectCommand(patientselect)
        patient_records = selectcommand.execute(self.db_manager)
        
        # Verify patient_records before setting row count
        if patient_records is None:
            print("Error: Query did not return any results.")
            return
        
        # Set the row count based on fetched records
        a.setRowCount(len(patient_records))
        
        # Populate the table with the retrieved data
        for row_index, (patient_id, patient_name, medical_condition, doctor_name) in enumerate(patient_records):
            a.setItem(row_index, 0, QTableWidgetItem(patient_id))
            a.setItem(row_index, 1, QTableWidgetItem(patient_name))
            a.setItem(row_index, 2, QTableWidgetItem(medical_condition))
            a.setItem(row_index, 3, QTableWidgetItem(doctor_name))

    def refresh_patient_records(self):
        self._refresh_patient(self.managepatientsrecords_tabrecords_view,'Y')
        self._refresh_patient(self.managepatientsrecords_tabdelete_view)
        self._refresh_patient(self.managepatientsrecords_tabrecords_view_past,'N')
        self.set_up_dashboard()

    def _search_patient(self, table_widget, condition=None, search_text=None):
        """
        Searches for patients based on user input in patient ID or name and displays
        the results in the specified table widget.
        """
        if not search_text:
            self.refresh_patient_records()
            return

        search_text = search_text.lower()
        if condition is None:
            query = f'''
                SELECT p.patient_id, p.name, p.medical_condition, d.name AS doctor_name
                FROM patient p
                LEFT JOIN appointment a ON p.patient_id = a.patient_id
                LEFT JOIN doctor d ON a.doctor_id = d.doctor_id
                WHERE (LOWER(p.name) LIKE '%' || '{search_text}' || '%' 
                    OR LOWER(p.patient_id) LIKE '%' || '{search_text}' || '%'
                    OR LOWER(p.medical_condition) LIKE '%' || '{search_text}' || '%')
            '''
        else:
            query = f'''
                SELECT p.patient_id, p.name, p.medical_condition, d.name AS doctor_name
                FROM patient p
                LEFT JOIN appointment a ON p.patient_id = a.patient_id
                LEFT JOIN doctor d ON a.doctor_id = d.doctor_id
                WHERE (LOWER(p.name) LIKE '%' || '{search_text}' || '%' 
                    OR LOWER(p.patient_id) LIKE '%' || '{search_text}' || '%'
                    OR LOWER(p.medical_condition) LIKE '%' || '{search_text}' || '%')
                    AND p.status = '{condition}'
            '''
        
        select_command = SelectCommand(query)
        patient_records = select_command.execute(self.db_manager)

        table_widget.setColumnCount(0)
        table_widget.setColumnCount(4)
        table_widget.setHorizontalHeaderLabels(["ID", "Patient Name", "Medical Condition", "Allotted Doctor"]) 
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Display the results in the specified table widget
        table_widget.setRowCount(len(patient_records))
        for row_index, (id, name, medical_condition, doctor_name) in enumerate(patient_records):
            table_widget.setItem(row_index, 0, QTableWidgetItem(id))
            table_widget.setItem(row_index, 1, QTableWidgetItem(name))
            table_widget.setItem(row_index, 2, QTableWidgetItem(medical_condition))
            table_widget.setItem(row_index, 3, QTableWidgetItem(doctor_name))


    def search_patient_t1(self):
        text = self.managepatientsrecords_tabrecords_search.text()
        self._search_patient(self.managepatientsrecords_tabrecords_view, 'Y', text)

    def search_patient_t2(self):
        text = self.managepatientsrecords_tabrecords_searchpast.text()
        self._search_patient(self.managepatientsrecords_tabrecords_viewpast, 'N', text)

    def search_patient_t3(self):
        text = self.managepatientsrecords_tabdelete_search.text()
        self._search_patient(self.managepatientsrecords_tabdelete_view, None, text)

    def _search_appointment(self, table_widget, condition, search_text=None):
        """
        Searches for appointments based on user input in appointment ID, patient name, 
        or doctor name, and displays the results in the specified table widget.
        """
        if not search_text:
            self.refresh_appointment_records()
            return
        
        search_text = search_text.lower()  # Convert input to lowercase for case-insensitive search
        
        query = f'''
            SELECT a.appointment_id, p.patient_id, p.name AS patient_name, 
                d.doctor_id, d.name AS doctor_name, a.appointment_date
            FROM appointment a
            INNER JOIN patient p ON a.patient_id = p.patient_id
            INNER JOIN doctor d ON a.doctor_id = d.doctor_id
            WHERE (LOWER(a.appointment_id) LIKE '%' || '{search_text}' || '%' 
                OR LOWER(p.name) LIKE '%' || '{search_text}' || '%' 
                OR LOWER(d.name) LIKE '%' || '{search_text}' || '%')
                AND a.status = '{condition}' -- Filter for active appointments
        '''
        
        select_command = SelectCommand(query)
        appointment_records = select_command.execute(self.db_manager)

        table_widget.setColumnCount(0)
        table_widget.setColumnCount(6)
        table_widget.setHorizontalHeaderLabels(["Appointment ID", "Patient ID", "Patient Name", "Doctor ID", "Doctor Name", "Appointment Date"]) 
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Display the results in the specified table widget
        table_widget.setRowCount(len(appointment_records))
        for row_index, (appointment_id, patient_id, patient_name, doctor_id, doctor_name, appointment_date) in enumerate(appointment_records):
            table_widget.setItem(row_index, 0, QTableWidgetItem(appointment_id))
            table_widget.setItem(row_index, 1, QTableWidgetItem(patient_id))
            table_widget.setItem(row_index, 2, QTableWidgetItem(patient_name))
            table_widget.setItem(row_index, 3, QTableWidgetItem(doctor_id))
            table_widget.setItem(row_index, 4, QTableWidgetItem(doctor_name))

    def search_appointment_cancel(self):
        text = self.bookappointment_tabcancel_search.text()
        self._search_appointment(self.bookappointment_tabcancel_view, 'Y', text)
    
    def search_appointment_completed(self):
        text = self.bookappointment_tabcompleted_search.text()
        self._search_appointment(self.bookappointment_tabcompleted_view, 'N', text)
    
    def _refresh_appointments(self, table_widget, condition):
        query = f'''
            SELECT a.appointment_id, p.patient_id, p.name AS patient_name, 
                d.doctor_id, p.medical_condition, a.appointment_date
            FROM appointment a
            INNER JOIN patient p ON a.patient_id = p.patient_id
            INNER JOIN doctor d ON a.doctor_id = d.doctor_id
            WHERE a.status = '{condition}'
        '''
        
        select_command = SelectCommand(query)
        appointment_records = select_command.execute(self.db_manager)

        table_widget.setColumnCount(0)
        table_widget.setColumnCount(6)
        table_widget.setHorizontalHeaderLabels(["Appointment ID", "Patient ID", "Patient Name", "Doctor ID", "Medical Condition", "Appointment Date"]) 
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Display the results in the specified table widget
        table_widget.setRowCount(len(appointment_records))
        for row_index, (appointment_id, patient_id, patient_name, doctor_id, medical_condition, appointment_date) in enumerate(appointment_records):
            table_widget.setItem(row_index, 0, QTableWidgetItem(appointment_id))
            table_widget.setItem(row_index, 1, QTableWidgetItem(patient_id))
            table_widget.setItem(row_index, 2, QTableWidgetItem(patient_name))
            table_widget.setItem(row_index, 3, QTableWidgetItem(doctor_id))
            table_widget.setItem(row_index, 4, QTableWidgetItem(medical_condition))
            table_widget.setItem(row_index, 5, QTableWidgetItem(str(appointment_date)))

    def refresh_appointment_records(self):
        self._refresh_appointments(self.bookappointment_tabcancel_view, 'Y')
        self._refresh_appointments(self.bookappointment_tabcompleted_view, 'N')
        self.set_up_dashboard()

    def refresh_billing_records(self):
        self._refresh_appointments(self.billing_search_display, 'Y')

    def search_billing(self):
        self._search_patient(self.billing_search_display, self.billing_search.text())

    def delete_patient_and_appointment(self, table_widget):
        table_name = 'patient'
        selected_row = table_widget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row to delete.",
                                QMessageBox.Ok)
            if QMessageBox.Ok:
                return
            return
        if table_widget == self.managepatientsrecords_tabdelete_view:
            record_id = table_widget.item(selected_row, 0).text()
        elif table_widget == self.bookappointment_tabcancel_view:
            record_id = table_widget.item(selected_row, 1).text()
        reply = QMessageBox.question(self, "Confirm Deletion",
                                     f"Are you sure you want to delete record with ID {record_id}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return
    
        alter_doctor_command = f'''
            update doctor set status = 'A'
            where doctor_id in (
            select doctor_id
            from appointment 
            where patient_id = '{record_id}' and status = 'Y'
            )
        '''
        alter_doctor = UpdateCommand(alter_doctor_command)
        mail_sending_details_command = f'''
        SELECT 
            pc.CONTACT AS email,
            p.NAME AS name,
            p.PATIENT_ID AS patient_id,
            a.APPOINTMENT_ID AS appointment_id
        FROM 
            PATIENT p
        JOIN 
            PATIENT_CONTACT pc ON p.PATIENT_ID = pc.PATIENT_ID
        JOIN 
            APPOINTMENT a ON p.PATIENT_ID = a.PATIENT_ID
        WHERE 
            pc.CONTACT LIKE '%@%' and 
            p.PATIENT_ID = '{record_id}'
        '''
        mail_sending_details = SelectCommand(mail_sending_details_command)
        mail_details = mail_sending_details.execute(self.db_manager)
        alter_doctor.execute(self.db_manager)

        delete_command = f'''
        DELETE FROM {table_name} WHERE patient_id = '{record_id}'
        '''
        delete_command = DeleteCommand(delete_command)
        delete_command.execute(self.db_manager)

        self.refresh_all_tables()

        print(mail_details)
        if mail_details:
            for email, name, patient_id, appointment_id in mail_details:
                send_mail.SendCancellation(email, name, patient_id, appointment_id)
                
        QMessageBox.information(self, "Success", "Record deleted successfully.")

    def delete_patient(self):
        self.delete_patient_and_appointment(self.managepatientsrecords_tabdelete_view)
        
    def delete_appointment(self):
        self.delete_patient_and_appointment(self.bookappointment_tabcancel_view)

    def delete_doctor(self):
        pass

    def refresh_all_tables(self):
        self.refresh_patient_records()
        self.refresh_doctor_records()
        self.refresh_appointment_records()
        self.refresh_billing_records()
        self.set_up_dashboard()

    def get_data(self):
        table_widget = self.billing_search_display
        selected_row = table_widget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row.",
                                QMessageBox.Ok)
            if QMessageBox.Ok:
                return
            return
        record_id = table_widget.item(selected_row, 0).text()

        select_no_of_days_command = f'''
        SELECT GET_APPOINTMENT_DAYS('{record_id}') AS DAYS_FROM_APPOINTMENT FROM DUAL
        '''
        select_no_of_days = SelectCommand(select_no_of_days_command)
        no_of_days = select_no_of_days.execute(self.db_manager)
        no_of_days = no_of_days[0][0]

        medical_condition = table_widget.item(selected_row, 4).text()
        select_price = f'''
        SELECT COST FROM MEDICAL_PROBLEMS WHERE PROBLEM_NAME = '{medical_condition}'
        '''
        select_price = SelectCommand(select_price)
        price = select_price.execute(self.db_manager)
        try:
            price = int(price[0][0])
        except:
            QMessageBox.warning(self, "Warning", "SOME TECHNICAL ERROR OCCURED.",
                                QMessageBox.Ok)
            if QMessageBox.Ok:
                return
            return

        self.billing_days.setText(str(no_of_days)+" days" if no_of_days > 1 else str(no_of_days)+" day")
        self.billing_costperday.setText("₹ "+str(price))
        total = int(no_of_days) * int(price)
        self.billing_totalcost.setText("₹ "+str(total)+" only")
        return total
        
    def make_payment(self):
        cost = self.get_data()  # Retrieve the cost or data for the payment
        payment_dialog = PaymentQRWidget(cost)
        result = payment_dialog.exec()  # Show dialog as modal

        # Retrieve the payment status after the dialog closes
        payment_status = payment_dialog.get_payment_status()
        
        if payment_status:
            self._payment_completed(str(cost))
            QMessageBox.information(self, "Payment Status", "Payment was successful!")
        else:
            QMessageBox.information(self, "Payment Status", "Payment was canceled.")
            # Handle canceled payment if needed

    def _payment_completed(self, amount):
        table_widget = self.billing_search_display
        selected_row = table_widget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a row.",
                                QMessageBox.Ok)
            if QMessageBox.Ok:
                return
            return
        appointment_id = table_widget.item(selected_row, 0).text()
        patient_id = table_widget.item(selected_row, 1).text()
        doctor_id = table_widget.item(selected_row,3).text()
        alter_appointment = UpdateCommand(f"UPDATE APPOINTMENT SET STATUS = 'N' WHERE APPOINTMENT_ID = '{appointment_id}'")
        alter_appointment.execute(self.db_manager)
        alter_patient = UpdateCommand(f"UPDATE PATIENT SET STATUS = 'N' WHERE PATIENT_ID = '{patient_id}'")
        alter_patient.execute(self.db_manager)
        alter_doctor = UpdateCommand(f"UPDATE DOCTOR SET STATUS = 'A' WHERE DOCTOR_ID = '{doctor_id}'")
        alter_doctor.execute(self.db_manager)

        # extradetails for mail send
        patient_email_command = SelectCommand(f"select contact from patient_contact where patient_id ='{patient_id}'")
        email = patient_email_command.execute(self.db_manager)
        email = email[0][0]
        name_command = SelectCommand(f"select name from patient where patient_id ='{patient_id}'")
        name = name_command.execute(self.db_manager)
        name = name[0][0]
        send_mail.SendPaymentConfirmation(email,name,patient_id,appointment_id,amount)
        self.refresh_all_tables()


class PaymentQRWidget(QDialog):  # Using QDialog for modal behavior and result
    def __init__(self, payment_data):
        super().__init__()
        self.payment_data = payment_data
        self.payment_status = False  # Initialize payment status as False
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Payment QR Code")
        self.setFixedSize(400, 450)  # Adjust size to fit buttons as well
        
        # Generate QR code
        qr_img = self.generate_qr(self.payment_data)
        
        # Display QR code in the GUI
        qr_label = QLabel()
        pixmap = QPixmap.fromImage(qr_img)
        qr_label.setPixmap(pixmap)
        qr_label.setAlignment(Qt.AlignCenter)
        
        # "Paid" button
        paid_button = QPushButton("Paid")
        paid_button.clicked.connect(self.mark_as_paid)
        
        # "Cancel Payment" button
        cancel_button = QPushButton("Cancel Payment")
        cancel_button.clicked.connect(self.cancel_payment)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(qr_label)
        layout.addWidget(paid_button)
        layout.addWidget(cancel_button)
        self.setLayout(layout)
    
    def generate_qr(self, data):
        # Create the QR code with the payment data
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=12,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Convert QR code to QImage
        img = qr.make_image(fill="black", back_color="white")
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        q_image = QImage.fromData(buffer.getvalue())
        
        return q_image
    
    def mark_as_paid(self):
        """Set payment status to True and close dialog."""
        self.payment_status = True
        self.accept()  # Closes the dialog with an "accepted" status

    def cancel_payment(self):
        """Set payment status to False and close dialog."""
        self.payment_status = False
        self.reject()  # Closes the dialog with a "rejected" status
    
    def get_payment_status(self):
        """Return the payment status after the dialog is closed."""
        return self.payment_status


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HMSApp()
    main_window.show()
    sys.exit(app.exec())