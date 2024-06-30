# Barnets Barbershop

![mockup2](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/fc8b2805-3753-4529-a66b-9744fd50b922)

## Project Overview
A Barber Shop Booking System

External User's Goal:
The user would like to book an appointment for a haircut and/or beard grooming service at a particular time and date.

Site Owner's Goal:
The site owner would like the ability to take online bookings for their barber shop.

## Features

### Home page and Hero
When a user lands on the website they are greeted with an attractive hero design. The call to action button prompts authenticated users to book and appointment.
If user is not authenticated the call to action button prompts users to "sign up or login to book and appointment"

![hero](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/71999812-5b52-433b-9499-13bbcbe30350)

### Booking form

The appointments page offers user the ability to create, view, update and delete appointments (full CRUD functionality) at the barbershop. Users are able to select their prefered time and date, required service and the ability to add additonal information for the barber.

![booking_form](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/f2043af8-d875-4514-8d0a-876f63f429e4)

![booking_form_date](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/7cae6d00-48b1-4c9f-a7f1-e01fbc2ee5fe)

![booking_form_services](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/3cf2d7fe-f575-4431-852c-f1fce8b9d291)


Upon creating a booking, users recieve feedback at the top of the page to confirm their appointment has been made. Furthermore, bookings that have been created by the user are then displayed in a list above the booking form along with cancel and edit buttons for each appointment. 

![appointment_details](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/aaf76f70-8af6-42e2-b176-676949fde9fe)


If a user presses the edit button they are taken to a new instance of the booking form where they can amend any of the appointment details. 

![edit_booking](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/a4204ffb-8a51-4dea-a9c9-0aa2ba8a8090)


If a user presses the cancel buttons they are redirected to the confirm_cancel page and prompoted to confirm the action. This feature avoids appointments being cancelled by the user in error.


![confirm_cancel](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/4d884185-7c1f-448d-8c88-6e4fff67b02e)

## Admin / superuser
The admin panel can only be reached by an authenticated superuser and it diplays appointment booking details in a list. 

![admin_bookings](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/c7bd6798-3e64-4532-898e-2e153cf76efb)

This list can be filtered by user, service, date, week and month.


![admin_filter](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/79c75582-670e-415e-a022-ccb6c5a7870d)


The superuser can also create, edit and delete appointments directly in the admin panel.

![admin_booking](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/6cc96a5a-d050-4fe4-b747-346241677dfa)

### Authentication

Django-allauth is used to handle user authentication. Users can create an account, verify email addresses and reset passwords.

![sign_in](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/d3825ee2-2ce7-418b-bf54-467f4159c491)

## Features Left to Implement

- Logic to avoid double bookings
- Add customer to mailing list
- Barbers blog section
- Send appointment reminder notifications
- Customer review and feedback form
- Customer contact form

## UX Design

Wireframe

![mobile](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/4eb7ddaf-e8ea-4c10-b2a3-fbe665eb6352)

## Data Model E.R.D

![ERD](https://github.com/chrissuttondev/Barnets-Barbershop/assets/136370848/12c6b3f0-1658-4f5f-84c5-90be205f534a)


## Validation

Python code was passed through Code Institute Python Linter and returned no errors.
Html code was passed through https://validator.w3.org/ and returned no errors.
CSS code was through https://jigsaw.w3.org/css-validator/ and returned no errors (CSS level 3 + SVG)
Html code was passed through https://websiteaccessibilitychecker.com/ and returned 12 known errors. These were all related to icon sizes and will not 
affect a user using a screen readers ability to navigate the site.

## Manual Testing

Manual testing was carried out against the 'Must Have' User Stories acceptance criteria.

- User Story: Authentication = PASS
- User Story: About Section = PASS
- User Story: View available appointment times = PASS
- User Story: User - Create, cancel, and update bookings = PASS
- User Story: User Landing = PASS
- User Story: Business Owner - View upcoming bookings = PASS
- User Story: User - Provide additional information = PASS

## Deployment

### Prerequisites

#### Database

Create an ElephantSQL database instance.
Ensure Ubuntu version is 12 or higher.

#### Workspace

- To connect the database, create an environment variable in env.py.
- pip3 install dj-database-url and psycopg2.
- Add DATABASE_URL os.environ to settings.py.
- Set DEBUG to False in settings.py.
- Create env.py file at the top level of the project.
- Add env.py to .gitignore to stop it being tracked by git.
- Add environment variables (Django SECRET_KEY and DATABASE_URL) to env.py (example).
- Install gunicorn and whitenoise, and add them to requirements.txt.
- Configure static root in settings.py.
- Run python3 manage.py collectstatic in terminal.
- Add .herokuapp.com to ALLOWED_HOSTS constant in settings.py.
- git add ., commit, and push changes to GitHub.

## Heroku Deployment

- Create a new Heroku app and navigate to settings.
- In settings, click 'Reveal Config Vars'.
- Add:
  DISABLE_COLLECTSTATIC = 1
  SECRET_KEY = ###############
  DATABASE_URL = #############
- Navigate to the deployment tab.
- Connect the app to the GitHub repository.
- Click deploy branch.

## Technologies Used
Django - Project Framework
Python - Backend Language
HTML - Frontend Structure
CSS - Frontend Styling
Bootstrap 5.3 - Frontend Styling
Heroku - Deployment
Gitpod - Coding Workspace
Git - Version Control
GitHub - Repository

## Credits
Rory Patrick Sheridan - Mentor
Code Institute Tutor Support
Pexels.com - Images used on the website
ElephantSQL - Database

## References
Django Tutorial On How To Create A Booking System For A Health Clinic by John Abdsho Khosrowabadi
https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78

Getting Started with Django by Corey Schafer
https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p by Corey Schafer















