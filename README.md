# Blood-Chain
This is a hackathon site. SDG 3

BloodChain is a Django-based web platform designed to support blood donation awareness, simplify donor interaction, and provide users with accessible information about blood availability, donation centers, and healthcare-related updates.

The project focuses on combining modern web technologies with social impact by creating a digital ecosystem where users can track donations, monitor blood inventory, read important news, and locate donation centers.

## Project Overview

BloodChain was created to make blood donation more transparent, organized, and accessible. It allows users to create accounts, manage personal profiles, participate in donation activities, and stay informed about blood supply levels and healthcare news.

The platform is designed not only as an informational website but also as a functional system that can help encourage real-world donor participation.

## Main Features

admin email: admin@gmail.com
admin password: admin
### User Management
- User registration and authentication
- Personal profile system
- Profile image upload
- Account settings
- Terms & Conditions agreement
- Donation count tracking
- Donor rank system based on activity

### Donation System
- Donation history tracking
- Automatic recording of user donations
- Recent donation display
- Personal donation statistics
- Blood inventory updates based on donations

### Blood Inventory Monitoring
The system tracks all major blood groups:
- O+
- O-
- A+
- A-
- B+
- B-
- AB+
- AB-

Each blood type includes availability indicators such as:
- Critical
- Stable
- Full

### News Management
- Admin-controlled news publishing
- Rich text article support with CKEditor
- Image uploads for articles
- Homepage news feed

### Donation Center Map
- Blood donation center database
- Address geolocation using OpenStreetMap (Nominatim API)
- Latitude and longitude storage
- Interactive map integration

### Multilingual Support
The platform supports multiple languages for broader accessibility.

## Technologies Used

### Backend
- Python 3
- Django
- SQLite3

### Frontend
- HTML5
- CSS3
- JavaScript

### Additional Tools
- CKEditor
- CKEditor Uploader
- Django Resized
- OpenStreetMap API

## Project Structure

```bash
BloodChain/
│
├── BloodChain/
├── Users/
├── Donations/
├── media/
├── static/
├── db.sqlite3
└── manage.py
