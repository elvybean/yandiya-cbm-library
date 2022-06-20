# Yandiya CBM Library

## Current: Version 0.1.1 | In Development: Version 0.2

- a python library written for Yandiya Technologies Ltd during my T Level Industry Placement.
- currently meets 2 out of 5 of the milestones listed in the proposal
  - almost meets a 3rd milestone - 50% the way there

## Description

This Python library is being written for Yandiya Technologies Ltd. Its purpose is to allow their employees to easily calculate the CBM (Cubic Meter) of their products.

The library takes user input of which of Yandiya's products they are packaging and it calculates the CBM, whether to use a pallet or parcel, if appicable which type of pallet would be best to use and the cost of delivery.

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

<p align="right">(<a href="#top">back to top</a>)</p>

#### Libraries

[openpyxl](https://pypi.org/project/openpyxl/) - which can be installled via pip once in the same directory python

```
pip install openpyxl
```

OR if the py global variable is enabled the following line can be used as an alternative

```
py -m pip install openpyxl
```
<p align="right">(<a href="#top">back to top</a>)</p>

#### OS version

Developed and tested on Windows 10 Pro 21H1 - has not been tested on other versions of Windows (7, 8, 8.1 or 11) or Windows 10 (21H2 +) but there is no reason for there to issue.

### Installing

```
This README.md section is unfinshed
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Executing program

```
This README.md section is unfinshed
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Potential Future Adddions

- Odoo Module to interact with the python library
- Web UI to interact with the python library - using pyscript
- pip package to simlify instillation of library

<p align="right">(<a href="#top">back to top</a>)</p>

## Authors

Contributors names and contact info

- Elvis Obero-Atkins [GitHub](https://github.com/elvybean) | [LinkedIn](www.linkedin.com/in/elvisoberoatkins)
- Ethan Cooksley [GitHub](https://github.com/eocooksley535) | [LinkedIn](https://www.linkedin.com/in/ethan-cooksley-a0666b238/)
- Jack Macguire [GitHub](#) | [LinkedIn](#)

<p align="right">(<a href="#top">back to top</a>)</p>

## Version History

### Version 0.2
#### Contributers: Elvis Obero-Atkins

```
In Development
```

### Version 0.1.1
#### Contributers: Elvis Obero-Atkins

- Fixed various spelling errors
- Reorganised file structure
- Minimal python logic changes
- started development of multiple item types on cbm [see commit](https://github.com/elvybean/yandiya-cbm-library/commit/b73434699832051913fc05ad7161e206b8854f66)

### Version 0.1
#### Contributers: Elvis Obero-Atkins

- Accesses Yandiya's product data from yandiya-db.xlsx
- Library takes user input for PartNo, sku or barcode
- Searches excel file for the product the user is looking for
- Calculates CBM for the product based on it's dimensions and quantity of the product
- Calculates based on the total weight weather to send products via pallets or parcel
- Has basic error messages in the event the search returns no values

<p align="right">(<a href="#top">back to top</a>)</p>

## Repo Fork(s)

### [Excel Postcode Sheet & Additional Development](https://github.com/eocooksley535/yandiya-cbm-library) 
#### Contributers: Ethan Cooksley | Developers: Ethan Cooksley & Jack Macguire

- Repo forked from [this commit](https://github.com/elvybean/yandiya-cbm-library/commit/4db2e7c4f7daca418048e6472bedf502df0fd242)

<p align="right">(<a href="#top">back to top</a>)</p>

## License

This project is licensed under the [MIT Lisence](https://choosealicense.com/licenses/mit/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Acknowledgments

Inspiration, code snippets, etc.

- [cbmcalculator.com for the Web UI inspiration](https://www.cbmcalculator.com/)
- [Dominique Pizzie&#39;s Gist for the README.md Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)

<p align="right">(<a href="#top">back to top</a>)</p>
