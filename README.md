# Hotel Management Module

This is a custom Odoo module for managing hotel operations. It includes features for managing room types, charges, and other hotel-related data.

## Features

- **Room Types**: Define various room types with details such as daily charges, extra charges, discounts, room capacity, and images.
- **Charges**: Manage charges for rooms and additional services.
- **Guests**: Track guest information and their stays.

## Installation

1. Copy the `hotel` module folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Navigate to the Apps menu in Odoo.
4. Update the app list and install the `Hotel Management` module.

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

## Views

- **List View**: Displays a list of room types with basic details.
- **Form View**: Allows detailed editing of room type information, including charges and images.

## Security

Access control is defined in `security/ir.model.access.csv` to restrict access to authorized users.

## Usage

1. Navigate to the **Room Types** menu under the **Hotel Master Lists** section.
2. Add or edit room types with detailed information.
3. Use the list and form views to manage room types effectively.
