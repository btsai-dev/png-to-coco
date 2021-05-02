# LSU Lamda Crack Detection

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Python
Tested with Python 3.7+

### Installing

- Clone the repository
```console
git clone https://github.com/btsai-dev/lsu-lamda-crack-detection.git
```

- Install all necessary dependencies. It is highly recommended to install dependencies in a virtual environment
```console
# For Python venv
pip install -r requirements.txt
```

### Run the Colorseg demo
- Navigate to ```samples\gen_training_data```  and execute the demo annotation program.
```console
python3 genTraining.py -m sample_dir
```
- Program attempts to annotate the marked files in the ```samples\gen_training_data\sample_dir\marked``` folder.

- The output annotated json file will be written to the same folder as ```annotations.json```.