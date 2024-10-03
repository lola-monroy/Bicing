# Bicing - Barcelona Bike Sharing Data Analysis

## Project Overview
This repository contains code for analyzing and visualizing the data from Barcelona's bike-sharing system, Bicing. The goal is to provide insights into bike availability, station usage, and general trends within the system.

## Features
- Data collection and preprocessing of Bicing data.
- Exploratory data analysis (EDA) to uncover key trends and patterns.
- Visualization tools for understanding station usage, availability, and more.
- Predictions of bike availability using various machine learning techniques.
  
## Prerequisites
To run the project, you will need the following:
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/lola-monroy/Bicing.git
    ```
2. Navigate into the project directory:
    ```bash
    cd Bicing
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. To preprocess the Bicing data, run:
    ```bash
    python preprocess_data.py
    ```
2. To perform exploratory data analysis, run:
    ```bash
    python eda.py
    ```
3. For predictions on bike availability:
    ```bash
    python predict_bike_availability.py
    ```

## Project Structure
- `data/` : Contains raw Bicing data files.
- `src/` : Contains scripts for data processing, analysis, and model building.
- `notebooks/` : Jupyter notebooks for visualizing the results.
- `requirements.txt` : Lists the dependencies required for the project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions
Feel free to open issues or submit pull requests for improvements or bug fixes. Contributions are welcome!
