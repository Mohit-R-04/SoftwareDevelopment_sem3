-- Creating the Patient table
CREATE TABLE PATIENT (
    PATIENT_ID VARCHAR2(30) PRIMARY KEY,
    NAME VARCHAR2(100) NOT NULL,
    DOB DATE NOT NULL,
    GENDER VARCHAR2(10) NOT NULL,
    MEDICAL_CONDITION VARCHAR2(255)
);

ALTER TABLE PATIENT
    ADD STATUS VARCHAR2(
        20
    ) CHECK (
        STATUS IN ('Y', 'N')
    );

-- Y = Active, N = appointment completed

-- Creating the Patient_contact table with ON DELETE CASCADE
CREATE TABLE PATIENT_CONTACT (
    PATIENT_ID VARCHAR2(30),
    CONTACT VARCHAR2(50),
    PRIMARY KEY (PATIENT_ID, CONTACT),
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID) ON DELETE CASCADE
);

-- Creating the Patient_address table with ON DELETE CASCADE
CREATE TABLE PATIENT_ADDRESS (
    PATIENT_ID VARCHAR2(30) PRIMARY KEY,
    HOUSE_NO VARCHAR2(50),
    CITY VARCHAR2(50),
    STATE VARCHAR2(50),
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID) ON DELETE CASCADE
);

-- Creating the Doctor table
CREATE TABLE DOCTOR (
    DOCTOR_ID VARCHAR2(30) PRIMARY KEY,
    NAME VARCHAR2(100) NOT NULL,
    SPECIALIZATION VARCHAR2(100) NOT NULL,
    STATUS VARCHAR2(20) NOT NULL
);

-- Adding a check constraint on the STATUS column in the Doctor table
ALTER TABLE DOCTOR
    ADD CONSTRAINT CHK_STATUS CHECK (
        STATUS IN ('A', 'NA', 'W')
    );

-- Creating the Doctor_contact table with ON DELETE CASCADE
CREATE TABLE DOCTOR_CONTACT (
    DOCTOR_ID VARCHAR2(30),
    CONTACT VARCHAR2(50),
    PRIMARY KEY (DOCTOR_ID, CONTACT),
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(DOCTOR_ID) ON DELETE CASCADE
);

-- Creating the Doctor_address table with ON DELETE CASCADE
CREATE TABLE DOCTOR_ADDRESS (
    DOCTOR_ID VARCHAR2(30) PRIMARY KEY,
    HOUSE_NO VARCHAR2(50),
    CITY VARCHAR2(50),
    STATE VARCHAR2(50),
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(DOCTOR_ID) ON DELETE CASCADE
);

-- Creating the Appointment table with ON DELETE CASCADE on patient and doctor IDs
CREATE TABLE APPOINTMENT (
    APPOINTMENT_ID VARCHAR2(30) PRIMARY KEY,
    PATIENT_ID VARCHAR2(30) NOT NULL,
    DOCTOR_ID VARCHAR2(30) NOT NULL,
    APPOINTMENT_DATE DATE NOT NULL,
    STATUS CHAR(1) CHECK (STATUS IN ('Y', 'N')), -- Y = Active, N = Inactive
    FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT(PATIENT_ID) ON DELETE CASCADE,
    FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR(DOCTOR_ID) ON DELETE CASCADE
);

--============================================
-- auto increment all table's primary key
--============================================

-- Creating a sequence for Patient table
CREATE SEQUENCE PATIENT_SEQ START WITH 1 INCREMENT BY 1;

-- Creating a trigger for Patient table
CREATE OR REPLACE TRIGGER TRG_PATIENT_ID BEFORE
    INSERT ON PATIENT FOR EACH ROW
BEGIN
    SELECT
        'P'
        || PATIENT_SEQ.NEXTVAL INTO :NEW.PATIENT_ID
    FROM
        DUAL;
END;
/

-- Creating a sequence for Doctor table
CREATE SEQUENCE DOCTOR_SEQ START WITH 1 INCREMENT BY 1;

-- Creating a trigger for Doctor table
CREATE OR REPLACE TRIGGER TRG_DOCTOR_ID BEFORE
    INSERT ON DOCTOR FOR EACH ROW
BEGIN
    SELECT
        'D'
        || DOCTOR_SEQ.NEXTVAL INTO :NEW.DOCTOR_ID
    FROM
        DUAL;
END;
/

--DROP SEQUENCE DOCTOR_SEQ;
--DROP TRIGGER TRG_DOCTOR_ID;

-- Creating a sequence for Appointment table
CREATE SEQUENCE APPOINTMENT_SEQ START WITH 1 INCREMENT BY 1;

-- Creating a trigger for Appointment table
CREATE OR REPLACE TRIGGER TRG_APPOINTMENT_ID BEFORE
    INSERT ON APPOINTMENT FOR EACH ROW
BEGIN
    SELECT
        'A'
        || APPOINTMENT_SEQ.NEXTVAL INTO :NEW.APPOINTMENT_ID
    FROM
        DUAL;
END;
/

--============================================
-- Functions
--===========================================

CREATE OR REPLACE FUNCTION GET_APPOINTMENT_DAYS(
    P_APPOINTMENT_ID VARCHAR2
) RETURN NUMBER IS
    DAYS_DIFFERENCE NUMBER;
BEGIN
 
    -- Fetch the difference in days
    SELECT
        TRUNC(SYSDATE - APPOINTMENT_DATE) INTO DAYS_DIFFERENCE
    FROM
        APPOINTMENT
    WHERE
        APPOINTMENT_ID = P_APPOINTMENT_ID;
    RETURN DAYS_DIFFERENCE + 1;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
 
        -- Handle the case where no appointment is found
        RETURN NULL; -- Or some other meaningful default value
    WHEN TOO_MANY_ROWS THEN
 
        -- Handle the case where multiple appointments are found (unexpected)
        RAISE_APPLICATION_ERROR(-20001, 'Multiple appointments found with the same ID');
END GET_APPOINTMENT_DAYS;
/