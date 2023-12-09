# PY-Text-Summarizer-App
A Flask-based web application for text summarization using SBERT (Sentence-BERT).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

The Text Summarizer App is a web application built with Flask that leverages the SBERT (Sentence-BERT) model for text summarization. Users can input text and choose the number of sentences in which the text will be summarized, and the application will provide a summarized version of the input.

## Features

- Summarize text using the SBERT model.
- Web-based interface for easy interaction.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/djordje34/PY-Text-Summarizer-App.git
    cd PY-Text-Summarizer-App
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:8000/](http://localhost:8000/).
3. Enter the text you want to summarize and click the "Summarize" button.

## Configuration

The application does not require specific configuration. However, you may customize it according to your needs.
