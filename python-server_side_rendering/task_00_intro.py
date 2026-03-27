#!/usr/bin/env python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid input type. 'template' must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type. 'attendees' must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(content)
            print(f"Generated: {output_filename}")
        except OSError as e:
            print(f"Error writing file '{output_filename}': {e}")
