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