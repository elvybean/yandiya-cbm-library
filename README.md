<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]

<br />
<div align="center">
  <a href="https://github.com/elvybean/yandiya-cbm-library">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Yandiya CBM Library</h3>
<h4 align="center">Current: Version 0.2.3 | In Development Version 0.2.4</h4>
<p> a python library consisting of; a custom python package, odoo module and web user interface written for Yandiya Technologies Ltd during my T Level Industry Placement and further developed during my Summer Internship </p<

</div> 
<div align="left">
  
## Description

This Python library is being written for Yandiya Technologies Ltd. Its purpose is to allow their employees to easily calculate the CBM (Cubic Meter) of their products.

The library takes user input of which of Yandiya's products they are packaging and it calculates the CBM, whether to use a pallet or parcel, if appicable which type of pallet would be best to use and the cost of delivery.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#knowledge-prerequisites">Knowledge Prerequisites</a></li>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#milestones-and-roadmap">Milestones & Roadmap</a></li>
     <li><a href="#authors">Authors</a></li>
    <li><a href="#version-history">Version History</a></li>
    <li><a href="#repo-forks">Repo Forks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

![Product Name Screen Shot][product-screenshot]

```
This README.md section is unfinshed
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [python 3.10](https://www.python.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Knowledge Prerequisites

The following knowledge is required to effectively contribute to this repo:

- Python basics and fundamentals
- Array manipulation in python
- openpyxl basics and fundamentals
  - OR csv library basics and fundamentals - as syntax between the two libraries are similar
- Git and Github basics (obviously)

###### If you lack any knowledge in these areas it is recommended you read up on them

<p align="right">(<a href="#top">back to top</a>)</p>

### Dependencies

#### Prerequisites

- [Python 3.10](https://www.python.org/downloads/) - older versions are likely to work as the code base doesn't utalize any python 3.10 specific features but this can't be ensured as no previous versions have been tested
- [yandiya-db.xlsx](https://github.com/elvybean/yandiya-cbm-library/blob/main/.main/yandiya-db.xlsx) - excel file that contains all the data required for the cbm library to function, this is located in the .main folder of the repo
- [openpyxl](https://pypi.org/project/openpyxl/) - which can be installled via pip once in the python install directory

<p align="right">(<a href="#top">back to top</a>)</p>

#### OS version

Developed and tested on Windows 10 Pro 21H1 - has not been tested on other versions of Windows (7, 8, 8.1 or 11) or Windows 10 (21H2 +) but there is no reason for there to issue.

### Installation

```
This README.md section is unfinshed
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Execution

```
This README.md section is unfinshed
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Milestones and Roadmap

- [x] [Access Database (Excel)](https://github.com/elvybean/yandiya-cbm-library/milestone/12)
- [x] [Search for Product in Database (Excel)](https://github.com/elvybean/yandiya-cbm-library/milestone/13)
- [x] [CBM Calculations - singular product types](https://github.com/elvybean/yandiya-cbm-library/milestone/1)
- [x] [CBM Calculations - multiple product types](https://github.com/elvybean/yandiya-cbm-library/milestone/3)
- [x] [Packaging Logic](https://github.com/elvybean/yandiya-cbm-library/milestone/2)
- [x] [Parcelforce & Pallet Selection Logic](https://github.com/elvybean/yandiya-cbm-library/milestone/10)
- [ ] [Price Calculation Logic](https://github.com/elvybean/yandiya-cbm-library/milestone/5)
- [x] [Three Dimensional Calculations](https://github.com/elvybean/yandiya-cbm-library/milestone/6)
- [ ] [PostgreSQL](https://github.com/elvybean/yandiya-cbm-library/milestone/14)
- [ ] [Web Interface](https://github.com/elvybean/yandiya-cbm-library/milestone/9)
- [ ] [Python Package](https://github.com/elvybean/yandiya-cbm-library/milestone/7)
- [ ] [Odoo Module](https://github.com/elvybean/yandiya-cbm-library/milestone/8)

See the [open issues](https://github.com/elvybean/yandiya-cbm-library/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

## Authors

Contributors names and contact info

- Elvis Obero-Atkins [GitHub](https://github.com/elvybean) | [LinkedIn](www.linkedin.com/in/elvisoberoatkins)

<p align="right">(<a href="#top">back to top</a>)</p>

## Version History

### Version 0.2.4

#### Contributers: Elvis Obero-Atkins

```
In Development
```

### Version 0.2.3 [go to commit]()

#### Contributers: Elvis Obero-Atkins

- Refactored file structure and module structure
- fully integrated py4dbp which is a python bin packing implemetation
  for the purpose of getting accurate 3 dimensional calculations
- updated tests and cli-app to utilize these new features

### Version 0.2.2 [go to commit](https://github.com/elvybean/yandiya-cbm-library/commit/c584706fa8ddc95fc030d9194a03928fb823b1bc)

#### Contributers: Elvis Obero-Atkins

- Refactored the file structure
- Refactored cbmcalculator.py into a local pyhton package called yandiyacbm
- functions of cbmcalculator.py was split into modules for further decomposition
- Refactored modules to make them more effiecent
- Refactored cli-app.py to make it more efficent and better meet PEP8
- added placeholder files and directories for odoo-module and web-ui

### Version 0.2.1 [go to commit](https://github.com/elvybean/yandiya-cbm-library/commit/d8ded715bbd3137efe298f2535ac7914d84e1874)

#### Contributers: Elvis Obero-Atkins

- refactored packaging logic as it created errors in certain edge cases
- calculates whether to send products via parcel or pallet (types) based on weight and CBM
- created test_shipping_logic.py to test the new shipping_logic function

### Version 0.2 [go to commit](https://github.com/elvybean/yandiya-cbm-library/commit/b95ea9a8c05951ad5e4707492b4af880fae2cf64)

#### Contributers: Elvis Obero-Atkins

- Added fucntion that calculates CBM of multiple product types
- Completely refactored cli-app
- cli-app creates 2D arrays for input for cbmcalculator

### Version 0.1.1 [go to commit](https://github.com/elvybean/yandiya-cbm-library/commit/db9bcbaa384f233411c3a0b2e108904e21bd056c)

#### Contributers: Elvis Obero-Atkins

- Fixed various spelling errors
- Reorganised file structure
- Minimal python logic changes
- started development of multiple item types on cbm

### Version 0.1 [go to commit](https://github.com/elvybean/yandiya-cbm-library/commit/c6076c3a13dfb1bab704bc005549391a104953a6)

#### Contributers: Elvis Obero-Atkins

- Accesses Yandiya's product data from yandiya-db.xlsx
- Library takes user input for PartNo, sku or barcode
- Searches excel file for the product the user is looking for
- Calculates CBM for the product based on it's dimensions and quantity of the product
- Calculates based on the total weight weather to send products via pallets or parcel
- Has basic error messages in the event the search returns no values

<p align="right">(<a href="#top">back to top</a>)</p>

## Repo Forks

### [Excel Postcode Sheet & Additional Development](https://github.com/eocooksley535/yandiya-cbm-library) (Stagnated Development)

#### Contributers: Ethan Cooksley | Developers: Ethan Cooksley & Jack Macguire

- Repo forked from V0.1.1 specifically [commit 51](https://github.com/elvybean/yandiya-cbm-library/commit/4db2e7c4f7daca418048e6472bedf502df0fd242)

<p align="right">(<a href="#top">back to top</a>)</p> 
  
## Contributing
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## License

This project is licensed under the [MIT Lisence](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

Inspiration, code snippets, etc.

- [cbmcalculator.com for the Web UI inspiration](https://www.cbmcalculator.com/)
- [Dominique Pizzie&#39;s Gist for the README.md Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
- [othneildrew&#39;s Repo for the README.md Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/elvybean/yandiya-cbm-library.svg?style=for-the-badge
[contributors-url]: https://github.com/elvybean/yandiya-cbm-library/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/elvybean/yandiya-cbm-library.svg?style=for-the-badge
[forks-url]: https://github.com/elvybean/yandiya-cbm-library/network/members
[issues-shield]: https://img.shields.io/github/issues/elvybean/yandiya-cbm-library.svg?style=for-the-badge
[issues-url]: https://github.com/elvybean/yandiya-cbm-library/issues
[product-screenshot]: images/screenshot.png

</div>
