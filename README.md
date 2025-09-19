# Printer Management Web Application

This is a simple printer management system that allows you to view all the printers on-site. You can view the brand, model, location, IP address, MAC address, manufacture date, and comments for each printer. You can also add a new printer, edit an existing printer, or delete a printer if you have the correct access.

## Live Website

**Accessible here**: [https://printers-sea-web-app.vercel.app/](https://printers-sea-web-app.vercel.app/)

## Usage

### User Registration & Authentication

1. **Register New Account**
   - Visit the application homepage and click register
   - Fill out username and password (must meet displayed security requirements)
   - Automatic login after successful registration

2. **Login Process**
   - Enter username and password
   - Redirected to printer management dashboard
   - Username displayed in navigation bar

3. **Logout**
   - Click "Log off" in the navigation bar
   - Session terminated and redirected to login page

## Features

### Core Functionality
- **Secure Authentication**: User registration, login, and session management
- **Role-Based Access Control**: Different permission levels for regular users and administrators
- **Printer Management**: Complete CRUD operations for printer inventory
- **Inventory Overview**: Comprehensive listing of all printers with detailed information
- **Data Validation**: Robust validation for IP addresses, MAC addresses, and dates
- **User Feedback**: Real-time success and error messaging

### User Roles & Permissions
- **Regular Users**: Can view, add, and update printer records
- **Administrators**: Full access including delete operations and user management
- **Automatic Role Assignment**: New users automatically assigned to RegularUser group

### Security Features
- **CSRF Protection**: Cross-Site Request Forgery protection on all forms
- **Input Validation**: Server-side validation for all user inputs
- **Session Management**: Secure login/logout with proper session handling
- **Permission Enforcement**: View-level permission checking

### Printer Management

#### Adding Printers
1. Click the **"+"** (Add) button in the printer list
2. Fill out the modal form with printer details:
   - **Brand**: Printer manufacturer (required)
   - **Model**: Printer model (required)  
   - **Location**: Physical location (required)
   - **IP Address**: Network IP address (validated)
   - **MAC Address**: Hardware MAC address (required)
   - **Manufacture Date**: Date in various formats (validated)
   - **Comments**: Additional notes (optional)
3. Click "Save changes" to add the printer

#### Editing Printers
1. Click the **pencil** (Edit) icon for any printer
2. Modify fields in the pre-populated modal
3. Click "Save changes" to update

#### Deleting Printers (Admin Only)
1. Click the **trash** (Delete) icon for any printer
2. Confirm deletion in the confirmation modal
3. Printer permanently removed from database

### Data Validation

The application automatically validates:
- **IP Addresses**: Must be valid IPv4 or IPv6 format
- **Dates**: Accepts multiple formats (YYYY-MM-DD, MM/DD/YYYY, DD-MM-YYYY)
- **Required Fields**: All fields except comments must be filled
- **MAC Addresses**: Standard MAC address format validation

## Technology Stack

### Backend
- **Framework**: Django 4.1.3
- **Language**: Python 3.12.6
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: Django's built-in authentication system

### Frontend
- **UI Framework**: Bootstrap 4.6
- **Icons**: Font Awesome 6.6.0
- **JavaScript**: jQuery with Bootstrap modals
- **Responsive Design**: Mobile-first approach

### Deployment & Infrastructure
- **Hosting**: Vercel
- **Static Files**: WhiteNoise for static file serving
- **Environment**: Python-decouple for configuration management
