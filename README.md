<<<<<<< HEAD
<!-- PROJECT OVERVIEW -->
<br />
<p align="center">
  <img src="doc/img/logo.jpg" alt="LSU" width="291" height="363">

  <h1 align="center">AI-Assisted Crack Detection for LAMDA Project</h1>
  <p align="center">
    <a href="https://github.com/btsai-dev/lsu-lamda-crack-detection">View Demo</a>
    ·
    <a href="https://github.com/btsai-dev/lsu-lamda-crack-detection/issues">Report Bug</a>
    ·
    <a href="https://github.com/btsai-dev/lsu-lamda-crack-detection/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Repository

This repository contains code relevant to crack detection as part of the Louisiana Materials Design Alliance (LAMDA) project. The LAMDA project is led by [Dr. Shengmin Guo](https://www.lsu.edu/eng/mie/people/faculty/guo.php) ([LSU MIE](https://www.lsu.edu/eng/mie/)) and is funded by the National Science Foundation. The project is researching the development of new materials in additive manufacturing.

### Related Links

* [Press Release](https://www.lsu.edu/mediacenter/news/2020/05/21engineering_khonsari_lamda.php)
* [NSF Award Page](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1946231)

### Built With

* [OpenCV](https://opencv.org/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.4+
* pip 20.1.0+

```sh
pip install -U pip 		# Linux or MacOS
python -m pip install -U pip	# Windows	
```

### Installation

1. Navigate to root directory
2. Prepare development environment

```sh
pip3 install -r requirements.txt	# Linux of MacOS
pip install -r requirements.txt		# Windows
```

<!-- USAGE EXAMPLES -->
## Usage

Example code can be found in the ```samples``` folder.

<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.


=======
# PNG to COCO

Converts png paint-brushed images into the COCO dataset format using color.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Python
Python 3.7+

### Installing

- Clone the repository
```console
git clone https://github.com/btsai-dev/png-to-coco.git
```

- Install all necessary dependencies. It is highly recommended to install dependencies in a virtual environment
```console
# For Python venv
pip install -r requirements.txt
```

### Execution
The Program expects the following file-structure format:

    dataset_name
    ├── Annotation Files
    │ ├── Category0
    │ │   ├── filename_0.jpg
    │ │   └── filename_1.jpg
    │ │   └── ...
    │ └── Category1
    │     ├── filename_0.jpg
    │     ├── filename_1.jpg
    │     └── ...
    └── Original Images Files
      ├── filename_0.jpg
      ├── filename_1.jpg
      └── ...

Note that, to ensure the right annotations for each category are associated with the right original image files, their filenames must all be identical.
The resulting annotation file will be placed inside the Original Images Files folder.

Files in each category without an associating file in the Original Image files will be skipped and a warning will be printed to the console.

### Run the Colorseg demo
- Navigate to ```samples/gen_training_data```  and execute the demo annotation program.
```console
python3 convert.py -a "sample_dataset/annotations" -o "sample_dataset/original"
```
- The output annotated json file will be written to the original image file directory as ```annotation_<DATE+TIME>.json```
>>>>>>> colorseg-dev
