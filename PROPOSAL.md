# Yandiya Technologies CBM Calculator Proposal

### By Elvis Obero-Atkins

## Context of Project + Defining the Scope of the Project

- Yandiya currently uses Odoo (which is an open-source software platform that offers a range of useful software packages for business) for its product inventory management
- Odoo, as it is an open-source platform, allows for the development of “modules” which can add added functionality, automation or integration with other software systems.
- The Project is the development of a CBM Calculator (Cubic Meter Calculator) made specifically for Yandiya’s Far Infrared Heating Panels.
- The calculator would allow Yandiya’s warehouse management employees to input the type and quantity of products a customer ordered and calculate and output the most cost-effective configuration of how the products should be distributed.
- It will consider pallet or package, how many products per pallet and whether products should be left in their inner carton or outer carton.
- The calculator needs to be able to accept input from the Odoo warehouse management program.

<p align="right">(<a href="#top">back to top</a>)</p>

## Outline of my proposed solution

- My proposed solution for the project is to implement the CBM calculator in python.
- I chose this language as it is Odoo’s primary language for development and because all of Yandiya’s work placement students are familiar which would allow any of them to contribute to the development of the CBM calculator.
- My proposed solution would also be implemented as a custom python library rather than a direct Odoo module.
- My reasoning for this is that it would allow for the reusability of the code as if Yandiya in the future changes warehouse management software's most of the code can be reused.
- Another reason for implementing it as a library is that it would make it easier for the development of other programs that would need the CBM calculator
- Such as a Web interface that would allow warehouse employees to get an estimate and a 3D visualization of the CBM.

<p align="right">(<a href="#top">back to top</a>)</p>

## Stored Data Required by my proposed solution
These will be in a appropriate file format such as CSV / Excel, JSON, SQL (MySQL, SQL Server, postgresql or SQLLite) or Database files etc
- Product Details:
    - Full product list
    - Each product‘s inner carton, outer carton dimensions and weight.
- Pallet Details:
  - Dimensions of each pallet type
  - Maximum weight and height for each pallet type
  - Pricing per Postcode for each pallet type
- Parcel Details:
  - Pricing per Postcode

<p align="right">(<a href="#top">back to top</a>)</p>

## Potential issues and how they will be mitigated

- The only potential issues I can currently foresee is that if the Odoo inventory management store’s the product details data in a different format to how the Odoo module does, there could be conflict when trying to get input from the inventory management to the Odoo module.

This could be mitigated by storing product details data in the Odoo module in the same format as the inventory management does.

<p align="right">(<a href="#top">back to top</a>)</p>

## What are the phases of the solution

- The first phase of the project will be the development of the CBM calculator and the development of the CBM library, which will hold all the logic for the calculations that would work out the values of the CBM. This phase will also include a simplistic CLI or basic GUI program that would be developed for the purpose of testing the usability of the library.
- The second phase of the project will be the development of the Odoo module that integrates with the warehouse inventory management system and uses the CBM calculator library.
- The third / future phase(s) of the project could include the development of a WebUI version to allow warehouse management employees to draft/test what products would fit onto a pallet; future phases could also include 3D visualization of the CBM either as a standalone or as part of the WebUI.

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Deliverables and Success Criteria – measuring the success of the solution via “milestones”

The milestones refer to the success of the project regardless of phases, this allows us to measure the success of the project and know how much more development time remains.

- The first milestone would be getting the solution to correctly calculate CBM for any combination of product type and quantity
- The second milestone would be getting the solution to decide when to use inner cartons or outer cartons (for the products this applies to)
- The third milestone would be getting the solution to correctly decide what is the appropriate pallet type or size to use
- The fourth milestone would be getting the solution to correctly decide whether or not to send the products via parcel force which requires additional logic – weight consideration
- The fifth milestone would be getting the solution to correctly calculate the price of sending the products based on pallet / parcel and postcode

<p align="right">(<a href="#top">back to top</a>)</p>

## Potential Tech Stack

As well as the technologies listed below, I think git / GitHub should be used to easily keep a good version control.
Some potential libraries to be used for the first phase include:

- Pandas for data manipulations and calculations
- NumPy for more complex calculations
- Statsmodel for data manipulation and statics

Some potential libraries to be used for the future phases (web UI and 3D visualization):

- PyScript for web UI as it allows more direct interaction with HTML and JavaScript
- Flask / Django for web UI as having a python-based backend would ensure better compatibility with the CBM calculator library (although PyScript could negate this)
- Three.js 3D for 3D visualization for web UI
- Pandas3D for 3D visualization for web UI but is python-based alternative

<p align="right">(<a href="#top">back to top</a>)</p>

## How the solution will be documented

The Project will be documented in the following ways:

- DocStrings will be used in all code to explain the purpose of each function
- Upon the completion of Phase 1 the readme file in the git repository will contain a long description of the project

<p align="right">(<a href="#top">back to top</a>)</p>

## Plan of how solution should be tested

- After Phase 1 is finished a CLI or basic GUI python program will be created to interact with the library so a user can input variables to see if the calculations are correct.
- In future phases the solution will be tested on usability and ease of use rather than functionality as all core logic and functionality will be completed before any further development starts in future phases

<p align="right">(<a href="#top">back to top</a>)</p>
