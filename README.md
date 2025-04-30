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

## Installation

1. Copy the `hotel` module folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Navigate to the Apps menu in Odoo.
4. Update the app list and install the `Hotel Management` module.

## Configuration

After installation, you can configure the module:
1. Go to **Settings** > **Hotel Management Settings**
2. Configure default values for room charges, check-in/check-out times

## Models

### Rooms (`hotel.rooms`)
- Fields:
  - `name`: Room number (required).
  - `description`: Room description.
  - `roomtype_id`: Room type (many2one to `hotel.roomtypes`, required).
  - `roomtypename`: Room type name (related, readonly).

### Room Types (`hotel.roomtypes`)
- Fields:
  - `name`: Room type name (required).
  - `description`: Room type description.
  - `photobed`: Bed photo.
  - `photorestroom`: Comfort room photo.
  - `room_image`: Room image.
  - `bathroom_image`: Bathroom image.
  - `daily_charge`: Daily charge.
  - `extra_charge`: Extra charge.
  - `discount`: Discount (%).
  - `total_charge`: Computed total charge after discount.
  - `room_capacity`: Room capacity.
  - `room_size`: Room size (sqm).
  - `room_bed_type`: Bed type (single, double, queen, king).
  - `room_bed_count`: Number of beds.
  - `charge_history_ids`: One2many to charge history.
  - `current_historical_charge`: Computed current charge from history.
  - `roomtypes_list`: Computed list of all room types.
- Main Functions:
  - `_compute_roomtypes_list`: Computes all room types.
  - `_compute_current_charge`: Computes the current historical charge.
  - `_compute_total_charge`: Computes the total charge.

### Room Type Charge History (`hotel.roomtype.charge.history`)
- Fields:
  - `roomtype_id`: Room type (many2one, required).
  - `date_from`: Valid from date (required).
  - `date_to`: Valid to date.
  - `charge_amount`: Charge amount (required).
  - `is_current`: Computed boolean if this is the current charge.
- Main Functions:
  - `_compute_is_current`: Computes if the charge is current.

### Daily Charges (`hotel.dailycharges`)
- Fields:
  - `charge_id`: Charge title (many2one to `hotel.charges`).
  - `amount`: Daily amount.
  - `roomtype_id`: Room type (many2one).

### Charges (`hotel.charges`)
- Fields:
  - `name`: Charge name.
  - `description`: Charge description.

### Guests (`hotel.guest`)
- Fields:
  - `name`: Computed full name (Lastname, Firstname Middlename).
  - `lastname`: Last name (required).
  - `firstname`: First name (required).
  - `middlename`: Middle name.
  - `address_streetno`: Address / Street & No.
  - `address_area`: Area, Unit & Bldg, Brgy.
  - `address_city`: City / Town.
  - `address_province`: Province / State.
  - `zipcode`: ZIP Code.
  - `contactno`: Contact number.
  - `email`: Email.
  - `gender`: Gender (Female/Male).
  - `birthdate`: Birthday.
  - `photo`: Guest photo.
  - `age`: Computed age.
- Main Functions:
  - `_compute_name`: Builds the `name` from lastname, firstname, middlename.
  - `_compute_age`: Computes the `age` from `birthdate`.

### Guest Registration (`hotel.guestregistration`)
- Fields:
  - `room_id`: Room (many2one to `hotel.rooms`).
  - `guest_id`: Guest (many2one to `hotel.guests`).
  - `roomname`: Room number (related).
  - `roomtname`: Room type (related).
  - `guestname`: Guest name (related).
  - `datecreated`: Date created (default today).
  - `datefromSched`: Scheduled check-in.
  - `datetoSched`: Scheduled check-out.
  - `datefromAct`: Actual check-in.
  - `datetoAct`: Actual check-out.
  - `name`: Computed registration name (room, guest).
- Main Functions:
  - `_compute_name`: Concatenates room and guest name.

## Views

The module includes the following views defined in the views folder:

- **Room Types Views**:
  - List View (`hotel_roomtypes_list.xml`): Displays a list of room types with basic details.
  - Form View (`hotel_roomtypes_form.xml`): Allows detailed editing of room type information, including charges and images.

Additional views may be available based on the specific implementation in the views folder.

## Security

Access control is defined in `security/ir.model.access.csv` to restrict access to authorized users.
Security rules are set up to control access based on user roles and permissions.

## Usage

1. **Setting Up Room Types**:
   - Navigate to the **Room Types** menu under the **Hotel Master Lists** section.
   - Add or edit room types with detailed information.
   - Upload images of rooms and bathrooms for better presentation.

2. **Managing Hotel Operations**:
   - Use the features provided by the installed module to manage your hotel operations.
   - Refer to specific menu items created by the module for various management tasks.

## Troubleshooting

- **Issue**: Module doesn't appear in the Apps list
  **Solution**: Check that the module folder is correctly placed and has the proper structure

- **Issue**: Images don't display correctly
  **Solution**: Verify file formats are supported (JPG, PNG) and size limits are respected

- **Issue**: Calculation errors in charges
  **Solution**: Verify discount settings and check for rounding configuration

## Version Information

- Version: 11.0.0
- Compatible with Odoo 18.0
- Last Updated: 2025-04-30
- License: LGPL-3

## Developer Notes

To extend this module with additional models:
1. Add new model files to the `models` folder
2. Register them in `models/__init__.py`
3. Create corresponding views in the `views` folder
4. Update the `__manifest__.py` file to include the new models and views
5. Update this documentation to reflect the new features
6. If you encounter any issue, create a new issue in the repository. You can also directly contact me.
7. If you see any inaccuracies in this readme, just contact me.
