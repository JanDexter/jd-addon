# Hotel Management Module

This is a custom Odoo module for managing hotel operations. It includes features for managing room types, charges, and other hotel-related data.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Models](#models)
- [Views](#views)
- [Security](#security)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Version Information](#version-information)

## Features

- **Room Types**: Define various room types with details such as daily charges, extra charges, discounts, room capacity, and images.
- **Charges**: Manage charges for rooms and additional services.
- **Guests**: Track guest information and their stays.
- **Booking Management**: Handle room bookings, check-ins, and check-outs.
- **Reports**: Generate reports on occupancy rates and revenue.

## Installation

1. Copy the `hotel` module folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Navigate to the Apps menu in Odoo.
4. Update the app list and install the `Hotel Management` module.

## Configuration

After installation, you can configure the module:
1. Go to **Settings** > **Hotel Management Settings**
2. Configure default values for room charges, check-in/check-out times
3. Set up email templates for booking confirmations and reminders

## Models

### Room Types (`hotel.roomtypes`)
- Fields:
  - `name`: Name of the room type.
  - `description`: Description of the room type.
  - `daily_charge`: Daily charge for the room.
  - `extra_charge`: Additional charges for the room.
  - `discount`: Discount percentage.
  - `total_charge`: Computed total charge after applying the discount.
  - `room_type`: Type of the room (e.g., Single, Double, Suite).
  - `room_capacity`: Maximum capacity of the room.
  - `room_size`: Size of the room in square meters.
  - `room_bed_type`: Type of bed in the room.
  - `room_bed_count`: Number of beds in the room.
  - `room_image`: Image of the room.
  - `bathroom_image`: Image of the bathroom.

### Bookings (`hotel.booking`)
- Fields:
  - `guest_id`: Link to the guest record
  - `room_id`: Link to the room record
  - `check_in_date`: Date of check-in
  - `check_out_date`: Date of check-out
  - `status`: Status of the booking (confirmed, checked-in, checked-out, cancelled)
  - `total_amount`: Total amount for the stay

## Views

- **List View**: Displays a list of room types with basic details.
- **Form View**: Allows detailed editing of room type information, including charges and images.
- **Calendar View**: Shows bookings in a calendar format.
- **Kanban View**: Visual representation of room status.
- **Dashboard**: Overview of hotel occupancy and revenue metrics.

## Security

Access control is defined in `security/ir.model.access.csv` to restrict access to authorized users.
Different user roles include:
- Hotel Manager: Full access to all features
- Front Desk Staff: Access to bookings and guest information
- Housekeeping: Limited access to room status information

## Usage

1. **Setting Up Room Types**:
   - Navigate to the **Room Types** menu under the **Hotel Master Lists** section.
   - Add or edit room types with detailed information.
   - Upload images of rooms and bathrooms for better presentation.

2. **Managing Bookings**:
   - Go to the **Bookings** menu to create new bookings.
   - Select a guest and room, enter check-in and check-out dates.
   - Confirm the booking, which will automatically calculate charges.

3. **Guest Check-in/Check-out**:
   - Process guest check-ins and check-outs from the **Front Desk** dashboard.
   - Print guest folios and receipts directly from the system.

4. **Reporting**:
   - Access the **Reports** section to view occupancy rates, revenue statistics, and other KPIs.
   - Export reports in various formats (PDF, Excel, CSV).

## Troubleshooting

- **Issue**: Module doesn't appear in the Apps list
  **Solution**: Check that the module folder is correctly placed and has the proper structure

- **Issue**: Images don't display correctly
  **Solution**: Verify file formats are supported (JPG, PNG) and size limits are respected

- **Issue**: Calculation errors in charges
  **Solution**: Verify discount settings and check for rounding configuration

## Version Information

- Version: 1.0.0
- Compatible with Odoo 16.0
- Last Updated: 2023-09-01
- License: LGPL-3
