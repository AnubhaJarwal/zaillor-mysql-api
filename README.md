# Lead Storage Migration & API Modernization (Proof of Concept)

## Overview

This project demonstrates the migration of a lead management workflow from Google Sheets to a MySQL-based architecture.

The original system stored lead information inside Google Sheets using Google Apps Script. While functional, this approach has limitations in scalability, data management, querying, reporting, and long-term maintainability.

The objective of this project was to validate whether the existing workflow could be migrated to a relational database architecture while preserving the lead collection process.

---

## Existing Architecture

Website → Google Apps Script → Google Sheets

Lead information included:

* Lead ID
* Website URL
* Email Address
* Phone Number
* Audit Score
* Lead Status
* Timestamp

---

## Proposed Architecture

Website → Flask API → MySQL Database

This architecture provides:

* Structured data storage
* Improved scalability
* Better data integrity
* Easier querying and reporting
* Future integration with dashboards and analytics tools

---

## Project Objectives

* Replace Google Sheets with a structured relational database.
* Store lead information in MySQL.
* Create an API layer for database operations.
* Validate end-to-end data flow.
* Evaluate cloud deployment feasibility.

---

## Phase 1: Database Design

A MySQL database was created to store lead information.

### Database

`zaillor_db`

### Table

`leads`

### Stored Fields

* id
* lead_id
* website_url
* email
* phone
* created_at
* overall_score
* lead_status

The schema was designed to replicate and improve the structure previously stored in Google Sheets.

---

## Phase 2: Data Migration

Existing lead records were exported from Google Sheets and imported into MySQL.

Migration workflow:

Google Sheets → CSV Export → MySQL Import

Validation was performed to verify:

* Record count accuracy
* Correct column mapping
* Data consistency after import

---

## Phase 3: API Development

A Flask REST API was developed to act as a bridge between applications and the MySQL database.

### Endpoint

`POST /saveLead`

### Responsibilities

* Accept lead data
* Process incoming requests
* Connect to MySQL
* Insert records into the database
* Return success responses

---

## Phase 4: Database Connectivity

The API was connected to MySQL using:

* Python
* Flask
* mysql-connector-python

Successful tests verified:

* Database connectivity
* Record insertion
* Data persistence
* Response handling

---

## Phase 5: Testing

A dedicated testing script was created to validate the API workflow.

Testing flow:

Test Script → Flask API → MySQL Database

Results:

* API received requests successfully
* Database connection established
* Records inserted correctly
* Data verified within MySQL

---

## Phase 6: Cloud Deployment

The Flask API was deployed using Render.

Deployment workflow:

GitHub → Render → Public API Endpoint

Tasks completed:

* Repository creation
* Git version control
* Dependency management
* Deployment configuration
* Automatic deployment through GitHub integration
* Public endpoint verification

---

## Technologies Used

### Backend

* Python
* Flask

### Database

* MySQL

### Deployment

* Render

### Version Control

* Git
* GitHub

### Data Migration

* CSV Export / Import

---

## Results

Successfully demonstrated:

* Migration from spreadsheet-based lead storage to MySQL
* API-driven database operations
* Cloud deployment of backend services
* Database integration testing
* End-to-end proof-of-concept validation

---

## Current Status

### Completed

* Database creation
* Data migration
* API development
* API testing
* Cloud deployment
* Database validation

### Pending

* Production cloud database setup
* Live website integration
* Production environment configuration
* End-to-end production deployment

---

## Learning Outcomes

This project provided hands-on experience with:

* Database design
* Data migration
* REST API development
* Backend engineering
* Cloud deployment
* Git and GitHub workflows
* MySQL integration
* System architecture design

---

## Author

**Anubha Jarwal**

B.Tech Computer Science Engineering (Data Science)
